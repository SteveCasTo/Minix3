def eliminar_documento():
    ventana_eliminar = tk.Toplevel()
    ventana_eliminar.title("Eliminar Documento")
    ventana_eliminar.geometry("400x300")

    with Session() as session:
        try:
            # Obtener el ID del usuario actual
            id_user = obtener_id_usuario(session, user)

            # Listar archivos propios
            archivos_propios = listar_archivos_usuario(session, id_user)
            lista_archivos_propios = [f"Propio: {archivo.nombre_archivo}" for archivo in archivos_propios]

            # Listar archivos compartidos
            archivos_compartidos = listar_archivos_compartidos(session, id_user)
            lista_archivos_compartidos = [f"Compartido: {archivo.nombre_archivo}" for archivo in archivos_compartidos]

            # Combinar ambas listas
            lista_documentos = lista_archivos_propios + lista_archivos_compartidos

        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los documentos. Error: {e}")
            ventana_eliminar.destroy()
            return

    # Verificar si hay documentos disponibles
    if not lista_documentos:
        messagebox.showerror("Error", "No hay documentos disponibles para eliminar.")
        ventana_eliminar.destroy()
        return

    # Crear interfaz de selección
    label_documento = tk.Label(ventana_eliminar, text="Selecciona el archivo a eliminar:")
    label_documento.pack(pady=5)
    variable_documento = tk.StringVar(ventana_eliminar)
    variable_documento.set(lista_documentos[0])  # Valor inicial
    menu_documento = tk.OptionMenu(ventana_eliminar, variable_documento, *lista_documentos)
    menu_documento.pack(pady=5)

    def confirmar_eliminar():
        nom_achv = variable_documento.get()
        nom_achv = nom_achv.split(": ", 1)[1]  # Extraer nombre del archivo

        with Session() as session:
            try:
                # Eliminar el archivo de la base de datos
                eliminar_archivo_por_nombre(session, nom_achv)
                messagebox.showinfo("Éxito", f"El archivo '{nom_achv}' ha sido eliminado exitosamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar el archivo. Error: {e}")
            finally:
                ventana_eliminar.destroy()

    # Botones de confirmación y cancelación
    button_confirmar = tk.Button(ventana_eliminar, text="Eliminar", command=confirmar_eliminar)
    button_confirmar.pack(pady=10)
    button_cancelar = tk.Button(ventana_eliminar, text="Cancelar", command=ventana_eliminar.destroy)
    button_cancelar.pack(pady=5)





def listar_archivos_usuario(session, id_user):
    return session.query(Archivo).filter_by(id_usuario=id_user).all()

def listar_archivos_compartidos(session, id_user):
    return session.query(Archivo).join(CompartirArchivo).filter(CompartirArchivo.id_usuario_compartido == id_user).all()

def eliminar_archivo_por_nombre(session, nombre_archivo):
    archivo = session.query(Archivo).filter_by(nombre_archivo=nombre_archivo).first()
    if archivo:
        session.delete(archivo)
        session.commit()
    else:
        raise Exception("Archivo no encontrado.")

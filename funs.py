def mover_documento():
    ventana_mover = tk.Toplevel()
    ventana_mover.title("Mover Archivo")
    ventana_mover.geometry("400x300")

    # Obtener archivos propios del usuario actual
    try:
        id_user = obtener_id_usuario(neo4j_conn, user)
        archivos_propios = listar_archivos_usuario(neo4j_conn, id_user)
        lista_archivos_propios = [f"Propio: {archivo['nombre_archivo']}" for archivo in archivos_propios]
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo obtener los archivos del usuario. Error: {e}")
        ventana_mover.destroy()
        return

    if not lista_archivos_propios:
        messagebox.showerror("Error", "No hay archivos disponibles para mover.")
        ventana_mover.destroy()
        return

    # Crear la interfaz gráfica
    label_archivo = tk.Label(ventana_mover, text="Selecciona el archivo a mover:")
    label_archivo.pack(pady=5)
    variable_archivo = tk.StringVar(ventana_mover)
    variable_archivo.set(lista_archivos_propios[0])  # Valor inicial
    menu_archivo = tk.OptionMenu(ventana_mover, variable_archivo, *lista_archivos_propios)
    menu_archivo.pack(pady=5)

    def seleccionar_carpeta_destino():
        ruta_carpeta = filedialog.askdirectory()
        if ruta_carpeta:
            entry_carpeta.delete(0, tk.END)
            entry_carpeta.insert(0, ruta_carpeta)

    label_carpeta_destino = tk.Label(ventana_mover, text="Seleccionar carpeta de destino:")
    label_carpeta_destino.pack(pady=5)
    entry_carpeta = tk.Entry(ventana_mover, width=30)
    entry_carpeta.pack(pady=5)
    button_seleccionar_carpeta = tk.Button(ventana_mover, text="Seleccionar Carpeta", command=seleccionar_carpeta_destino)
    button_seleccionar_carpeta.pack(pady=5)

    def confirmar_mover():
        nom_archivo = variable_archivo.get().split(": ", 1)[1]  # Extraer nombre del archivo
        ruta_nueva_carpeta = entry_carpeta.get()

        if not ruta_nueva_carpeta:
            messagebox.showerror("Error", "Debe seleccionar una carpeta de destino.")
            return

        try:
            # Obtener la ruta actual del archivo
            query_ruta_actual = """
            MATCH (a:Archivo {nombre_archivo: $nom_archivo})<-[:POSEE]-(u:Usuario)
            WHERE elementId(u) = $id_user
            RETURN a.ruta_archivo AS ruta_actual
            """
            result = neo4j_conn.run_query(query_ruta_actual, {"nom_archivo": nom_archivo, "id_user": id_user})
            ruta_actual = result[0]["ruta_actual"]

            # Mover físicamente el archivo
            nueva_ruta = os.path.join(ruta_nueva_carpeta, os.path.basename(ruta_actual))
            shutil.move(ruta_actual, nueva_ruta)

            # Actualizar la ruta en la base de datos
            query_actualizar_ruta = """
            MATCH (a:Archivo {nombre_archivo: $nom_archivo})<-[:POSEE]-(u:Usuario)
            WHERE elementId(u) = $id_user
            SET a.ruta_archivo = $nueva_ruta
            """
            neo4j_conn.run_query(query_actualizar_ruta, {
                "nom_archivo": nom_archivo,
                "id_user": id_user,
                "nueva_ruta": nueva_ruta
            })

            messagebox.showinfo("Éxito", f"El archivo '{nom_archivo}' ha sido movido correctamente a '{ruta_nueva_carpeta}'.")

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo mover el archivo. Error: {e}")

        finally:
            ventana_mover.destroy()

    button_confirmar = tk.Button(ventana_mover, text="Mover Archivo", command=confirmar_mover)
    button_confirmar.pack(pady=10)
    button_cancelar = tk.Button(ventana_mover, text="Cancelar", command=ventana_mover.destroy)
    button_cancelar.pack(pady=5)

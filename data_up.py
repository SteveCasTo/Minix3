def crear_documento_texto():
    crear_documento(1, ".txt")

def crear_documento_excel():
    crear_documento(2, ".xlsx")

def crear_documento(id_tip, nom_tip):
    ventana_crear = tk.Toplevel()
    ventana_crear.title("Crear Documento")
    ventana_crear.geometry("400x300")

    label_nombre = tk.Label(ventana_crear, text="Nombre del archivo:")
    label_nombre.pack(pady=5)
    entry_nombre = tk.Entry(ventana_crear, width=30)
    entry_nombre.pack(pady=5)

    def seleccionar_carpeta():
        ruta_carpeta = filedialog.askdirectory()
        if ruta_carpeta:
            entry_carpeta.delete(0, tk.END)
            entry_carpeta.insert(0, ruta_carpeta)

    label_carpeta = tk.Label(ventana_crear, text="Seleccionar carpeta de destino:")
    label_carpeta.pack(pady=5)
    entry_carpeta = tk.Entry(ventana_crear, width=30)
    entry_carpeta.pack(pady=5)

    button_seleccionar_carpeta = tk.Button(ventana_crear, text="Seleccionar Carpeta", command=seleccionar_carpeta)
    button_seleccionar_carpeta.pack(pady=5)

    def confirmar_crear():
        nombre_archivo = entry_nombre.get()
        ruta_carpeta = entry_carpeta.get()
        nombre_carpeta = os.path.basename(ruta_carpeta)
        
        if not nombre_archivo:
            messagebox.showerror("Error", "El nombre del archivo es obligatorio.")
            return
        if not ruta_carpeta:
            messagebox.showerror("Error", "La ruta de la carpeta es obligatoria.")
            return

        ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo + nom_tip)
        
        # Crear contenido simulado como bytes vacíos (no se crea el archivo real)
        contenido_binario = b''

        with Session() as session:
            try:
                # Obtener el ID del usuario actual
                id_user = obtener_id_usuario(session, user)
                
                # Obtener o crear la carpeta en la base de datos
                id_carpeta = obtener_id_carpeta(session, ruta_carpeta, nombre_carpeta, id_user)
                
                # Insertar el archivo en la base de datos
                insertar_archivo(session, id_user, id_tip, nombre_archivo, ruta_archivo, datetime.now(), contenido_binario)
                
                messagebox.showinfo("Éxito", f"Se ha creado el archivo '{nombre_archivo}' en la carpeta '{ruta_carpeta}'.")

            except Exception as e:
                messagebox.showerror("Error", f"No se pudo crear el archivo. Error: {e}")

            finally:
                ventana_crear.destroy()

    button_confirmar = tk.Button(ventana_crear, text="Crear Archivo", command=confirmar_crear)
    button_confirmar.pack(pady=10)
    button_cancelar = tk.Button(ventana_crear, text="Cancelar", command=ventana_crear.destroy)
    button_cancelar.pack(pady=5)






def obtener_id_usuario(session: Session, nombre_usuario: str):
    usuario = session.query(Usuario).filter_by(nombre_usuario=nombre_usuario).first()
    return usuario.id_usuario if usuario else None

def obtener_id_carpeta(session: Session, ruta_carpeta: str, nombre_carpeta: str, id_usuario: int):
    carpeta = session.query(Carpeta).filter_by(ruta_carpeta=ruta_carpeta).first()
    if carpeta:
        return carpeta.id_carpeta
    else:
        nueva_carpeta = Carpeta(nombre_carpeta=nombre_carpeta, ruta_carpeta=ruta_carpeta, id_usuario=id_usuario)
        session.add(nueva_carpeta)
        session.commit()
        return nueva_carpeta.id_carpeta

def insertar_archivo(session: Session, id_usuario: int, id_tipo: int, nombre_archivo: str, ruta_archivo: str, creacion_archivo, contenido_binario: bytes):
    nuevo_archivo = Archivo(
        id_tipo=id_tipo,
        id_usuario=id_usuario,
        nombre_archivo=nombre_archivo,
        ruta_archivo=ruta_archivo,
        creacion_archivo=creacion_archivo,
        contenido_archivo=contenido_binario
    )
    session.add(nuevo_archivo)
    session.commit()
    return nuevo_archivo

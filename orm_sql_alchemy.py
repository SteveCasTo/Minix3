import tkinter as tk
import os
import psycopg2
from tkinter import messagebox, filedialog
from functions import *
from sqlalchemy.orm import sessionmaker
from models import engine
from datetime import datetime

# Crear sesión de SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

user = None

# Funciones individuales (debes implementarlas)
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
        contenido_binario = b"Prueba"

        with Session() as session:
            try:
                # Obtener el ID del usuario actual
                id_user = obtener_id_usuario(session, user)
                
                # Obtener o crear la carpeta en la base de datos
                id_carpeta = obtener_id_carpeta(session, ruta_carpeta, nombre_carpeta, id_user, datetime.now())
                
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

def compartir_documento():
    ventana_compartir = tk.Toplevel()
    ventana_compartir.title("Compartir Documento")
    ventana_compartir.geometry("400x320")
    id_user = obtener_id_usuario(session, user)
    if not id_user:
        messagebox.showerror("Error", "Usuario no encontrado.")
        ventana_compartir.destroy()
        return

    lista_usuarios = listar_usuarios(session, id_user)
    lista_documentos = listar_documentos_usuario(session, id_user)
    
    if not lista_usuarios or not lista_documentos:
        messagebox.showerror("Error", "No hay usuarios o documentos disponibles para compartir.")
        ventana_compartir.destroy()
        return

    lista_nombres_usuarios = [usuario.nombre_usuario for usuario in lista_usuarios]
    lista_nombres_documentos = [documento.nombre_archivo for documento in lista_documentos]

    label_documento = tk.Label(ventana_compartir, text="Selecciona el archivo a compartir:")
    label_documento.pack(pady=5)
    variable_documento = tk.StringVar(ventana_compartir)
    variable_documento.set(lista_nombres_documentos[0])
    menu_documento = tk.OptionMenu(ventana_compartir, variable_documento, *lista_nombres_documentos)
    menu_documento.pack(pady=5)

    label_usuario = tk.Label(ventana_compartir, text="Selecciona el usuario:")
    label_usuario.pack(pady=5)
    variable_usuario = tk.StringVar(ventana_compartir)
    variable_usuario.set(lista_nombres_usuarios[0])
    menu_usuario = tk.OptionMenu(ventana_compartir, variable_usuario, *lista_nombres_usuarios)
    menu_usuario.pack(pady=5)

    label_fecha = tk.Label(ventana_compartir, text="Fecha de expiración (YYYY-MM-DD):")
    label_fecha.pack(pady=5)
    entry_fecha = tk.Entry(ventana_compartir)
    entry_fecha.pack(pady=5)

    def confirmar_compartir():
        nom_achv = variable_documento.get()
        nom_user_comp = variable_usuario.get()
        fecha_exp = entry_fecha.get()
        
        try:
            fecha_exp = datetime.strptime(fecha_exp, '%Y-%m-%d').date()
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha incorrecto.")
            return

        try:
            id_achv = obtener_id_documento(session, nom_achv)
            id_user_comp = obtener_id_usuario(session, nom_user_comp)

            if not id_achv or not id_user_comp:
                messagebox.showerror("Error", "No se pudo encontrar el archivo o el usuario especificado.")
                return

            compartir_archivo(session, id_achv, id_user, id_user_comp, datetime.now(), fecha_exp)
            messagebox.showinfo("Éxito", "El archivo ha sido compartido exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo compartir el archivo. Error: {e}")
        finally:
            ventana_compartir.destroy()

    button_confirmar = tk.Button(ventana_compartir, text="Compartir", command=confirmar_compartir)
    button_confirmar.pack(pady=10)
    button_cancelar = tk.Button(ventana_compartir, text="Cancelar", command=ventana_compartir.destroy)
    button_cancelar.pack(pady=5)

def eliminar_documento():
    messagebox.showinfo("Función", "Eliminar Documento")

def mover_documento():
    messagebox.showinfo("Función", "Mover Documento")

def crear_carpeta():
    messagebox.showinfo("Función", "Crear Carpeta")

def eliminar_carpeta():
    messagebox.showinfo("Función", "Eliminar Carpeta")

funciones_mapa = {
    "CrearDocumentoTexto": crear_documento_texto,
    "CrearDocumentoExcel": crear_documento_excel,
    "CompartirDocumento": compartir_documento,
    "EliminarDocumento": eliminar_documento,
    "MoverDocumento": mover_documento,
    "CrearCarpeta": crear_carpeta,
    "EliminarCarpeta": eliminar_carpeta
}

# Función para abrir la interfaz de Gestor de Archivos con botones por UI
def abrir_gestor_archivos(rol_usuario):
    # Crear una nueva ventana para el gestor de archivos
    root_gestor = tk.Toplevel()
    root_gestor.title("Gestor de Archivos")
    root_gestor.geometry("400x400")

    # Obtener las funciones disponibles según el rol
    id_rol = obtener_rol_id(session, rol_usuario)
    funciones_db = obtener_funciones_rol(session, id_rol)

    # Crear botones de función en el centro de la ventana
    for funcion_nombre in funciones_db:
        if funcion_nombre in funciones_mapa:
            button = tk.Button(root_gestor, text=funcion_nombre, command=funciones_mapa[funcion_nombre])
        else:
            button = tk.Button(root_gestor, text=funcion_nombre, command=lambda: messagebox.showerror("Error", "Función no disponible"))
        button.pack(pady=5)

# Función de autenticación
def autenticar():
    global user
    user = entry_user.get()
    contrasena = entry_password.get()
    usuario = user

    # Autenticación a través de la función SQLAlchemy
    usuarioA = autenticar_usuario(session, usuario, contrasena)

    if usuarioA:
        messagebox.showinfo("Éxito", f"Bienvenido {usuario}")
        root.withdraw()  # Ocultar ventana de login
        id_usuario = obtener_id_usuario(session, usuario)
        roles_usuario = obtener_roles_usuario(session, id_usuario)
        rol_usuario = roles_usuario[0]
        abrir_gestor_archivos(rol_usuario)
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Configuración de la ventana principal (Login)
root = tk.Tk()
root.title("Inicio de Sesión")
root.geometry("300x200")

# Etiqueta y campo de entrada para el usuario
label_user = tk.Label(root, text="Usuario:")
label_user.pack()
entry_user = tk.Entry(root, width=20)
entry_user.pack()

# Etiqueta y campo de entrada para la contraseña
label_password = tk.Label(root, text="Contraseña:")
label_password.pack()
entry_password = tk.Entry(root, show="*", width=20)
entry_password.pack()

# Botón para iniciar sesión
button_login = tk.Button(root, text="Iniciar Sesión", command=autenticar)
button_login.pack(pady=10)

# Botón para salir
button_exit = tk.Button(root, text="Salir", command=root.quit)
button_exit.pack()

# Ejecutar la interfaz
root.mainloop()

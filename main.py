import tkinter as tk
from tkinter import messagebox
from functions import obtener_funciones_por_rol, autenticar_usuario
from sqlalchemy.orm import sessionmaker
from models import engine

# Crear sesión de SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# Funciones individuales (debes implementarlas)
def crear_documento_texto():
    messagebox.showinfo("Función", "Crear Documento de Texto")

def crear_documento_excel():
    messagebox.showinfo("Función", "Crear Documento de Excel")

def compartir_documento():
    messagebox.showinfo("Función", "Compartir Documento")

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
    funciones_db = obtener_funciones_por_rol(session, rol_usuario)

    # Crear botones de función en el centro de la ventana
    for funcion in funciones_db:
        funcion_nombre = funcion["nombre"]
        if funcion_nombre in funciones_mapa:
            button = tk.Button(root_gestor, text=funcion_nombre, command=funciones_mapa[funcion_nombre])
        else:
            button = tk.Button(root_gestor, text=funcion_nombre, command=lambda: messagebox.showerror("Error", "Función no disponible"))
        button.pack(pady=5)

# Función de autenticación
def autenticar():
    usuario = entry_user.get()
    contrasena = entry_password.get()

    # Autenticación a través de la función SQLAlchemy
    rol_usuario = autenticar_usuario(session, usuario, contrasena)

    if rol_usuario:
        messagebox.showinfo("Éxito", f"Bienvenido {usuario}")
        root.withdraw()  # Ocultar ventana de login
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
button_login = tk.Button(root, text="Iniciar Sesión", command=iniciar_sesion)
button_login.pack(pady=10)

# Botón para salir
button_exit = tk.Button(root, text="Salir", command=root.quit)
button_exit.pack()

# Ejecutar la interfaz
root.mainloop()
import psycopg2
from psycopg2 import OperationalError
import tkinter as tk
from tkinter import messagebox
user = None
password = None
def conectar_postgres():
    global user
    global password
    user = entry_user.get()
    password = entry_password.get()
    try:
        # Conectar a la base de datos PostgreSQL
        conexion = psycopg2.connect(
            host="localhost",
            database="Gestor_Archivos",
            user=user,
            password=password
        )
        cursor = conexion.cursor()

        # Obtener el PID del proceso
        cursor.execute("SELECT pg_backend_pid();")
        pid = cursor.fetchone()[0]

        # Obtener el ID de usuario
        cursor.execute("SELECT id_usuario FROM Usuario WHERE nombre_usuario = %s;", (user,))
        id_user = cursor.fetchone()[0]

        # Obtener el rol del usuario
        cursor.execute("""SELECT nombre_rol FROM Rol JOIN Roles_User ON Rol.id_rol = Roles_User.id_rol WHERE Roles_User.id_usuario = %s;""", (id_user,))
        rol_usuario = cursor.fetchone()[0]  # Obtiene el rol del usuario

        # Insertar la sesión del usuario
        cursor.execute("SELECT insert_sesion(%s,%s);", (id_user, pid))
        conexion.commit()

        # Cerrar la conexión
        conexion.close()

        # Muestra el PID en el campo de texto
        text_pid.config(state=tk.NORMAL)
        text_pid.delete(1.0, tk.END)
        text_pid.insert(tk.END, f"PID: {pid}")
        text_pid.config(state=tk.DISABLED)

        messagebox.showinfo("Éxito", f"Conexión exitosa. Rol: {rol_usuario}")

        # Si la conexión fue exitosa, abrir la nueva interfaz y pasar el rol del usuario
        abrir_gestor_archivos(rol_usuario)

    except OperationalError as e:
        messagebox.showerror("Error", "Fallo en la conexión: Verifica las credenciales")
        text_pid.config(state=tk.NORMAL)
        text_pid.delete(1.0, tk.END)
        text_pid.config(state=tk.DISABLED)
        print(f"Error: {e}")

# Función para abrir la interfaz de Gestor de Archivos
def abrir_gestor_archivos(rol_usuario):
    # Crear una nueva ventana para el gestor de archivos
    root_gestor = tk.Toplevel()
    root_gestor.title("Gestor de Archivos")
    # Mapa de funciones
    funciones_mapa = {
        "CrearDocumentoTexto": crear_documento_texto,
        "CrearDocumentoExcel": crear_documento_excel,
        "CompartirDocumento": compartir_documento,
        "EliminarDocumento": eliminar_documento,
        "MoverDocumento": mover_documento
    }

    # Crear la barra de menús
    menu_bar = tk.Menu(root_gestor)

    # Obtener las funciones disponibles según el rol
    funciones_db = obtener_funciones_por_rol(rol_usuario)
    categorias = set([funcion["categoria"] for funcion in funciones_db])
    menus = {}

    for categoria in categorias:
        menus[categoria] = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label=categoria, menu=menus[categoria])

    for funcion in funciones_db:
        categoria_menu = menus[funcion["categoria"]]
        funcion_nombre = funcion["nombre"]
        if funcion_nombre in funciones_mapa:
            categoria_menu.add_command(label=funcion_nombre, command=funciones_mapa[funcion_nombre])
        else:
            categoria_menu.add_command(label=funcion_nombre, command=lambda: messagebox.showerror("Error", "Función no disponible"))

    # Asignar la barra de menús a la ventana
    root_gestor.config(menu=menu_bar)

# Obtener funciones desde la base de datos según el rol
def obtener_funciones_por_rol(rol):
    global user
    global password
    try:
        conexion = psycopg2.connect(
            host="localhost",
            database="Gestor_Archivos",
            user=user,
            password=password
        )
    except OperationalError as e:
        messagebox.showerror("Error", "Fallo en la conexión: Verifica las credenciales")
        print(f"Error: {e}")
    cursor = conexion.cursor()
    cursor.execute("""SELECT Funcion.nombre_funcion FROM Funcion JOIN Funciones_Rol ON Funcion.id_funcion = Funciones_Rol.id_funcion JOIN Rol ON Rol.id_rol = Funciones_Rol.id_rol JOIN Roles_User ON Rol.id_rol = Roles_User.id_rol WHERE Roles_User.estado = 'Activo' AND Rol.nombre_rol = %s;""", (rol,))
    funciones_db = cursor.fetchall()
    cursor.close()
    conexion.close()
    return [{"nombre": f} for f in funciones_db]

# Definir funciones simuladas (las puedes reemplazar por las funciones reales)
def crear_documento_texto():
    messagebox.showinfo("Función", "Se ha creado un nuevo documento de texto.")

def crear_documento_excel():
    messagebox.showinfo("Función", "Se ha creado un nuevo documento de Excel.")

def compartir_documento():
    messagebox.showinfo("Función", "Documento compartido exitosamente.")

def eliminar_documento():
    messagebox.showwarning("Función", "El documento ha sido eliminado.")

def mover_documento():
    messagebox.showinfo("Función", "El documento ha sido movido.")

# Configuración de la ventana principal (Login)
root = tk.Tk()
root.title("Conexión a PostgreSQL")
root.geometry("250x250")

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

# Botón para conectar
button_connect = tk.Button(root, text="Conectar", command=conectar_postgres)
button_connect.pack()

# Campo para mostrar el PID
label_pid = tk.Label(root, text="PID de la conexión:")
label_pid.pack()

text_pid = tk.Text(root, height=1, width=10)
text_pid.pack()
text_pid.config(state=tk.DISABLED)

# Botón para salir
button_exit = tk.Button(root, text="Cancelar", command=root.quit)
button_exit.pack()

# Ejecutar la interfaz
root.mainloop()

import psycopg2
from psycopg2 import OperationalError
import tkinter as tk
from tkinter import messagebox

# Función que intenta conectarse a PostgreSQL y obtener el PID
def conectar_postgres():
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
        cursor.execute("SELECT pg_backend_pid();")  # Obtener el PID del proceso
        pid = cursor.fetchone()[0]
        cursor.execute("SELECT get_idUsr(%s);", (user,))
        id_user = cursor.fetchone()[0]
        cursor.execute("SELECT insert_sesion(%s,%s);", (id_user, pid))
        conexion.commit()
        conexion.close()

        # Muestra el PID en el campo de texto
        text_pid.config(state=tk.NORMAL)  # Habilitar edición temporalmente
        text_pid.delete(1.0, tk.END)  # Limpia el campo
        text_pid.insert(tk.END, f"PID: {pid}")  # Muestra el PID
        text_pid.config(state=tk.DISABLED)  # Deshabilitar edición nuevamente
        messagebox.showinfo("Éxito", "Conexión exitosa a PostgreSQL.")

        # Si la conexión fue exitosa, abrir la nueva interfaz
        abrir_gestor_archivos()

    except OperationalError as e:
        messagebox.showerror("Error", "Fallo en la conexión: Verifica las credenciales")
        # Limpia el campo de PID si hubo error
        text_pid.config(state=tk.NORMAL)
        text_pid.delete(1.0, tk.END)
        text_pid.config(state=tk.DISABLED)
        print(f"Error: {e}")

# Función para abrir la interfaz de Gestor de Archivos
def abrir_gestor_archivos():
    # Crear una nueva ventana para el gestor de archivos
    root_gestor = tk.Toplevel()
    root_gestor.title("Gestor de Archivos")

    # Crear la barra de menús
    def obtener_funciones():
        # Obtener funciones simuladas desde la base de datos (puedes cambiar esto por la consulta real)
        return [
            {"nombre": "Nuevo Documento de Texto", "categoria": "Crear documentos", "funcion": "crear_documento_texto"},
            {"nombre": "Nuevo Documento Excel", "categoria": "Crear documentos", "funcion": "crear_documento_excel"},
            {"nombre": "Compartir Documento", "categoria": "Compartir archivos", "funcion": "compartir_documento"},
            {"nombre": "Eliminar Documento", "categoria": "Gestión de documentos", "funcion": "eliminar_documento"},
            {"nombre": "Mover Documento", "categoria": "Gestión de documentos", "funcion": "mover_documento"}
        ]

    # Definir las funciones simuladas
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

    # Mapa de funciones
    funciones_mapa = {
        "crear_documento_texto": crear_documento_texto,
        "crear_documento_excel": crear_documento_excel,
        "compartir_documento": compartir_documento,
        "eliminar_documento": eliminar_documento,
        "mover_documento": mover_documento
    }

    # Crear la barra de menús
    menu_bar = tk.Menu(root_gestor)
    funciones_db = obtener_funciones()
    categorias = set([funcion["categoria"] for funcion in funciones_db])
    menus = {}

    for categoria in categorias:
        menus[categoria] = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label=categoria, menu=menus[categoria])

    for funcion in funciones_db:
        categoria_menu = menus[funcion["categoria"]]
        funcion_nombre = funcion["nombre"]
        funcion_codigo = funcion["funcion"]

        if funcion_codigo in funciones_mapa:
            categoria_menu.add_command(label=funcion_nombre, command=funciones_mapa[funcion_codigo])
        else:
            categoria_menu.add_command(label=funcion_nombre, command=lambda: messagebox.showerror("Error", "Función no disponible"))

    # Asignar la barra de menús a la ventana
    root_gestor.config(menu=menu_bar)

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

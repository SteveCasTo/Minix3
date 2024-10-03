import psycopg2
from psycopg2 import OperationalError
import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime
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

        # Obtener el ID de usuario
        cursor.execute("SELECT get_idusr(%s);", (user,))
        id_user = cursor.fetchone()[0]

        # Obtener el PID del proceso
        cursor.execute("SELECT get_pid(%s);",(id_user,))
        pid = cursor.fetchone()[0]

        # Obtener el rol del usuario
        cursor.execute("SELECT get_rol(%s);", (id_user,))
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

    # Agrupar funciones por UI
    uis = set([funcion["ui"] for funcion in funciones_db])
    menus = {}

    # Crear un menú por cada UI
    for ui in uis:
        menus[ui] = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label=ui, menu=menus[ui])

    # Añadir las funciones a su correspondiente UI
    for funcion in funciones_db:
        ui_menu = menus[funcion["ui"]]
        funcion_nombre = funcion["nombre"]
        if funcion_nombre in funciones_mapa:
            ui_menu.add_command(label=funcion_nombre, command=funciones_mapa[funcion_nombre])
        else:
            ui_menu.add_command(label=funcion_nombre, command=lambda: messagebox.showerror("Error", "Función no disponible"))

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
    cursor.execute("SELECT * FROM get_ui_fun(%s);", (rol,))
    funciones_db = cursor.fetchall()
    cursor.close()
    conexion.close()

    # Estructurar el resultado para que incluya tanto la UI como el nombre de la función
    return [{"ui": f[0], "nombre": f[1]} for f in funciones_db]

# Definir funciones simuladas (las puedes reemplazar por las funciones reales)
def crear_documento_texto():
    crear_doc(1,"texto")

def crear_documento_excel():
    crear_doc(2,"excel")

def compartir_documento():
    conexion = psycopg2.connect(
            host="localhost",
            database="Gestor_Archivos",
            user=user,
            password=password
        )
    cursor = conexion.cursor()
    cursor.execute("SELECT get_idusr(%s);", (user,))
    id_user = cursor.fetchone()[0]
    try:
        nom_achv = simpledialog.askstring("Compartir archivo", "Ingresa el nombre del archivo a compartir:")
        if not nom_achv:
            messagebox.showerror("Error", "El nombre del archivo es obligatorio.")
            return
        cursor.execute("SELECT get_achvID(%s);", (nom_achv,))
        id_achv = cursor.fetchone()[0]
        if not id_achv:
            messagebox.showerror("Error", "El archivo no existe.")
            cursor.close()
            conexion.close()
            return

        nom_user_compartir = simpledialog.askstring("Compartir con usuario", "Ingresa el nombre del usuario:")
        if not nom_user_compartir:
            messagebox.showerror("Error", "El nombre del usuario es obligatorio.")
            return
        cursor.execute("SELECT get_idusr(%s);", (nom_user_comp,))
        id_user_comp = cursor.fetchone()[0]
        if not id_user_comp:
            messagebox.showerror("Error", "El usuario no existe.")
            cursor.close()
            conexion.close()
            return

        fecha_exp = simpledialog.askstring("Fecha de expiración", "Ingresa la fecha de expiración (YYYY-MM-DD):")
        try:
            fecha_exp = datetime.strptime(fecha_expiracion, '%Y-%m-%d').date()
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha incorrecto.")
            return
        cursor.execute("SELECT insert_permisoAchv(%s,%s,%s,%s)",(id_achv, id_user, id_user_comp, fecha_exp))
        conexion.commit()
        cursor.close()
        conexion.close()

        messagebox.showinfo("Éxito", "El archivo ha sido compartido exitosamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo compartir el archivo. Error: {e}")

def eliminar_documento():
    conexion = psycopg2.connect(
            host="localhost",
            database="Gestor_Archivos",
            user=user,
            password=password
        )
    cursor = conexion.cursor()
    try:
        nom_achv = simpledialog.askstring("Eliminar archivo", "Ingresa el nombre del archivo a eliminar:")
        if not nom_achv:
            messagebox.showerror("Error", "El nombre del archivo es obligatorio.")
            return

        cursor.execute("SELECT get_achvID(%s);", (nom_achv,))
        id_achv = cursor.fetchone()[0]
        if not id_achv:
            messagebox.showerror("Error", "El archivo no existe.")
            cursor.close()
            conexion.close()
            return
        cursor.execute("SELECT delete_achvID(%s);", (nom_achv,))
        conexion.commit()
        cursor.close()
        conexion.close()

        messagebox.showinfo("Éxito", "El archivo ha sido eliminado exitosamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo eliminar el archivo. Error: {e}")

def mover_documento():
    messagebox.showinfo("Función", "El documento ha sido movido.")

def crear_doc(id_tip, nom_tip):
    conexion = psycopg2.connect(
            host="localhost",
            database="Gestor_Archivos",
            user=user,
            password=password
        )
    cursor = conexion.cursor()
    cursor.execute("SELECT get_idusr(%s);", (user,))
    id_user = cursor.fetchone()[0]
    try:
        nom_achv = simpledialog.askstring("Nombre del archivo", f"Ingresa el nombre del archivo ({nom_tip}):")
        if not nom_achv:
            messagebox.showerror("Error", "El nombre del archivo es obligatorio.")
            return

        ruta_achv = simpledialog.askstring("Ruta del archivo", "Ingresa la ruta donde se guardará el archivo:")
        if not ruta_achv:
            messagebox.showerror("Error", "La ruta del archivo es obligatoria.")
            return

        cursor.execute("SELECT insert_achv(%s,%s,%s,%s)", (id_user, id_tip, nom_achv, ruta_achv))
        conexion.commit()
        cursor.close()
        conexion.close()
        messagebox.showinfo("Éxito", f"Se ha creado un nuevo documento de {nom_tip}.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo crear el documento. Error: {e}")

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

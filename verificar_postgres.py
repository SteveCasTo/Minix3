import psycopg2
from psycopg2 import OperationalError
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
from datetime import datetime
import os
import openpyxl
import pandas as pd
import shutil

user = None
password = None
def conectar_postgres():
    global user
    global password
    user = entry_user.get()
    password = entry_password.get()
    try:
        # Conectar a la base de datos PostgreSQL
        conexion = conectar_base_datos()
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
        "MoverDocumento": mover_documento,
        "CrearCarpeta": crear_carpeta,
        "EliminarCarpeta": eliminar_carpeta
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

def conectar_base_datos():
    global user
    global password
    return psycopg2.connect(
            host="localhost",
            database="Gestor_Archivos",
            user=user,
            password=password
        )

def crear_documento_texto():
    crear_documento(1,".txt")

def crear_documento_excel():
    crear_documento(2,".xlsx")

def crear_carpeta():
    ventana_crear = tk.Toplevel()
    ventana_crear.title("Crear Carpeta")
    ventana_crear.geometry("400x300")

    label_nombre = tk.Label(ventana_crear, text="Nombre de la carpeta:")
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
        nombre_carpeta = entry_nombre.get()
        ruta_carpeta = entry_carpeta.get()
        if not nombre_carpeta:
            messagebox.showerror("Error", "El nombre de la carpeta es obligatorio.")
            return
        if not ruta_carpeta:
            messagebox.showerror("Error", "La ruta de la carpeta es obligatoria.")
            return
        
        ruta_completa = os.path.join(ruta_carpeta, nombre_carpeta)
        try:
            if not os.path.exists(ruta_completa):
                os.makedirs(ruta_completa)
            else:
                messagebox.showwarning("Advertencia", "La carpeta ya existe en el sistema de archivos.")
                return
            
            conexion = conectar_base_datos()
            cursor = conexion.cursor()
            cursor.execute("SELECT get_idusr(%s);", (user,))
            id_user = cursor.fetchone()[0]
            cursor.execute("SELECT insert_carpet(%s,%s,%s);", (id_user, nombre_carpeta, ruta_completa))
            conexion.commit()

            messagebox.showinfo("Éxito", f"Se ha creado la carpeta '{nombre_carpeta}' en la ruta '{ruta_carpeta}'.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear la carpeta. Error: {e}")
        finally:
            cursor.close()
            conexion.close()
            ventana_crear.destroy()
            
    button_confirmar = tk.Button(ventana_crear, text="Crear Carpeta", command=confirmar_crear)
    button_confirmar.pack(pady=10)
    button_cancelar = tk.Button(ventana_crear, text="Cancelar", command=ventana_crear.destroy)
    button_cancelar.pack(pady=5)

def compartir_documento():
    ventana_compartir = tk.Toplevel()
    ventana_compartir.title("Compartir Documento")
    ventana_compartir.geometry("400x300")

    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    
    cursor.execute("SELECT get_idusr(%s);", (user,))
    id_user = cursor.fetchone()[0]
    
    cursor.execute("SELECT listar_usrs(%s);", (id_user,))
    lista_usuarios = [fila[0] for fila in cursor.fetchall()]
    cursor.execute("SELECT achv_user(%s);",(id_user,))
    lista_documentos = [fila[0] for fila in cursor.fetchall()]
    cursor.close()
    conexion.close()

    if not lista_usuarios or not lista_documentos:
        messagebox.showerror("Error", "No hay usuarios disponibles para compartir.")
        ventana_compartir.destroy()
        return
    
    if not lista_documentos:
        messagebox.showerror("Error", "No hay documentos disponibles para compartir.")
        ventana_compartir.destroy()
        return

    label_documento = tk.Label(ventana_compartir, text="Selecciona el archivo a compartir:")
    label_documento.pack(pady=5)
    variable_documento = tk.StringVar(ventana_compartir)
    variable_documento.set(lista_documentos[0])
    menu_documento = tk.OptionMenu(ventana_compartir, variable_documento, *lista_documentos)
    menu_documento.pack(pady=5)

    label_usuario = tk.Label(ventana_compartir, text="Selecciona el usuario:")
    label_usuario.pack(pady=5)
    variable_usuario = tk.StringVar(ventana_compartir)
    variable_usuario.set(lista_usuarios[0])
    menu_usuario = tk.OptionMenu(ventana_compartir, variable_usuario, *lista_usuarios)
    menu_usuario.pack(pady=5)

    label_fecha = tk.Label(ventana_compartir, text="Fecha de expiración (YYYY-MM-DD):")
    label_fecha.pack(pady=5)
    entry_fecha = tk.Entry(ventana_compartir)
    entry_fecha.pack(pady=5)
    
    def confirmar_compartir():
        nom_achv = variable_documento.get()
        nom_user_comp = variable_usuario.get()
        fecha_exp = entry_fecha.get()
        try: fecha_exp = datetime.strptime(fecha_exp, '%Y-%m-%d').date()
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha incorrecto.")
            return
        conexion = conectar_base_datos()
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT get_achvID(%s);", (nom_achv,))
            id_achv = cursor.fetchone()[0]
            cursor.execute("SELECT get_idusr(%s);", (nom_user_comp,))
            id_user_comp = cursor.fetchone()[0]

            cursor.execute("SELECT insert_permisoAchv(%s,%s,%s,%s)", (id_achv, id_user, id_user_comp, fecha_exp))
            conexion.commit()
            messagebox.showinfo("Éxito", "El archivo ha sido compartido exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo compartir el archivo. Error: {e}")
        finally:
            cursor.close()
            conexion.close()
            ventana_compartir.destroy()

    button_confirmar = tk.Button(ventana_compartir, text="Compartir", command=confirmar_compartir)
    button_confirmar.pack(pady=10)
    button_cancelar = tk.Button(ventana_compartir, text="Cancelar", command=ventana_compartir.destroy)
    button_cancelar.pack(pady=5)

def eliminar_carpeta():
    ventana_eliminar = tk.Toplevel()
    ventana_eliminar.title("Eliminar Carpeta")
    ventana_eliminar.geometry("400x300")
    
    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    cursor.execute("SELECT get_idusr(%s);", (user,))
    id_user = cursor.fetchone()[0]
    cursor.execute("SELECT cpt_user(%s);", (id_user,))
    carpetas_propias = [("Carpeta: " + fila[0]) for fila in cursor.fetchall()]

    cursor.close()
    conexion.close()

    if not carpetas_propias:
        messagebox.showerror("Error", "No hay carpetas disponibles para eliminar.")
        ventana_eliminar.destroy()
        return

    label_carpeta = tk.Label(ventana_eliminar, text="Selecciona la carpeta a eliminar:")
    label_carpeta.pack(pady=5)
    variable_carpeta = tk.StringVar(ventana_eliminar)
    variable_carpeta.set(carpetas_propias[0])
    menu_carpeta = tk.OptionMenu(ventana_eliminar, variable_carpeta, *carpetas_propias)
    menu_carpeta.pack(pady=5)

    def confirmar_eliminar():
        nom_carpeta = variable_carpeta.get()
        nom_carpeta = nom_carpeta.split(": ", 1)[1]
        try:
            conexion = conectar_base_datos()
            cursor = conexion.cursor()
            cursor.execute("SELECT Druta_cpts(%s,%s);", (nom_carpeta, id_user))
            ruta_carpeta = cursor.fetchone()[0]
            cursor.execute("SELECT achv_Fromcpt(%s);", (ruta_carpeta+'%',))
            archivos_en_carpeta = cursor.fetchall()

            # Eliminar archivos de la carpeta en el sistema y en la base de datos
            for archivo in archivos_en_carpeta:
                ruta_archivo = archivo[0]
                # Eliminar el archivo del sistema de archivos
                if os.path.exists(ruta_archivo):
                    os.remove(ruta_archivo)
                # Eliminar el archivo de la base de datos
                cursor.execute("SELECT delete_achvR(%s);", (ruta_archivo,))
            # Eliminar la carpeta del sistema de archivos
            if os.path.exists(ruta_carpeta):
                shutil.rmtree(ruta_carpeta)

            # Eliminar la carpeta de la base de datos
            cursor.execute("SELECT delete_cpt(%s,%s);", (nom_carpeta, id_user))
            conexion.commit()

            messagebox.showinfo("Éxito", f"La carpeta '{nom_carpeta}' y todos sus archivos han sido eliminados correctamente.")
        
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar la carpeta. Error: {e}")
        finally:
            cursor.close()
            conexion.close()
            ventana_eliminar.destroy()

    button_confirmar = tk.Button(ventana_eliminar, text="Eliminar", command=confirmar_eliminar)
    button_confirmar.pack(pady=10)
    button_cancelar = tk.Button(ventana_eliminar, text="Cancelar", command=ventana_eliminar.destroy)
    button_cancelar.pack(pady=5)

def eliminar_documento():
    ventana_eliminar = tk.Toplevel()
    ventana_eliminar.title("Eliminar Documento")
    ventana_eliminar.geometry("400x300")
    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    
    cursor.execute("SELECT get_idusr(%s);", (user,))
    id_user = cursor.fetchone()[0]

    cursor.execute("SELECT achv_user(%s)",(id_user,))
    archivos_propios = [("Propio: " + fila[0]) for fila in cursor.fetchall()]

    cursor.execute("SELECT achv_user_comp(%s)",(id_user,))
    archivos_compartidos = [("Compartido: " + fila[0]) for fila in cursor.fetchall()]

    lista_documentos = archivos_propios + archivos_compartidos

    cursor.close()
    conexion.close()

    if not lista_documentos:
        messagebox.showerror("Error", "No hay documentos disponibles para eliminar.")
        ventana_eliminar.destroy()
        return

    label_documento = tk.Label(ventana_eliminar, text="Selecciona el archivo a eliminar:")
    label_documento.pack(pady=5)
    variable_documento = tk.StringVar(ventana_eliminar)
    variable_documento.set(lista_documentos[0])  # Establecer valor inicial
    menu_documento = tk.OptionMenu(ventana_eliminar, variable_documento, *lista_documentos)
    menu_documento.pack(pady=5)

    def confirmar_eliminar():
        nom_achv = variable_documento.get()

        # Extraer solo el nombre del archivo (quitando el prefijo "Propio:" o "Compartido:")
        nom_achv = nom_achv.split(": ", 1)[1]
        try:
            conexion = conectar_base_datos()
            cursor = conexion.cursor()
            cursor.execute("SELECT delete_achvID(%s);", (nom_achv,))
            conexion.commit()
            messagebox.showinfo("Éxito", "El archivo ha sido eliminado exitosamente.")
        except Exception as e: messagebox.showerror("Error", f"No se pudo eliminar el archivo. Error: {e}")
        finally:
            cursor.close()
            conexion.close()
            ventana_eliminar.destroy()

    button_confirmar = tk.Button(ventana_eliminar, text="Eliminar", command=confirmar_eliminar)
    button_confirmar.pack(pady=10)
    button_cancelar = tk.Button(ventana_eliminar, text="Cancelar", command=ventana_eliminar.destroy)
    button_cancelar.pack(pady=5)

def mover_documento():
    messagebox.showinfo("Función", "El documento ha sido movido.")

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
        try:
            conexion = conectar_base_datos()
            cursor = conexion.cursor()
            cursor.execute("SELECT get_idusr(%s);", (user,))
            id_user = cursor.fetchone()[0]
            cursor.execute("SELECT id_carpet_forRuta(%s)", (ruta_carpeta,))
            resultado = cursor.fetchone()
            if resultado:
                id_carpeta = resultado[0]
            else:
                cursor.execute("SELECT insert_carpet(%s,%s,%s)", (id_user, nombre_carpeta, ruta_carpeta))
                conexion.commit()
            if(id_tip == 1):
                with open(ruta_archivo, 'w') as archivo:
                    archivo.write('')
                with open(ruta_archivo, 'rb') as file:
                    contenido_binario = file.read()
            elif id_tip == 2:
                workbook = openpyxl.Workbook()
                workbook.save(ruta_archivo)
                with open(ruta_archivo, 'rb') as archivo:
                    tamanio = 2000
                    contenido_binario = archivo.read(tamanio)
            cursor.execute("SELECT insert_achv_withCont(%s,%s,%s,%s,%s);", (id_user, id_tip, nombre_archivo, ruta_archivo, psycopg2.Binary(contenido_binario)))
            conexion.commit()
            messagebox.showinfo("Éxito", f"Se ha creado el archivo '{nombre_archivo}' en la carpeta '{ruta_carpeta}'.")
        except Exception as e: messagebox.showerror("Error", f"No se pudo crear el archivo. Error: {e}")
        finally:
            cursor.close()
            conexion.close()
            ventana_crear.destroy()

    button_confirmar = tk.Button(ventana_crear, text="Crear Archivo", command=confirmar_crear)
    button_confirmar.pack(pady=10)
    button_cancelar = tk.Button(ventana_crear, text="Cancelar", command=ventana_crear.destroy)
    button_cancelar.pack(pady=5)

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

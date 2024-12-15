import neo4j
from neo4j import GraphDatabase
import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import messagebox, filedialog
from datetime import datetime
import os
from funs import *

# Conexión a Neo4j
class Neo4jConnection:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def run_query(self, query, parameters=None):
        try:
            with self.driver.session() as session:
                result = session.run(query, parameters)
                return [record for record in result]
        except Exception as e:
            print(f"Error ejecutando la consulta: {e}")
            return []

# Inicializar conexión
neo4j_conn = Neo4jConnection(uri="bolt://localhost:7689", user="neo4j", password="486579123")

user = None

def crear_botones_desplegables(ventana, datos_ui_funciones, funciones_mapa):
    for ui_dato in datos_ui_funciones:
        nombre_ui = ui_dato["ui"]
        funciones = ui_dato["funciones"]

        # Crear marco para cada UI
        frame_ui = ttk.LabelFrame(ventana, text=nombre_ui)
        frame_ui.pack(pady=10, fill="x")

        for funcion in funciones:
            if funcion in funciones_mapa:
                boton = ttk.Button(frame_ui, text=funcion, command=funciones_mapa[funcion])
            else:
                boton = ttk.Button(frame_ui, text=funcion, command=lambda: messagebox.showerror("Error", "Función no disponible"))
            boton.pack(side="top", fill="x", padx=5, pady=5)


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
        try:
            # Obtener el ID del usuario actual
            id_user = obtener_id_usuario(neo4j_conn, user)
            id_doc = obtener_id_documento(nombre_archivo)
            # Obtener o crear la carpeta en la base de datos
            id_carpeta = obtener_id_carpeta(neo4j_conn, ruta_carpeta, nombre_carpeta, id_user, datetime.now(), id_doc)
            
            # Insertar el archivo en la base de datos
            insertar_archivo(neo4j_conn, id_user, id_tip, nombre_archivo, ruta_archivo, datetime.now(), contenido_binario, user)
            
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
    id_user = obtener_id_usuario(neo4j_db, user)
    if not id_user:
        messagebox.showerror("Error", "Usuario no encontrado.")
        ventana_compartir.destroy()
        return
    lista_usuarios = listar_usuarios(neo4j_db, id_user)
    lista_documentos = listar_documentos_usuario(neo4j_db, id_user)
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
            id_achv = obtener_id_documento(neo4j_db, nom_achv)
            id_user_comp = obtener_id_usuario(neo4j_db, nom_user_comp)
            
            if not id_achv or not id_user_comp:
                messagebox.showerror("Error", "No se pudo encontrar el archivo o el usuario especificado.")
                return
            
            compartir_archivo(neo4j_db, id_achv, id_user, id_user_comp, datetime.now(), fecha_exp)
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
    ventana_eliminar = tk.Toplevel()
    ventana_eliminar.title("Eliminar Documento")
    ventana_eliminar.geometry("400x300")

    try:
        # Obtener el ID del usuario actual
        id_user = obtener_id_usuario(neo4j_conn, user)
        # Listar archivos propios
        archivos_propios = listar_archivos_usuario(neo4j_conn, id_user)
        lista_archivos_propios = [f"Propio: {archivo.nombre_archivo}" for archivo in archivos_propios]
        # Listar archivos compartidos
        archivos_compartidos = listar_archivos_compartidos(neo4j_conn, id_user)
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
        
        try:
            # Eliminar el archivo de la base de datos
            eliminar_archivo_por_nombre(neo4j_conn, nom_achv)
            messagebox.showinfo("Éxito", f"El archivo '{nom_achv}' ha sido eliminado exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar el archivo. Error: {e}")
        finally:
            ventana_eliminar.destroy()

    button_confirmar = tk.Button(ventana_eliminar, text="Eliminar", command=confirmar_eliminar)
    button_confirmar.pack(pady=10)
    button_cancelar = tk.Button(ventana_eliminar, text="Cancelar", command=ventana_eliminar.destroy)
    button_cancelar.pack(pady=5)

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

def abrir_gestor_archivos(rol_usuario):
    root_gestor = tk.Toplevel()
    root_gestor.title("Gestor de Archivos")
    root_gestor.geometry("400x400")
    
    try:
        # Obtener UI y funciones desde Neo4j
        datos_ui_funciones = obtener_ui_con_funciones(neo4j_conn)

        # Crear botones desplegables
        crear_botones_desplegables(root_gestor, datos_ui_funciones, funciones_mapa)

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar la información. Error: {e}")
        root_gestor.destroy()
        
def autenticar():
    global user
    user = entry_user.get()
    contrasena = entry_password.get()

    if autenticar_usuario(neo4j_conn, user, contrasena):
        messagebox.showinfo("Éxito", f"Bienvenido {user}")
        root.withdraw()
        user_id = obtener_id_usuario(neo4j_conn, user)
        # TODO: Obtener rol del usuario desde Neo4j
        rol_usuario = "Admin"  # Simulado
        abrir_gestor_archivos(rol_usuario)
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

root = tk.Tk()
root.title("Inicio de Sesión")
root.geometry("300x200")

label_user = tk.Label(root, text="Usuario:")
label_user.pack()
entry_user = tk.Entry(root, width=20)
entry_user.pack()

label_password = tk.Label(root, text="Contraseña:")
label_password.pack()
entry_password = tk.Entry(root, show="*", width=20)
entry_password.pack()

button_login = tk.Button(root, text="Iniciar Sesión", command=autenticar)
button_login.pack(pady=10)

button_exit = tk.Button(root, text="Salir", command=root.quit)
button_exit.pack()

root.mainloop()

neo4j_conn.close()

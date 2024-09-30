import tkinter as tk
from tkinter import simpledialog, messagebox
import psycopg2
from psycopg2 import OperationalError
from datetime import datetime

# Crear documento de texto (id_tipo = 1)
def crear_documento_texto():
    crear_documento(1, "texto")

# Crear documento de Excel (id_tipo = 2)
def crear_documento_excel():
    crear_documento(2, "Excel")

# Función común para crear documento
def crear_documento(id_tipo, tipo_documento):
    try:
        # Obtener datos del usuario
        id_usuario = obtener_id_usuario()

        # Solicitar el nombre del archivo
        nombre_archivo = simpledialog.askstring("Nombre del archivo", f"Ingresa el nombre del archivo ({tipo_documento}):")
        if not nombre_archivo:
            messagebox.showerror("Error", "El nombre del archivo es obligatorio.")
            return

        # Solicitar la ruta del archivo
        ruta_archivo = simpledialog.askstring("Ruta del archivo", "Ingresa la ruta donde se guardará el archivo:")
        if not ruta_archivo:
            messagebox.showerror("Error", "La ruta del archivo es obligatoria.")
            return

        # Obtener la fecha de creación
        creacion_archivo = datetime.now().date()

        # Insertar el documento en la base de datos
        conexion = conectar_base_datos()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Archivo (id_usuario, id_tipo, nombre_archivo, ruta_archivo, creacion_archivo)
            VALUES (%s, %s, %s, %s, %s)
        """, (id_usuario, id_tipo, nombre_archivo, ruta_archivo, creacion_archivo))
        conexion.commit()
        cursor.close()
        conexion.close()

        messagebox.showinfo("Éxito", f"Se ha creado un nuevo documento de {tipo_documento}.")
    
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo crear el documento. Error: {e}")

# Función para obtener el ID de usuario (simulada)
def obtener_id_usuario():
    # Aquí deberías implementar la lógica real para obtener el ID de usuario
    # Por ejemplo, puedes almacenarlo al iniciar sesión
    return 1  # Supongamos que el usuario con ID 1 está conectado

# Función para conectar con la base de datos
def conectar_base_datos():
    return psycopg2.connect(
        host="localhost",
        database="Gestor_Archivos",
        user="tu_usuario",  # Reemplazar con el usuario real
        password="tu_contraseña"  # Reemplazar con la contraseña real
    )
def eliminar_documento():
    try:
        # Solicitar el nombre del archivo a eliminar
        nombre_archivo = simpledialog.askstring("Eliminar archivo", "Ingresa el nombre del archivo a eliminar:")
        if not nombre_archivo:
            messagebox.showerror("Error", "El nombre del archivo es obligatorio.")
            return

        # Verificar si el archivo existe
        conexion = conectar_base_datos()
        cursor = conexion.cursor()
        cursor.execute("SELECT id_archivo FROM Archivo WHERE nombre_archivo = %s;", (nombre_archivo,))
        archivo = cursor.fetchone()

        if not archivo:
            messagebox.showerror("Error", "El archivo no existe.")
            cursor.close()
            conexion.close()
            return

        # Eliminar el archivo
        cursor.execute("DELETE FROM Archivo WHERE nombre_archivo = %s;", (nombre_archivo,))
        conexion.commit()
        cursor.close()
        conexion.close()

        messagebox.showinfo("Éxito", "El archivo ha sido eliminado exitosamente.")
    
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo eliminar el archivo. Error: {e}")
def compartir_documento():
    try:
        # Solicitar el nombre del archivo a compartir
        nombre_archivo = simpledialog.askstring("Compartir archivo", "Ingresa el nombre del archivo a compartir:")
        if not nombre_archivo:
            messagebox.showerror("Error", "El nombre del archivo es obligatorio.")
            return

        # Verificar si el archivo existe
        conexion = conectar_base_datos()
        cursor = conexion.cursor()
        cursor.execute("SELECT id_archivo FROM Archivo WHERE nombre_archivo = %s;", (nombre_archivo,))
        archivo = cursor.fetchone()

        if not archivo:
            messagebox.showerror("Error", "El archivo no existe.")
            cursor.close()
            conexion.close()
            return

        id_archivo = archivo[0]

        # Solicitar el nombre del usuario con quien se compartirá
        nombre_usuario_compartir = simpledialog.askstring("Compartir con usuario", "Ingresa el nombre del usuario:")
        if not nombre_usuario_compartir:
            messagebox.showerror("Error", "El nombre del usuario es obligatorio.")
            return

        # Obtener el id del usuario con quien se compartirá
        cursor.execute("SELECT id_usuario FROM Usuario WHERE nombre_usuario = %s;", (nombre_usuario_compartir,))
        usuario_compartir = cursor.fetchone()

        if not usuario_compartir:
            messagebox.showerror("Error", "El usuario no existe.")
            cursor.close()
            conexion.close()
            return

        id_usuario_compartir = usuario_compartir[0]

        # Solicitar la fecha de expiración del permiso
        fecha_expiracion = simpledialog.askstring("Fecha de expiración", "Ingresa la fecha de expiración (YYYY-MM-DD):")
        try:
            fecha_expiracion = datetime.strptime(fecha_expiracion, '%Y-%m-%d').date()
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha incorrecto.")
            return

        # Insertar el permiso en la base de datos
        cursor.execute("""
            INSERT INTO Permiso_Archivo (id_archivo, id_usuario_compartido, expiration)
            VALUES (%s, %s, %s)
        """, (id_archivo, id_usuario_compartir, fecha_expiracion))
        conexion.commit()
        cursor.close()
        conexion.close()

        messagebox.showinfo("Éxito", "El archivo ha sido compartido exitosamente.")
    
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo compartir el archivo. Error: {e}")

import psycopg2
from psycopg2 import OperationalError
import tkinter as tk
from tkinter import messagebox

def conectar_postgres(user, password):
    try:
        # Intentar conectar a la base de datos "postgres" usando las credenciales del usuario
        conexion = psycopg2.connect(
            host="localhost",
            database="postgres",  # Base de datos por defecto
            user=user,
            password=password
        )
        messagebox.showinfo("Éxito", "Conexión exitosa a PostgreSQL")
        conexion.close()  # Cerrar conexión si es exitosa
    except OperationalError as e:
        messagebox.showerror("Error", "Fallo en la conexión: Verifica las credenciales")
        print(f"Error: {e}")

def validar_conexion():
    # Obtener los valores de usuario y contraseña de la interfaz
    user = usuario_entry.get()
    password = contrasena_entry.get()
    conectar_postgres(user, password)

def cerrar_ventana():
    ventana.quit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conectar a PostgreSQL")

# Etiquetas y campos de entrada para el usuario y contraseña
tk.Label(ventana, text="Usuario:").grid(row=0, column=0, padx=10, pady=10)
usuario_entry = tk.Entry(ventana)
usuario_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10)
contrasena_entry = tk.Entry(ventana, show="*")  # Ocultar la contraseña con '*'
contrasena_entry.grid(row=1, column=1, padx=10, pady=10)

# Botón para aceptar y validar la conexión
aceptar_btn = tk.Button(ventana, text="Aceptar", command=validar_conexion)
aceptar_btn.grid(row=2, column=0, padx=10, pady=10)

# Botón para cancelar y cerrar la ventana
cancelar_btn = tk.Button(ventana, text="Cancelar", command=cerrar_ventana)
cancelar_btn.grid(row=2, column=1, padx=10, pady=10)

# Iniciar el loop de la interfaz gráfica
ventana.mainloop()
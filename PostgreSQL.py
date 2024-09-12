import psycopg2
from psycopg2 import OperationalError
import tkinter as tk
from tkinter import messagebox

# Función que intenta conectarse a PostgreSQL y obtener el PID
def conectar_postgres():
    user = entry_user.get()  # Obtiene el usuario ingresado
    password = entry_password.get()  # Obtiene la contraseña ingresada
    
    try:
        # Conexión a la base de datos PostgreSQL
        conexion = psycopg2.connect(
            host="localhost",
            database="postgres",  # Base de datos por defecto
            user=user,
            password=password
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT pg_backend_pid();")  # Obtiene el PID del proceso actual
        pid = cursor.fetchone()[0]
        conexion.close()  # Cierra la conexión
        # Muestra el PID en el campo de texto
        text_pid.config(state=tk.NORMAL)  # Habilitar edición temporalmente
        text_pid.delete(1.0, tk.END)  # Limpia el campo
        text_pid.insert(tk.END, f"PID: {pid}")  # Muestra el PID
        text_pid.config(state=tk.DISABLED)  # Deshabilitar edición nuevamente
        messagebox.showinfo("Éxito", "Conexión exitosa a PostgreSQL.")
        
    except OperationalError as e:
        messagebox.showerror("Error", "Fallo en la conexión: Verifica las credenciales")
        # Limpia el campo de PID si hubo error
        text_pid.config(state=tk.NORMAL)
        text_pid.delete(1.0, tk.END)
        text_pid.config(state=tk.DISABLED)
        print(f"Error: {e}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Conexión a PostgreSQL")

# Etiqueta y campo de entrada para el usuario
label_user = tk.Label(root, text="Usuario:")
label_user.pack()
entry_user = tk.Entry(root)
entry_user.pack()

# Etiqueta y campo de entrada para la contraseña
label_password = tk.Label(root, text="Contraseña:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Botón para conectar
button_connect = tk.Button(root, text="Conectar", command=conectar_postgres)
button_connect.pack()

# Campo para mostrar el PID
label_pid = tk.Label(root, text="PID de la conexión:")
label_pid.pack()

text_pid = tk.Text(root, height=1, width=30)
text_pid.pack()
text_pid.config(state=tk.DISABLED)  # Deshabilita la edición del campo PID

# Botón para salir
button_exit = tk.Button(root, text="Cancelar", command=root.quit)
button_exit.pack()

# Ejecutar la interfaz
root.mainloop()
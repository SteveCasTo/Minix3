import psycopg2
from psycopg2 import OperationalError

def conectar_postgres(host, dbname, user, password):
    try:
        # Intentar conectar con las credenciales proporcionadas
        conexion = psycopg2.connect(
            host=host,
            database=dbname,
            user=user,
            password=password
        )
        print("Conexión exitosa a la base de datos PostgreSQL")
        conexion.close()  # Cerrar conexión si es exitosa
    except OperationalError as e:
        print("Fallo en la conexión: Verifica las credenciales")
        print(f"Error: {e}")

if __name__ == "__main__":
    # Pedir al usuario las credenciales
    host = input("Ingresa el host (default: localhost): ") or "localhost"
    dbname = input("Ingresa el nombre de la base de datos: ")
    user = input("Ingresa el nombre de usuario: ")
    password = input("Ingresa la contraseña: ")

    # Verificar la conexión
    conectar_postgres(host, dbname, user, password)

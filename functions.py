from neo4j import GraphDatabase
from datetime import datetime

class Neo4jDatabase:
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

neo4j_db = Neo4jDatabase("bolt://localhost:7687", "neo4j", "987654321")

def insertar_user(neo4j_db, nombre, contrasena, active=True):
    query = """
    CREATE (u:Usuario {nombre_usuario: $nombre, contrasena: $contrasena, active: $active})
    """
    neo4j_db.run_query(query, {"nombre": nombre, "contrasena": contrasena, "active": active})

def insertar_roles(neo4j_db, id_rol, nombre_rol):
    query = """
    CREATE (r:Rol {id_rol: $id_rol, nombre_rol: $nombre_rol})
    """
    neo4j_db.run_query(query, {"id_rol": id_rol, "nombre_rol": nombre_rol})

def insertar_ui(neo4j_db, id_ui, url):
    query = """
    CREATE (ui:UI {id_ui: $id_ui, url: $url})
    """
    neo4j_db.run_query(query, {"id_ui": id_ui, "url": url})

def insertar_funciones(neo4j_db, id_funcion, nombre_funcion):
    query = """
    CREATE (f:Funcion {id_funcion: $id_funcion, nombre_funcion: $nombre_funcion})
    """
    neo4j_db.run_query(query, {"id_funcion": id_funcion, "nombre_funcion": nombre_funcion})

def autenticar_usuario(neo4j_db, nombre_usuario, contrasena):
    query = """
    MATCH (u:Usuario {nombre_usuario: $nombre_usuario, contrasena: $contrasena})
    RETURN u
    """
    result = neo4j_db.run_query(query, {"nombre_usuario": nombre_usuario, "contrasena": contrasena})
    return result[0]["u"] if result else None

def obtener_roles_usuario(neo4j_db, id_usuario):
    query = """
    MATCH (u:Usuario)-[:TIENE_ROL]->(r:Rol)
    WHERE ID(u) = $id_usuario
    RETURN r.nombre_rol AS rol
    """
    result = neo4j_db.run_query(query, {"id_usuario": id_usuario})
    return [record["rol"] for record in result]

def obtener_rol_id(neo4j_db, nombre_rol):
    query = """
    MATCH (r:Rol {nombre_rol: $nombre_rol})
    RETURN ID(r) AS id_rol
    """
    result = neo4j_db.run_query(query, {"nombre_rol": nombre_rol})
    return result[0]["id_rol"] if result else None

def obtener_funciones_rol(neo4j_db, id_rol):
    query = """
    MATCH (r:Rol)-[:TIENE_FUNCION]->(f:Funcion)
    WHERE ID(r) = $id_rol
    RETURN f.nombre_funcion AS funcion
    """
    result = neo4j_db.run_query(query, {"id_rol": id_rol})
    return [record["funcion"] for record in result]

def obtener_id_usuario(neo4j_db, nombre_usuario):
    query = """
    MATCH (u:Usuario {nombre_usuario: $nombre_usuario})
    RETURN ID(u) AS id_usuario
    """
    result = neo4j_db.run_query(query, {"nombre_usuario": nombre_usuario})
    return result[0]["id_usuario"] if result else None

def listar_usuarios(neo4j_db, id_usuario_actual):
    query = """
    MATCH (u:Usuario)
    WHERE ID(u) <> $id_usuario_actual
    RETURN u
    """
    result = neo4j_db.run_query(query, {"id_usuario_actual": id_usuario_actual})
    return [record["u"] for record in result]

def listar_documentos_usuario(neo4j_db, id_usuario):
    query = """
    MATCH (u:Usuario)-[:POSEE]->(a:Archivo)
    WHERE ID(u) = $id_usuario
    RETURN a
    """
    result = neo4j_db.run_query(query, {"id_usuario": id_usuario})
    return [record["a"] for record in result]

def obtener_id_documento(neo4j_db, nombre_documento):
    query = """
    MATCH (a:Archivo {nombre_archivo: $nombre_documento})
    RETURN ID(a) AS id_archivo
    """
    result = neo4j_db.run_query(query, {"nombre_documento": nombre_documento})
    return result[0]["id_archivo"] if result else None

def compartir_archivo(neo4j_db, id_documento, id_usuario, id_usuario_destino, fecha_inicio, fecha_expiracion):
    query = """
    MATCH (a:Archivo), (u:Usuario), (ud:Usuario)
    WHERE ID(a) = $id_documento AND ID(u) = $id_usuario AND ID(ud) = $id_usuario_destino
    CREATE (u)-[:COMPARTIO {fecha_permiso: $fecha_inicio, expiration: $fecha_expiracion}]->(a)
    CREATE (ud)-[:RECIBIO]->(a)
    """
    neo4j_db.run_query(query, {
        "id_documento": id_documento,
        "id_usuario": id_usuario,
        "id_usuario_destino": id_usuario_destino,
        "fecha_inicio": fecha_inicio,
        "fecha_expiracion": fecha_expiracion
    })

def insertar_archivo(neo4j_db, id_usuario, id_tipo, nombre_archivo, ruta_archivo, creacion_archivo, contenido_binario, usuario):
    datos_nuevos = {
        "id_tipo": id_tipo,
        "nombre_archivo": nombre_archivo,
        "ruta_archivo": ruta_archivo,
        "creacion_archivo": creacion_archivo,
        "contenido_archivo": contenido_binario
    }

    query = """
    MATCH (u:Usuario)
    WHERE ID(u) = $id_usuario
    CREATE (a:Archivo {
        id_tipo: $id_tipo, nombre_archivo: $nombre_archivo, 
        ruta_archivo: $ruta_archivo, creacion_archivo: $creacion_archivo, 
        contenido_archivo: $contenido_binario
    })
    CREATE (u)-[:POSEE]->(a)
    """
    
    neo4j_db.run_query(query, {
        "id_usuario": id_usuario,
        "id_tipo": id_tipo,
        "nombre_archivo": nombre_archivo,
        "ruta_archivo": ruta_archivo,
        "creacion_archivo": creacion_archivo,
        "contenido_binario": contenido_binario
    })
    
    registrar_log(neo4j_db, "INSERT", "Archivo", datos_nuevos=datos_nuevos, usuario=usuario)
    
def obtener_ui_con_funciones(neo4j_conn):
    query = """
    MATCH (ui:UI)-[:TIENE_FUNCION]->(funcion:Funcion)
    RETURN ui.nombre_ui AS nombre_ui, collect(funcion.nombre_funcion) AS funciones
    """
    result = neo4j_conn.query(query)
    return [{"ui": record["nombre_ui"], "funciones": record["funciones"]} for record in result]

    
def obtener_id_carpeta(neo4j_db, ruta_carpeta, nombre_carpeta, id_usuario, creacion_carpeta):
    query_buscar = """
    MATCH (c:Carpeta {ruta_carpeta: $ruta_carpeta})
    RETURN ID(c) AS id_carpeta
    """
    result = neo4j_db.run_query(query_buscar, ruta_carpeta=ruta_carpeta).evaluate()

    if result:
        return result  # Retorna el id_carpeta si ya existe
    
    query_crear = """
    MATCH (u:Usuario {id_usuario: $id_usuario})
    CREATE (c:Carpeta {
        ruta_carpeta: $ruta_carpeta,
        nombre_carpeta: $nombre_carpeta,
        creacion_carpeta: $creacion_carpeta
    })
    CREATE (u)-[:POSEE]->(c)
    RETURN ID(c) AS id_carpeta
    """
    result = neo4j_db.run_query(
        query_crear,
        id_usuario=id_usuario,
        ruta_carpeta=ruta_carpeta,
        nombre_carpeta=nombre_carpeta,
        creacion_carpeta=creacion_carpeta
    ).evaluate()

    return result

def listar_archivos_usuario(neo4j_db, id_usuario):
    query = """
    MATCH (u:Usuario {id_usuario: $id_usuario})-[:POSEE]->(a:Archivo)
    RETURN a {
        id_archivo: a.id_archivo,
        nombre_archivo: a.nombre_archivo,
        ruta_archivo: a.ruta_archivo,
        creacion_archivo: a.creacion_archivo
    } AS archivo
    """
    result = neo4j_db.run_query(query, id_usuario=id_usuario)
    return [record["archivo"] for record in result]

def listar_archivos_compartidos(neo4j_db, id_usuario):
    query = """
    MATCH (a:Archivo)-[:COMPARTIO]->(u:Usuario {id_usuario: $id_usuario})
    RETURN a {
        id_archivo: a.id_archivo,
        nombre_archivo: a.nombre_archivo,
        ruta_archivo: a.ruta_archivo,
        creacion_archivo: a.creacion_archivo
    } AS archivo
    """
    result = neo4j_db.run_query(query, id_usuario=id_usuario)
    return [record["archivo"] for record in result]

def eliminar_archivo_por_nombre(neo4j_db, id_usuario, nombre_archivo):
    query_obtener = """
    MATCH (u:Usuario {id_usuario: $id_usuario})-[:POSEE]->(a:Archivo {nombre_archivo: $nombre_archivo})
    RETURN a {
        id_archivo: a.id_archivo,
        nombre_archivo: a.nombre_archivo,
        ruta_archivo: a.ruta_archivo,
        creacion_archivo: a.creacion_archivo
    } AS archivo
    """
    archivo_a_eliminar = neo4j_db.run_query(query_obtener, id_usuario=id_usuario, nombre_archivo=nombre_archivo)
    datos_viejos = archivo_a_eliminar[0]["archivo"] if archivo_a_eliminar else None

    if not datos_viejos:
        print("No se encontró el archivo para eliminar.")
        return

    query_eliminar = """
    MATCH (u:Usuario {id_usuario: $id_usuario})-[:POSEE]->(a:Archivo {nombre_archivo: $nombre_archivo})
    DETACH DELETE a
    """
    neo4j_db.run_query(query_eliminar, id_usuario=id_usuario, nombre_archivo=nombre_archivo)

    registrar_log(neo4j_db=neo4j_db,operation="DELETE",tabla="Archivo",datos_nuevos=None,datos_viejos=datos_viejos)

def registrar_log(neo4j_db, operation, tabla, datos_nuevos=None, datos_viejos=None, usuario=None):
    fecha = datetime.now().isoformat()
    query = """
    CREATE (log:Log {
        fecha_log: $fecha, operation: $operation, tabla: $tabla, 
        dato_nuevo: $datos_nuevos, dato_viejo: $datos_viejos, usuario: $usuario
    })
    """
    neo4j_db.run_query(query, {
        "fecha": fecha,
        "operation": operation,
        "tabla": tabla,
        "datos_nuevos": datos_nuevos,
        "datos_viejos": datos_viejos,
        "usuario": usuario
    })

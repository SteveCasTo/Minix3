from sqlalchemy import event
import psycopg2
import json
import base64
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from models import *
from models import session as ses
from datetime import date, datetime

user=None

def insertar_user(session, nombre, contrasena, active=True):
    nuevo_user = Usuario(nombre_usuario=nombre,contrasena=contrasena, active=True)
    session.add(nuevo_user)
    session.commit()

def insertar_roles(session, id_rol: int, nombre_rol: str):
    nuevo_rol = Rol(id_rol=id_rol, nombre_rol=nombre_rol)
    session.add(nuevo_rol)
    session.commit()

def insertar_ui(session, id_ui: int, url: str):
    nueva_ui = UI(id_ui=id_ui, url=url)
    session.add(nueva_ui)
    session.commit()

def insertar_funciones(session, id_funcion: int, nombre_funcion: str):
    nueva_funcion = Funcion(id_funcion=id_funcion, nombre_funcion=nombre_funcion)
    session.add(nueva_funcion)
    session.commit()

def autenticar_usuario(session, nombre_usuario, contrasena):
    global user
    user=nombre_usuario
    usuario = session.query(Usuario).filter_by(nombre_usuario=nombre_usuario, contrasena=contrasena).first()
    if usuario:
        return usuario
    return None

def obtener_roles_usuario(session, id_usuario):
    usuario = session.query(Usuario).filter_by(id_usuario=id_usuario).first()
    if usuario:
        roles = [rol_rol.rol.nombre_rol for rol_rol in usuario.roles]
        return roles
    return []

def obtener_rol_id(session, nombre_rol):
    rol = session.query(Rol).filter_by(nombre_rol=nombre_rol).first()
    return rol.id_rol

def obtener_funciones_rol(session, id_rol):
    funciones = session.query(Funcion).join(FuncionesRol).filter(FuncionesRol.id_rol == id_rol).all()
    return [funcion.nombre_funcion for funcion in funciones]

def obtener_id_usuario(session: Session, nombre_usuario: str) -> int:
    usuario = session.query(Usuario).filter_by(nombre_usuario=nombre_usuario).first()
    return usuario.id_usuario if usuario else None

def listar_usuarios(session: Session, id_usuario_actual: int):
    return session.query(Usuario).filter(Usuario.id_usuario != id_usuario_actual).all()

def listar_documentos_usuario(session: Session, id_usuario: int):
    return session.query(Archivo).filter_by(id_usuario=id_usuario).all()

def obtener_id_documento(session: Session, nombre_documento: str) -> int:
    archivo = session.query(Archivo).filter_by(nombre_archivo=nombre_documento).first()
    return archivo.id_archivo if archivo else None

def compartir_archivo(session, id_documento, id_usuario, id_usuario_destino, fecha_inicio, fecha_expiracion):
    nuevo_permiso = PermisoArchivo(
                    fecha_permiso=fecha_inicio,
                    id_archivo=id_documento,
                    id_usuario=id_usuario,
                    id_usuario_compartido=id_usuario_destino,
                    expiration=fecha_expiracion
    )
    session.add(nuevo_permiso)
    session.commit()

def obtener_id_usuario(session: Session, nombre_usuario: str):
    usuario = session.query(Usuario).filter_by(nombre_usuario=nombre_usuario).first()
    return usuario.id_usuario if usuario else None

def obtener_id_carpeta(session: Session, ruta_carpeta, nombre_carpeta, id_usuario, creacion_carpeta):
    carpeta = session.query(Carpeta).filter_by(ruta_carpeta=ruta_carpeta).first()
    if carpeta:
        return carpeta.id_carpeta
    else:
        nueva_carpeta = Carpeta(
        id_usuario=id_usuario,
        nombre_carpeta=nombre_carpeta,
        ruta_carpeta=ruta_carpeta,
        creacion_carpeta=creacion_carpeta
    )
        session.add(nueva_carpeta)
        session.commit()
        return nueva_carpeta.id_carpeta

def insertar_archivo(session, id_usuario, id_tipo, nombre_archivo, ruta_archivo, creacion_archivo, contenido_binario):
    nuevo_archivo = Archivo(
        id_tipo=id_tipo,
        id_usuario=id_usuario,
        nombre_archivo=nombre_archivo,
        ruta_archivo=ruta_archivo,
        creacion_archivo=creacion_archivo,
        contenido_archivo=contenido_binario
    )
    session.add(nuevo_archivo)
    session.commit()
    return nuevo_archivo

def registrar_log(session, operation, tabla, datos_nuevos=None, datos_viejos=None):
    fecha = datetime.now()
    hora = datetime.utcnow().strftime('%H:%M:%S')
    # Preparar datos para el log
    log = Log(
        fecha_log=fecha,
        hora_log=hora,
        operation=operation,
        dato_nuevo=str(datos_nuevos) if datos_nuevos else None,
        dato_viejo=str(datos_viejos) if datos_viejos else None,
        tabla_insertada=tabla,
        userN=user
   )
    session.add(log)
    session.commit()


# Listener para inserciones
@event.listens_for(Archivo, 'after_insert')
def after_insert(mapper, connection, target):
    global session
    datos_nuevos=({f"{str(v)}, " for k,v in target.__dict__.items() if not k.startswith("_")})
    datos_nuevos=datos_nuevos[:-3]
    registrar_log(session, "INSERT", "Archivo", datos_nuevos)

# Listener para actualizaciones
@event.listens_for(Archivo, 'after_update')
def after_update(mapper, connection, target):
    global session
    inspector = inspect(target)
    dato_viejo = {attr.key: attr.history.deleted[0] for attr in inspector.attrs if attr.history.has_changes() and attr.history.deleted}
    registrar_log(session, "UPDATE", "Archivo", datos_nuevos=str(target), datos_viejos=str(dato_viejo))

# Listener para eliminaciones
@event.listens_for(Archivo, 'after_delete')
def after_delete(mapper, connection, target):
    global session
    registrar_log(session, "DELETE", "Archivo", datos_viejos=str(target))

def serializar_valor(valor):
    try:
        if isinstance(valor, set):
            return list(valor)
        elif isinstance(valor, bytes):
            return base64.b64encode(valor).decode()
        elif isinstance(valor, datetime):
            return str(valor)
        json.dumps(valor)
        return valor
    except (TypeError, ValueError):
        return str(valor)

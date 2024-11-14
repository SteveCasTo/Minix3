from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from models import *
from datetime import date

def insertar_user(session, nombre, contrasena, active=True):
    nuevo_user = Usuario(nombre, contrasena, active)
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

def obtener_funciones_rol(session, id_rol):
    funciones = session.query(Funcion).join(FuncionesRol).filter(FuncionesRol.id_rol == id_rol).all()
    return [funcion.nombre_funcion for funcion in funciones]

def obtener_id_usuario(session: Session, nombre_usuario: str) -> int:
    usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()
    return usuario.id_usr if usuario else None

def listar_usuarios(session: Session, id_usuario_actual: int):
    return session.query(Usuario).filter(Usuario.id_usr != id_usuario_actual).all()

def listar_documentos_usuario(session: Session, id_usuario: int):
    return session.query(Archivo).filter_by(id_usr=id_usuario).all()

def obtener_id_documento(session: Session, nombre_documento: str) -> int:
    archivo = session.query(Archivo).filter_by(nombre=nombre_documento).first()
    return archivo.id_achv if archivo else None

def compartir_archivo(session: Session, id_documento: int, id_usuario: int, id_usuario_destino: int, fecha_expiracion: date):
    nuevo_permiso = PermisoArchivo(id_achv=id_documento, id_usr=id_usuario, id_usr_destino=id_usuario_destino, fecha_exp=fecha_expiracion)
    session.add(nuevo_permiso)
    session.commit()

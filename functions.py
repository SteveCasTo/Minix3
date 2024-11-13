from sqlalchemy.orm import sessionmaker
from models import *

# Crear una sesión de SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# Función para autenticar usuario
def autenticar_usuario(nombre_usuario, contrasena):
    usuario = session.query(Usuario).filter_by(nombre_usuario=nombre_usuario, contrasena=contrasena).first()
    if usuario:
        return usuario
    return None

# Función para obtener roles de un usuario
def obtener_roles_usuario(id_usuario):
    usuario = session.query(Usuario).filter_by(id_usuario=id_usuario).first()
    if usuario:
        roles = [rol_rol.rol.nombre_rol for rol_rol in usuario.roles]
        return roles
    return []

# Función para obtener funciones de un rol
def obtener_funciones_rol(id_rol):
    funciones = session.query(Funcion).join(FuncionesRol).filter(FuncionesRol.id_rol == id_rol).all()
    return [funcion.nombre_funcion for funcion in funciones]

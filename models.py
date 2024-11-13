from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

# Tabla: UI
class UI(Base):
    __tablename__ = 'UI'
    
    id_ui = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    
    funciones = relationship('UiFuncion', back_populates='ui')

# Tabla: Funcion
class Funcion(Base):
    __tablename__ = 'Funcion'
    
    id_funcion = Column(Integer, primary_key=True)
    nombre_funcion = Column(String, nullable=False)
    
    roles = relationship('FuncionesRol', back_populates='funcion')
    ui_funciones = relationship('UiFuncion', back_populates='funcion')

# Tabla: Rol
class Rol(Base):
    __tablename__ = 'Rol'
    
    id_rol = Column(Integer, primary_key=True)
    nombre_rol = Column(String, nullable=False)
    
    funciones = relationship('FuncionesRol', back_populates='rol')
    usuarios = relationship('RolesUser', back_populates='rol')

# Tabla: Sesion
class Sesion(Base):
    __tablename__ = 'Sesion'
    
    id_sesion = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'), nullable=False)
    
    usuario = relationship('Usuario', back_populates='sesiones')

# Tabla: Ui_funcion (relación muchos a muchos entre UI y Funcion)
class UiFuncion(Base):
    __tablename__ = 'Ui_funcion'
    
    id_ui = Column(Integer, ForeignKey('UI.id_ui'), primary_key=True)
    id_funcion = Column(Integer, ForeignKey('Funcion.id_funcion'), primary_key=True)
    fecha_desde = Column(Date, primary_key=True)
    fecha_hasta = Column(Date, nullable=False)
    estado = Column(String, nullable=False)
    
    ui = relationship('UI', back_populates='funciones')
    funcion = relationship('Funcion', back_populates='ui_funciones')

# Tabla: Funciones_Rol (relación muchos a muchos entre Funcion y Rol)
class FuncionesRol(Base):
    __tablename__ = 'Funciones_Rol'
    
    id_funcion = Column(Integer, ForeignKey('Funcion.id_funcion'), primary_key=True)
    id_rol = Column(Integer, ForeignKey('Rol.id_rol'), primary_key=True)
    fecha_desde = Column(Date, primary_key=True)
    fecha_hasta = Column(Date, nullable=False)
    estado = Column(String, nullable=False)
    
    funcion = relationship('Funcion', back_populates='roles')
    rol = relationship('Rol', back_populates='funciones')

# Tabla: Roles_User (relación muchos a muchos entre Usuario y Rol)
class RolesUser(Base):
    __tablename__ = 'Roles_User'
    
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'), primary_key=True)
    id_rol = Column(Integer, ForeignKey('Rol.id_rol'), primary_key=True)
    fecha_desde = Column(Date, primary_key=True)
    fecha_hasta = Column(Date, nullable=False)
    estado = Column(String, nullable=False)
    
    usuario = relationship('Usuario', back_populates='roles')
    rol = relationship('Rol', back_populates='usuarios')

# Clase Tipo
class Tipo(Base):
    __tablename__ = 'Tipo'
    
    id_tipo = Column(Integer, primary_key=True)
    nombre_tipo = Column(String, nullable=False)
    
    archivos = relationship('Archivo', back_populates='tipo')

# Clase Archivo
class Archivo(Base):
    __tablename__ = 'Archivo'
    
    id_archivo = Column(Integer, primary_key=True)
    id_tipo = Column(Integer, ForeignKey('Tipo.id_tipo'), nullable=False)
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'), nullable=False)
    nombre_archivo = Column(String(255), nullable=False)
    ruta_archivo = Column(String, nullable=False)
    creacion_archivo = Column(Date, nullable=False)
    
    tipo = relationship('Tipo', back_populates='archivos')
    usuario = relationship('Usuario', back_populates='archivos')
    versiones = relationship('Version', back_populates='archivo')

# Clase Version
class Version(Base):
    __tablename__ = 'Version'
    
    id_version = Column(Integer, primary_key=True)
    id_archivo = Column(Integer, ForeignKey('Archivo.id_archivo'), nullable=False)
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'), nullable=False)
    num_version = Column(Integer, nullable=False)
    
    archivo = relationship('Archivo', back_populates='versiones')

# Clase Log
class Log(Base):
    __tablename__ = 'Log'
    
    id_log = Column(Integer, primary_key=True)
    fecha_log = Column(Date, nullable=False)
    hora_log = Column(String, nullable=False)
    operation = Column(String, nullable=False)
    dato_nuevo = Column(String(1000))
    dato_viejo = Column(String(1000))
    tabla_insertada = Column(String, nullable=False)
    userN = Column(String, nullable=False)

# Clase Permiso_Archivo
class PermisoArchivo(Base):
    __tablename__ = 'Permiso_Archivo'
    
    fecha_permiso = Column(Date, primary_key=True)
    id_archivo = Column(Integer, ForeignKey('Archivo.id_archivo'), primary_key=True)
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'), primary_key=True)
    id_usuario_compartido = Column(Integer, ForeignKey('Usuario.id_usuario'), primary_key=True)
    expiration = Column(Date, nullable=False)

    archivo = relationship('Archivo')
    usuario = relationship('Usuario', foreign_keys=[id_usuario])
    usuario_compartido = relationship('Usuario', foreign_keys=[id_usuario_compartido])

# Clase Permiso_Carpeta
class PermisoCarpeta(Base):
    __tablename__ = 'Permiso_Carpeta'
    
    fecha_permiso = Column(Date, primary_key=True)
    id_carpeta = Column(Integer, ForeignKey('Carpeta.id_carpeta'), primary_key=True)
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'), primary_key=True)
    id_usuario_compartido = Column(Integer, ForeignKey('Usuario.id_usuario'), primary_key=True)
    expiration = Column(Date, nullable=False)
    
    carpeta = relationship('Carpeta')
    usuario = relationship('Usuario', foreign_keys=[id_usuario])
    usuario_compartido = relationship('Usuario', foreign_keys=[id_usuario_compartido])

# Clase Carpeta
class Carpeta(Base):
    __tablename__ = 'Carpeta'
    
    id_carpeta = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'), nullable=False)
    nombre_carpeta = Column(String, nullable=False)
    ruta_carpeta = Column(String, nullable=False)
    creacion_carpeta = Column(Date, nullable=False)
    
    usuario = relationship('Usuario', back_populates='carpetas')

# Clase Usuario (Modificada para incluir relaciones adicionales)
class Usuario(Base):
    __tablename__ = 'Usuario'
    
    id_usuario = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(255), nullable=False)
    contrasena = Column(String(255), nullable=False)
    active = Column(Boolean, nullable=False)
    
    roles = relationship('RolesUser', back_populates='usuario')
    sesiones = relationship('Sesion', back_populates='usuario')
    archivos = relationship('Archivo', back_populates='usuario')
    carpetas = relationship('Carpeta', back_populates='usuario')
    
    def __str__(self):
        return self.nombre_usuario + " , " + self.contrasena

# Clase Desarrollador (Extiende Usuario)
class Desarrollador(Usuario):
    __tablename__ = 'Desarrollador'
    
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'), primary_key=True)
    email = Column(String(255), nullable=False)
    creacion_usuario = Column(Date, nullable=False)




if __name__ == '__main__':
    engine = create_engine('postgresql://stevecas:486579@localhost/ORMGestor')
    Base.metadata.create_all(engine)
    # # Crear usuarios nuevos
    # user1 = Usuario(nombre_usuario="jose", contrasena=123456789, active=True)
    # user2 = Usuario(nombre_usuario="laura", contrasena=987654321, active=True)
    # user3 = Usuario(nombre_usuario="andre", contrasena=246813579, active=True)

    # # Añadir cambios en nuestro stack 
    # session.add(user1)
    # session.add(user2)
    # session.add(user3)
    
    # # Ejemplo de instanciación
    # tipo_documento = Tipo(nombre_tipo="Documento")
    # usuario_jose = Usuario(nombre_usuario="jose", contrasena="hashed_password", active=True)
    # carpeta_personal = Carpeta(nombre_carpeta="Personal", ruta_carpeta="/home/jose/personal", creacion_carpeta="2024-10-31", usuario=usuario_jose)
    
    # # Añadir y guardar
    # session.add_all([tipo_documento, usuario_jose, carpeta_personal])
    
    # # Persistir cambios en la base de datos
    # session.commit()
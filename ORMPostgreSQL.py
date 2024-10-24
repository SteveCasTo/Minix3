from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

# Crear el engine y la base de datos
engine = create_engine('postgresql://stevecas:486579@localhost/ORMGestor')

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

# Tabla: Usuario
class Usuario(Base):
    __tablename__ = 'Usuario'
    
    id_usuario = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(255), nullable=False)
    contrasena = Column(String(255), nullable=False)
    active = Column(Boolean, nullable=False)
    
    roles = relationship('RolesUser', back_populates='usuario')
    sesiones = relationship('Sesion', back_populates='usuario')

    def __str__(self):
        return self.nombre_usuario + " , " + self.contrasena

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

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    # Eliminar todas las tablas
    Base.metadata.drop_all(engine)
    
    # Crear todas las tablas
    Base.metadata.create_all(engine)
    
    # Crear usuarios nuevos
    user1 = Usuario(nombre_usuario="jose", contrasena=123456789, active=True)
    user2 = Usuario(nombre_usuario="laura", contrasena=987654321, active=True)
    user3 = Usuario(nombre_usuario="andre", contrasena=246813579, active=True)

    # Añadir cambios en nuestro stack 
    session.add(user1)
    session.add(user2)
    session.add(user3)
    
    # Persistir cambios en la base de datos
    session.commit()

    # Consulta generica
    users = session.query(Usuario).all()
    # users es una lista
    for user in users:
        print(user)
        
    # Consulta específica
    users = session.query(Usuario).filter(
        Usuario.id_usuario == 2
    )
    # users es una lista
    for user in users:
        print(user)

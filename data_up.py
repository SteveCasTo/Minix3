from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from functions import *

# Configuración de SQLAlchemy
engine = create_engine('postgresql://usuario:contraseña@localhost/tu_base_de_datos')
Session = sessionmaker(bind=engine)
session = Session()

# # Insertar roles
# insertar_roles(session, 1, 'Administrador')
# insertar_roles(session, 2, 'ManipuladorElementos')

# # Insertar UIs
# insertar_ui(session, 1, 'Edicion')
# insertar_ui(session, 2, 'Compartir')

# # Insertar funciones
# insertar_funciones(session, 1, 'CrearDocumentoTexto')
# insertar_funciones(session, 2, 'CrearDocumentoExcel')
insertar_user(session, "steve", 486579, active=True)
insertar_user(session, "jose", 123456789, active=True)
insertar_user(session, "laura", 987654321, active=True)
insertar_user(session, "andre", 246813579, active=True)

# Cerrar la sesión
session.close()

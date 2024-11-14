from sqlalchemy import event

def registrar_log(mapper, user, connection, target, operation):
    fecha = datetime.utcnow().date()
    hora = datetime.utcnow().strftime('%H:%M:%S')
    tabla = target.__tablename__
    
    # Obtener datos nuevos y antiguos
    datos_nuevos = {col.name: getattr(target, col.name) for col in target.__table__.columns}
    datos_viejos = None
    
    if operation == "UPDATE":
        state = Session.object_session(target)._get_state_attr_by_key(target)
        datos_viejos = {k: v for k, v in state.committed_state.items() if k in datos_nuevos and datos_nuevos[k] != v}
    
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
    
    session = Session(bind=connection)
    session.add(log)
    session.commit()


# Listener para INSERT
@event.listens_for(Session, 'after_insert')
def log_insert(mapper, connection, target):
    registrar_log(mapper, connection, target, "INSERT")

# Listener para UPDATE
@event.listens_for(Session, 'after_update')
def log_update(mapper, connection, target):
    registrar_log(mapper, connection, target, "UPDATE")

# Listener para DELETE
@event.listens_for(Session, 'after_delete')
def log_delete(mapper, connection, target):
    registrar_log(mapper, connection, target, "DELETE")

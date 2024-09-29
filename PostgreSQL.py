CREATE OR REPLACE FUNCTION log_funcion_changes() 
RETURNS TRIGGER 
LANGUAGE plpgsql
AS $$
BEGIN
    -- Insertar en la tabla Log
    INSERT INTO Log (fecha_log, hora_log, operacion_log, dato_nuevo, dato_viejo, tabla_insertada, usern)
    VALUES (
        CURRENT_DATE,                -- Fecha actual
        CURRENT_TIME,                -- Hora actual
        TG_OP,                       -- Tipo de operación (INSERT, UPDATE, DELETE)
        ROW(NEW.*)::TEXT,            -- Datos nuevos (si los hay)
        ROW(OLD.*)::TEXT,            -- Datos viejos (si los hay)
        TG_TABLE_NAME,               -- Nombre de la tabla que se está modificando
        SESSION_USER                 -- Usuario que realizó la operación
    );
    
    -- Continuar con la operación original
    RETURN NEW;
END;
$$;

CREATE TRIGGER trigger_log_funcion
AFTER INSERT OR UPDATE OR DELETE
ON Funcion
FOR EACH ROW
EXECUTE FUNCTION log_funcion_changes();

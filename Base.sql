PGDMP  *    .    
        	    |            Gestor_Archivos #   16.4 (Ubuntu 16.4-0ubuntu0.24.04.1) #   16.4 (Ubuntu 16.4-0ubuntu0.24.04.1) �    #           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            $           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            %           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            &           1262    24810    Gestor_Archivos    DATABASE     }   CREATE DATABASE "Gestor_Archivos" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'es_ES.UTF-8';
 !   DROP DATABASE "Gestor_Archivos";
                stevecas    false            '           0    0    DATABASE "Gestor_Archivos"    ACL     �   GRANT ALL ON DATABASE "Gestor_Archivos" TO jose;
GRANT ALL ON DATABASE "Gestor_Archivos" TO laura;
GRANT ALL ON DATABASE "Gestor_Archivos" TO andre;
                   stevecas    false    3622            (           0    0    SCHEMA public    ACL     t   GRANT USAGE ON SCHEMA public TO jose;
GRANT USAGE ON SCHEMA public TO laura;
GRANT USAGE ON SCHEMA public TO andre;
                   pg_database_owner    false    5            �           1247    25359    active    DOMAIN     �   CREATE DOMAIN public.active AS character varying
	CONSTRAINT active_check CHECK (((VALUE)::text = ANY ((ARRAY['Yes'::character varying, 'No'::character varying])::text[])));
    DROP DOMAIN public.active;
       public          stevecas    false                       1255    25443    achv_fromcpt(character varying)    FUNCTION     �   CREATE FUNCTION public.achv_fromcpt(rut_cpt character varying) RETURNS TABLE(ruta_archivo character varying)
    LANGUAGE plpgsql
    AS $$
BEGIN
RETURN QUERY
	SELECT a.ruta_archivo
	FROM Archivo a
	WHERE a.ruta_archivo LIKE rut_cpt;
END;
$$;
 >   DROP FUNCTION public.achv_fromcpt(rut_cpt character varying);
       public          stevecas    false                       1255    25424    achv_user(integer)    FUNCTION     �   CREATE FUNCTION public.achv_user(id_usr integer) RETURNS TABLE(nombre_archivo character varying)
    LANGUAGE plpgsql
    AS $$
BEGIN
RETURN QUERY
SELECT a.nombre_archivo
	FROM Archivo a
	WHERE a.id_usuario = id_usr;
END;
$$;
 0   DROP FUNCTION public.achv_user(id_usr integer);
       public          stevecas    false            �            1255    25423    achv_user_comp(integer)    FUNCTION     -  CREATE FUNCTION public.achv_user_comp(id_usr integer) RETURNS TABLE(nombre_archivo character varying)
    LANGUAGE plpgsql
    AS $$
BEGIN
RETURN QUERY
SELECT a.nombre_archivo
	FROM Archivo a
	JOIN Permiso_Archivo pa on a.id_archivo = pa.id_archivo
	WHERE pa.id_ususario_compartido = id_usr;
END;
$$;
 5   DROP FUNCTION public.achv_user_comp(id_usr integer);
       public          stevecas    false                       1255    25450 :   act_rutachv(character varying, character varying, integer)    FUNCTION     
  CREATE FUNCTION public.act_rutachv(nw_rut character varying, nom_achv character varying, id_usr integer) RETURNS void
    LANGUAGE plpgsql
    AS $$
BEGIN
	UPDATE Archivo
	SET ruta_archivo = nw_rut
	WHERE nombre_archivo = nom_achv
	AND id_usuario = id_usr;
END;
$$;
 h   DROP FUNCTION public.act_rutachv(nw_rut character varying, nom_achv character varying, id_usr integer);
       public          stevecas    false            
           1255    25441    cpt_user(integer)    FUNCTION     �   CREATE FUNCTION public.cpt_user(id_usr integer) RETURNS TABLE(nombre_carpeta character varying)
    LANGUAGE plpgsql
    AS $$
BEGIN
RETURN QUERY
SELECT c.nombre_carpeta
	FROM Carpeta c
	WHERE c.id_usuario = id_usr;
END;
$$;
 /   DROP FUNCTION public.cpt_user(id_usr integer);
       public          stevecas    false                       1255    25409     delete_achvid(character varying)    FUNCTION     �   CREATE FUNCTION public.delete_achvid(nom_achv character varying) RETURNS void
    LANGUAGE plpgsql
    AS $$
BEGIN
	DELETE FROM Archivo 
	WHERE nombre_archivo = nom_achv;
END;
$$;
 @   DROP FUNCTION public.delete_achvid(nom_achv character varying);
       public          stevecas    false            )           0    0 2   FUNCTION delete_achvid(nom_achv character varying)    ACL     �   GRANT ALL ON FUNCTION public.delete_achvid(nom_achv character varying) TO jose;
GRANT ALL ON FUNCTION public.delete_achvid(nom_achv character varying) TO laura;
GRANT ALL ON FUNCTION public.delete_achvid(nom_achv character varying) TO andre;
          public          stevecas    false    260                       1255    25444    delete_achvr(character varying)    FUNCTION     �   CREATE FUNCTION public.delete_achvr(rut_achv character varying) RETURNS void
    LANGUAGE plpgsql
    AS $$
BEGIN
	DELETE FROM Archivo a
	WHERE a.ruta_archivo = rut_achv;
END;
$$;
 ?   DROP FUNCTION public.delete_achvr(rut_achv character varying);
       public          stevecas    false            �            1255    25447 &   delete_cpt(character varying, integer)    FUNCTION     �   CREATE FUNCTION public.delete_cpt(nom_cpt character varying, id_usr integer) RETURNS void
    LANGUAGE plpgsql
    AS $$
BEGIN
	DELETE FROM Carpeta c
	WHERE c.nombre_carpeta = nom_cpt
	AND c.id_usuario = id_usr;
END;
$$;
 L   DROP FUNCTION public.delete_cpt(nom_cpt character varying, id_usr integer);
       public          stevecas    false                       1255    25412    delete_permsachv()    FUNCTION     �   CREATE FUNCTION public.delete_permsachv() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
	DELETE FROM permiso_archivo where id_archivo = OLD.id_archivo;
    RETURN OLD;
END;
$$;
 )   DROP FUNCTION public.delete_permsachv();
       public          stevecas    false            *           0    0    FUNCTION delete_permsachv()    ACL     �   GRANT ALL ON FUNCTION public.delete_permsachv() TO jose;
GRANT ALL ON FUNCTION public.delete_permsachv() TO laura;
GRANT ALL ON FUNCTION public.delete_permsachv() TO andre;
          public          stevecas    false    269                       1255    25414    delete_permscrp()    FUNCTION     �   CREATE FUNCTION public.delete_permscrp() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
	DELETE FROM permiso_carpeta where id_carpeta = OLD.id_carpeta;
    RETURN OLD;
END;
$$;
 (   DROP FUNCTION public.delete_permscrp();
       public          stevecas    false            +           0    0    FUNCTION delete_permscrp()    ACL     �   GRANT ALL ON FUNCTION public.delete_permscrp() TO andre;
GRANT ALL ON FUNCTION public.delete_permscrp() TO laura;
GRANT ALL ON FUNCTION public.delete_permscrp() TO jose;
          public          stevecas    false    270            	           1255    25433    druta_achv(character varying)    FUNCTION     �   CREATE FUNCTION public.druta_achv(nom_achv character varying) RETURNS character varying
    LANGUAGE plpgsql
    AS $$
DECLARE
	rut varchar;
BEGIN
	SELECT a.ruta_archivo into rut
	FROM Archivo a
	WHERE a.nombre_archivo = nom_achv;
	return rut;
END;
$$;
 =   DROP FUNCTION public.druta_achv(nom_achv character varying);
       public          stevecas    false                       1255    25442 &   druta_cpts(character varying, integer)    FUNCTION       CREATE FUNCTION public.druta_cpts(nom_cpt character varying, id_usr integer) RETURNS TABLE(ruta_carpeta character varying)
    LANGUAGE plpgsql
    AS $$
BEGIN
RETURN QUERY
	SELECT c.ruta_carpeta
	FROM Carpeta c
	WHERE c.nombre_carpeta = nom_cpt
	AND c.id_usuario = id_usr;
END;
$$;
 L   DROP FUNCTION public.druta_cpts(nom_cpt character varying, id_usr integer);
       public          stevecas    false                       1255    25408    get_achvid(character varying)    FUNCTION     �   CREATE FUNCTION public.get_achvid(nom_achv character varying) RETURNS integer
    LANGUAGE plpgsql
    AS $$
DECLARE
	ids integer;
BEGIN
	SELECT id_archivo into ids
	FROM Archivo
	WHERE nombre_archivo = nom_achv;
	return ids;
END;
$$;
 =   DROP FUNCTION public.get_achvid(nom_achv character varying);
       public          stevecas    false            ,           0    0 /   FUNCTION get_achvid(nom_achv character varying)    ACL     �   GRANT ALL ON FUNCTION public.get_achvid(nom_achv character varying) TO jose;
GRANT ALL ON FUNCTION public.get_achvid(nom_achv character varying) TO laura;
GRANT ALL ON FUNCTION public.get_achvid(nom_achv character varying) TO andre;
          public          stevecas    false    259            �            1255    24966    get_idusr(character varying)    FUNCTION     �   CREATE FUNCTION public.get_idusr(name character varying) RETURNS integer
    LANGUAGE plpgsql
    AS $$
declare
	usuario_id integer;
begin
	select id_usuario into usuario_id
	from Usuario
	where nombre_usuario = name;
	return usuario_id;
end;
$$;
 8   DROP FUNCTION public.get_idusr(name character varying);
       public          stevecas    false            -           0    0 *   FUNCTION get_idusr(name character varying)    ACL     �   GRANT ALL ON FUNCTION public.get_idusr(name character varying) TO jose;
GRANT ALL ON FUNCTION public.get_idusr(name character varying) TO laura;
GRANT ALL ON FUNCTION public.get_idusr(name character varying) TO andre;
          public          stevecas    false    240            �            1255    25381    get_pid(integer)    FUNCTION       CREATE FUNCTION public.get_pid(id_user integer) RETURNS integer
    LANGUAGE plpgsql
    AS $$
DECLARE
	pids integer;
BEGIN
	select pid into pids
	from Sesion
	where id_usuario = id_user;
	
	IF NOT FOUND THEN
	select pg_backend_pid() into pids;
	END IF;
	
	RETURN pids;
END;
$$;
 /   DROP FUNCTION public.get_pid(id_user integer);
       public          stevecas    false            .           0    0 !   FUNCTION get_pid(id_user integer)    ACL     �   GRANT ALL ON FUNCTION public.get_pid(id_user integer) TO jose;
GRANT ALL ON FUNCTION public.get_pid(id_user integer) TO laura;
GRANT ALL ON FUNCTION public.get_pid(id_user integer) TO andre;
          public          stevecas    false    238            �            1255    25383    get_rol(integer)    FUNCTION     *  CREATE FUNCTION public.get_rol(id_user integer) RETURNS character varying
    LANGUAGE plpgsql
    AS $$
DECLARE
	nom_rol varchar;
BEGIN
	SELECT nombre_rol into nom_rol
	FROM Rol 
	JOIN Roles_User ON Rol.id_rol = Roles_User.id_rol 
	WHERE Roles_User.id_usuario = id_user;
	RETURN nom_rol;
END;
$$;
 /   DROP FUNCTION public.get_rol(id_user integer);
       public          stevecas    false            /           0    0 !   FUNCTION get_rol(id_user integer)    ACL     �   GRANT ALL ON FUNCTION public.get_rol(id_user integer) TO jose;
GRANT ALL ON FUNCTION public.get_rol(id_user integer) TO laura;
GRANT ALL ON FUNCTION public.get_rol(id_user integer) TO andre;
          public          stevecas    false    237                       1255    25384    get_ui_fun(character varying)    FUNCTION     c  CREATE FUNCTION public.get_ui_fun(rol_usr character varying) RETURNS TABLE(ui character varying, fncion character varying)
    LANGUAGE plpgsql
    AS $$
BEGIN
RETURN QUERY
SELECT distinct on (nombre_funcion) url, nombre_funcion
    FROM Funcion
    JOIN UI_Funcion ON Funcion.id_funcion = UI_Funcion.id_funcion
    JOIN UI ON UI.id_ui = UI_Funcion.id_ui
    JOIN Funciones_Rol ON Funcion.id_funcion = Funciones_Rol.id_funcion
    JOIN Rol ON Rol.id_rol = Funciones_Rol.id_rol
    JOIN Roles_User ON Rol.id_rol = Roles_User.id_rol
    WHERE Roles_User.estado = 'Activo' 
	AND Rol.nombre_rol = rol_usr;
END;
$$;
 <   DROP FUNCTION public.get_ui_fun(rol_usr character varying);
       public          stevecas    false            0           0    0 .   FUNCTION get_ui_fun(rol_usr character varying)    ACL     �   GRANT ALL ON FUNCTION public.get_ui_fun(rol_usr character varying) TO jose;
GRANT ALL ON FUNCTION public.get_ui_fun(rol_usr character varying) TO laura;
GRANT ALL ON FUNCTION public.get_ui_fun(rol_usr character varying) TO andre;
          public          stevecas    false    257                       1255    25418 $   id_carpet_forruta(character varying)    FUNCTION     �   CREATE FUNCTION public.id_carpet_forruta(ruta_cpt character varying) RETURNS integer
    LANGUAGE plpgsql
    AS $$
DECLARE
	id_cpt integer;
BEGIN
SELECT c.id_carpeta into id_cpt
	FROM Carpeta c
	WHERE c.ruta_carpeta = ruta_cpt;
	return id_cpt;
END;
$$;
 D   DROP FUNCTION public.id_carpet_forruta(ruta_cpt character varying);
       public          stevecas    false                       1255    25407 C   insert_achv(integer, integer, character varying, character varying)    FUNCTION     �  CREATE FUNCTION public.insert_achv(id_user integer, id_tip integer, nom_achv character varying, ruta_achv character varying) RETURNS void
    LANGUAGE plpgsql
    AS $$
BEGIN
	INSERT INTO Archivo (id_usuario, id_tipo, nombre_archivo, ruta_archivo, creacion_archivo, contenido_archivo)
    VALUES (id_user,
			id_tip,
			nom_achv,
			ruta_achv,
			CURRENT_DATE,
			pg_read_binary_file(ruta_achv));
END;
$$;
 |   DROP FUNCTION public.insert_achv(id_user integer, id_tip integer, nom_achv character varying, ruta_achv character varying);
       public          stevecas    false            1           0    0 n   FUNCTION insert_achv(id_user integer, id_tip integer, nom_achv character varying, ruta_achv character varying)    ACL     �  GRANT ALL ON FUNCTION public.insert_achv(id_user integer, id_tip integer, nom_achv character varying, ruta_achv character varying) TO jose;
GRANT ALL ON FUNCTION public.insert_achv(id_user integer, id_tip integer, nom_achv character varying, ruta_achv character varying) TO laura;
GRANT ALL ON FUNCTION public.insert_achv(id_user integer, id_tip integer, nom_achv character varying, ruta_achv character varying) TO andre;
          public          stevecas    false    261                        1255    25425 S   insert_achv_withcont(integer, integer, character varying, character varying, bytea)    FUNCTION     �  CREATE FUNCTION public.insert_achv_withcont(id_user integer, id_tip integer, nom_achv character varying, ruta_achv character varying, contenido_achv bytea) RETURNS void
    LANGUAGE plpgsql
    AS $$
BEGIN
	INSERT INTO Archivo (id_usuario, id_tipo, nombre_archivo, ruta_archivo, creacion_archivo, contenido_archivo)
    VALUES (id_user,
			id_tip,
			nom_achv,
			ruta_achv,
			CURRENT_DATE,
			contenido_achv);
END;
$$;
 �   DROP FUNCTION public.insert_achv_withcont(id_user integer, id_tip integer, nom_achv character varying, ruta_achv character varying, contenido_achv bytea);
       public          stevecas    false                       1255    25419 <   insert_carpet(integer, character varying, character varying)    FUNCTION     8  CREATE FUNCTION public.insert_carpet(id_usr integer, nom_cpt character varying, ruta_cpt character varying) RETURNS void
    LANGUAGE plpgsql
    AS $$
BEGIN
	INSERT INTO Carpeta (id_usuario, nombre_carpeta, ruta_carpeta, creacion_carpeta)
    VALUES (id_usr,
			nom_cpt,
			ruta_cpt,
			CURRENT_DATE);
END;
$$;
 k   DROP FUNCTION public.insert_carpet(id_usr integer, nom_cpt character varying, ruta_cpt character varying);
       public          stevecas    false                       1255    25420 /   insert_carpet_oblig(integer, character varying)    FUNCTION     (  CREATE FUNCTION public.insert_carpet_oblig(id_usr integer, ruta_cpt character varying) RETURNS void
    LANGUAGE plpgsql
    AS $$
BEGIN
	INSERT INTO Carpeta (id_usuario, nombre_carpeta, ruta_carpeta, creacion_carpeta)
    VALUES (id_usr,
			CURRENT_DATE,
			ruta_cpt,
			CURRENT_DATE);
END;
$$;
 V   DROP FUNCTION public.insert_carpet_oblig(id_usr integer, ruta_cpt character varying);
       public          stevecas    false            �            1255    25411 3   insert_permisoachv(integer, integer, integer, date)    FUNCTION       CREATE FUNCTION public.insert_permisoachv(id_achv integer, id_user integer, id_user_comp integer, expn date) RETURNS void
    LANGUAGE plpgsql
    AS $$
BEGIN
	INSERT INTO Permiso_Archivo
    VALUES (CURRENT_DATE,
			id_achv,
			id_user,
			id_user_comp,
			expn);
END;
$$;
 l   DROP FUNCTION public.insert_permisoachv(id_achv integer, id_user integer, id_user_comp integer, expn date);
       public          stevecas    false            2           0    0 ^   FUNCTION insert_permisoachv(id_achv integer, id_user integer, id_user_comp integer, expn date)    ACL     v  GRANT ALL ON FUNCTION public.insert_permisoachv(id_achv integer, id_user integer, id_user_comp integer, expn date) TO jose;
GRANT ALL ON FUNCTION public.insert_permisoachv(id_achv integer, id_user integer, id_user_comp integer, expn date) TO laura;
GRANT ALL ON FUNCTION public.insert_permisoachv(id_achv integer, id_user integer, id_user_comp integer, expn date) TO andre;
          public          stevecas    false    254            �            1255    25171    insert_sesion(integer, integer)    FUNCTION     9  CREATE FUNCTION public.insert_sesion(ids integer, p_pid integer) RETURNS integer
    LANGUAGE plpgsql
    AS $$
declare
pid2 integer;
begin
	select pid into pid2
	from Sesion
	where id_sesion = ids;
	
	if not found then
	insert into Sesion (id_usuario, pid) values (ids, p_pid);
	end if;
	
	return pid2;
end;
$$;
 @   DROP FUNCTION public.insert_sesion(ids integer, p_pid integer);
       public          stevecas    false            3           0    0 2   FUNCTION insert_sesion(ids integer, p_pid integer)    ACL     �   GRANT ALL ON FUNCTION public.insert_sesion(ids integer, p_pid integer) TO jose;
GRANT ALL ON FUNCTION public.insert_sesion(ids integer, p_pid integer) TO laura;
GRANT ALL ON FUNCTION public.insert_sesion(ids integer, p_pid integer) TO andre;
          public          stevecas    false    239            �            1255    25422    listar_usrs(integer)    FUNCTION     �   CREATE FUNCTION public.listar_usrs(id_usr integer) RETURNS TABLE(nombre_usuario character varying)
    LANGUAGE plpgsql
    AS $$
BEGIN
	RETURN QUERY
	SELECT u.nombre_usuario
	FROM Usuario u
	WHERE u.id_usuario != id_usr;
END;
$$;
 2   DROP FUNCTION public.listar_usrs(id_usr integer);
       public          stevecas    false                       1255    25387    tf_changestable()    FUNCTION     �  CREATE FUNCTION public.tf_changestable() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    INSERT INTO Log (fecha_log, hora_log, operacion_log, dato_nuevo, dato_viejo, tabla_insertada, usern)
    VALUES (
        CURRENT_DATE,
        CURRENT_TIME,
        TG_OP,
        ROW(NEW.*)::TEXT,
        ROW(OLD.*)::TEXT,
        TG_TABLE_NAME,
        SESSION_USER
    );
    RETURN NEW;
END;
$$;
 (   DROP FUNCTION public.tf_changestable();
       public          stevecas    false            4           0    0    FUNCTION tf_changestable()    ACL     �   GRANT ALL ON FUNCTION public.tf_changestable() TO jose;
GRANT ALL ON FUNCTION public.tf_changestable() TO laura;
GRANT ALL ON FUNCTION public.tf_changestable() TO andre;
          public          stevecas    false    271            �            1259    25403    mi_archivo_id_seq    SEQUENCE     z   CREATE SEQUENCE public.mi_archivo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.mi_archivo_id_seq;
       public          stevecas    false            5           0    0    SEQUENCE mi_archivo_id_seq    ACL     �   GRANT ALL ON SEQUENCE public.mi_archivo_id_seq TO jose;
GRANT ALL ON SEQUENCE public.mi_archivo_id_seq TO laura;
GRANT ALL ON SEQUENCE public.mi_archivo_id_seq TO andre;
          public          stevecas    false    235            �            1259    25247    archivo    TABLE     X  CREATE TABLE public.archivo (
    id_archivo integer DEFAULT nextval('public.mi_archivo_id_seq'::regclass) NOT NULL,
    id_usuario integer NOT NULL,
    id_tipo integer NOT NULL,
    nombre_archivo character varying(255) NOT NULL,
    ruta_archivo character varying NOT NULL,
    creacion_archivo date NOT NULL,
    contenido_archivo bytea
);
    DROP TABLE public.archivo;
       public         heap    stevecas    false    235            6           0    0    TABLE archivo    ACL     �   GRANT ALL ON TABLE public.archivo TO jose;
GRANT ALL ON TABLE public.archivo TO laura;
GRANT ALL ON TABLE public.archivo TO andre;
          public          stevecas    false    227            �            1259    25405    mi_carpeta_id_seq    SEQUENCE     z   CREATE SEQUENCE public.mi_carpeta_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.mi_carpeta_id_seq;
       public          stevecas    false            7           0    0    SEQUENCE mi_carpeta_id_seq    ACL     �   GRANT ALL ON SEQUENCE public.mi_carpeta_id_seq TO jose;
GRANT ALL ON SEQUENCE public.mi_carpeta_id_seq TO laura;
GRANT ALL ON SEQUENCE public.mi_carpeta_id_seq TO andre;
          public          stevecas    false    236            �            1259    25264    carpeta    TABLE       CREATE TABLE public.carpeta (
    id_carpeta integer DEFAULT nextval('public.mi_carpeta_id_seq'::regclass) NOT NULL,
    id_usuario integer NOT NULL,
    nombre_carpeta character varying(255) NOT NULL,
    ruta_carpeta character varying NOT NULL,
    creacion_carpeta date NOT NULL
);
    DROP TABLE public.carpeta;
       public         heap    stevecas    false    236            8           0    0    TABLE carpeta    ACL     �   GRANT ALL ON TABLE public.carpeta TO jose;
GRANT ALL ON TABLE public.carpeta TO laura;
GRANT ALL ON TABLE public.carpeta TO andre;
          public          stevecas    false    230            �            1259    25242    desarrollador    TABLE     �   CREATE TABLE public.desarrollador (
    id_usuario integer NOT NULL,
    email character varying(255) NOT NULL,
    creacion_usuario date NOT NULL
);
 !   DROP TABLE public.desarrollador;
       public         heap    stevecas    false            9           0    0    TABLE desarrollador    ACL     �   GRANT ALL ON TABLE public.desarrollador TO jose;
GRANT ALL ON TABLE public.desarrollador TO laura;
GRANT ALL ON TABLE public.desarrollador TO andre;
          public          stevecas    false    226            �            1259    25389    mi_funcion_id_seq    SEQUENCE     z   CREATE SEQUENCE public.mi_funcion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.mi_funcion_id_seq;
       public          stevecas    false            :           0    0    SEQUENCE mi_funcion_id_seq    ACL     �   GRANT ALL ON SEQUENCE public.mi_funcion_id_seq TO jose;
GRANT ALL ON SEQUENCE public.mi_funcion_id_seq TO laura;
GRANT ALL ON SEQUENCE public.mi_funcion_id_seq TO andre;
          public          stevecas    false    234            �            1259    25186    funcion    TABLE     �   CREATE TABLE public.funcion (
    id_funcion integer DEFAULT nextval('public.mi_funcion_id_seq'::regclass) NOT NULL,
    nombre_funcion character varying NOT NULL
);
    DROP TABLE public.funcion;
       public         heap    stevecas    false    234            ;           0    0    TABLE funcion    ACL     �   GRANT ALL ON TABLE public.funcion TO jose;
GRANT ALL ON TABLE public.funcion TO laura;
GRANT ALL ON TABLE public.funcion TO andre;
          public          stevecas    false    217            �            1259    25207    funciones_rol    TABLE     �   CREATE TABLE public.funciones_rol (
    id_rol integer NOT NULL,
    id_funcion integer NOT NULL,
    fecha_desde date NOT NULL,
    fecha_hasta date NOT NULL,
    estado character varying NOT NULL
);
 !   DROP TABLE public.funciones_rol;
       public         heap    stevecas    false            <           0    0    TABLE funciones_rol    ACL     �   GRANT ALL ON TABLE public.funciones_rol TO jose;
GRANT ALL ON TABLE public.funciones_rol TO laura;
GRANT ALL ON TABLE public.funciones_rol TO andre;
          public          stevecas    false    220            �            1259    25385    mi_log_id_seq    SEQUENCE     v   CREATE SEQUENCE public.mi_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.mi_log_id_seq;
       public          stevecas    false            =           0    0    SEQUENCE mi_log_id_seq    ACL     �   GRANT ALL ON SEQUENCE public.mi_log_id_seq TO jose;
GRANT ALL ON SEQUENCE public.mi_log_id_seq TO laura;
GRANT ALL ON SEQUENCE public.mi_log_id_seq TO andre;
          public          stevecas    false    233            �            1259    25172    log    TABLE     �  CREATE TABLE public.log (
    id_log integer DEFAULT nextval('public.mi_log_id_seq'::regclass) NOT NULL,
    fecha_log date NOT NULL,
    hora_log time without time zone NOT NULL,
    operacion_log character varying NOT NULL,
    dato_nuevo character varying(5000) NOT NULL,
    dato_viejo character varying(5000) NOT NULL,
    tabla_insertada character varying NOT NULL,
    usern character varying NOT NULL
);
    DROP TABLE public.log;
       public         heap    stevecas    false    233            >           0    0 	   TABLE log    ACL     w   GRANT ALL ON TABLE public.log TO jose;
GRANT ALL ON TABLE public.log TO laura;
GRANT ALL ON TABLE public.log TO andre;
          public          stevecas    false    215            �            1259    25259    permiso_archivo    TABLE     �   CREATE TABLE public.permiso_archivo (
    fecha_permiso date NOT NULL,
    id_archivo integer NOT NULL,
    id_usuario integer NOT NULL,
    id_ususario_compartido integer NOT NULL,
    expiracion date NOT NULL
);
 #   DROP TABLE public.permiso_archivo;
       public         heap    stevecas    false            ?           0    0    TABLE permiso_archivo    ACL     �   GRANT ALL ON TABLE public.permiso_archivo TO jose;
GRANT ALL ON TABLE public.permiso_archivo TO laura;
GRANT ALL ON TABLE public.permiso_archivo TO andre;
          public          stevecas    false    229            �            1259    25271    permiso_carpeta    TABLE     �   CREATE TABLE public.permiso_carpeta (
    fecha_permiso date NOT NULL,
    id_carpeta integer NOT NULL,
    id_usuario integer NOT NULL,
    id_ususario_compartido integer NOT NULL,
    expiracion date NOT NULL
);
 #   DROP TABLE public.permiso_carpeta;
       public         heap    stevecas    false            @           0    0    TABLE permiso_carpeta    ACL     �   GRANT ALL ON TABLE public.permiso_carpeta TO jose;
GRANT ALL ON TABLE public.permiso_carpeta TO laura;
GRANT ALL ON TABLE public.permiso_carpeta TO andre;
          public          stevecas    false    231            �            1259    25200    rol    TABLE     d   CREATE TABLE public.rol (
    id_rol integer NOT NULL,
    nombre_rol character varying NOT NULL
);
    DROP TABLE public.rol;
       public         heap    stevecas    false            A           0    0 	   TABLE rol    ACL     w   GRANT ALL ON TABLE public.rol TO jose;
GRANT ALL ON TABLE public.rol TO laura;
GRANT ALL ON TABLE public.rol TO andre;
          public          stevecas    false    219            �            1259    25228 
   roles_user    TABLE     �   CREATE TABLE public.roles_user (
    id_usuario integer NOT NULL,
    id_rol integer NOT NULL,
    fecha_desde date NOT NULL,
    fecha_hasta date NOT NULL,
    estado character varying NOT NULL
);
    DROP TABLE public.roles_user;
       public         heap    stevecas    false            B           0    0    TABLE roles_user    ACL     �   GRANT ALL ON TABLE public.roles_user TO jose;
GRANT ALL ON TABLE public.roles_user TO laura;
GRANT ALL ON TABLE public.roles_user TO andre;
          public          stevecas    false    223            �            1259    25236    sesion    TABLE     z   CREATE TABLE public.sesion (
    id_sesion integer NOT NULL,
    id_usuario integer NOT NULL,
    pid integer NOT NULL
);
    DROP TABLE public.sesion;
       public         heap    stevecas    false            C           0    0    TABLE sesion    ACL     �   GRANT ALL ON TABLE public.sesion TO jose;
GRANT ALL ON TABLE public.sesion TO laura;
GRANT ALL ON TABLE public.sesion TO andre;
          public          stevecas    false    225            �            1259    25235    sesion_id_sesion_seq    SEQUENCE     }   CREATE SEQUENCE public.sesion_id_sesion_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.sesion_id_sesion_seq;
       public          stevecas    false    225            D           0    0    sesion_id_sesion_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.sesion_id_sesion_seq OWNED BY public.sesion.id_sesion;
          public          stevecas    false    224            E           0    0    SEQUENCE sesion_id_sesion_seq    ACL     �   GRANT ALL ON SEQUENCE public.sesion_id_sesion_seq TO jose;
GRANT ALL ON SEQUENCE public.sesion_id_sesion_seq TO laura;
GRANT ALL ON SEQUENCE public.sesion_id_sesion_seq TO andre;
          public          stevecas    false    224            �            1259    25214    tipo    TABLE     g   CREATE TABLE public.tipo (
    id_tipo integer NOT NULL,
    nombre_tipo character varying NOT NULL
);
    DROP TABLE public.tipo;
       public         heap    stevecas    false            F           0    0 
   TABLE tipo    ACL     z   GRANT ALL ON TABLE public.tipo TO jose;
GRANT ALL ON TABLE public.tipo TO laura;
GRANT ALL ON TABLE public.tipo TO andre;
          public          stevecas    false    221            �            1259    25179    ui    TABLE     [   CREATE TABLE public.ui (
    id_ui integer NOT NULL,
    url character varying NOT NULL
);
    DROP TABLE public.ui;
       public         heap    stevecas    false            G           0    0    TABLE ui    ACL     t   GRANT ALL ON TABLE public.ui TO jose;
GRANT ALL ON TABLE public.ui TO laura;
GRANT ALL ON TABLE public.ui TO andre;
          public          stevecas    false    216            �            1259    25193 
   ui_funcion    TABLE     �   CREATE TABLE public.ui_funcion (
    id_funcion integer NOT NULL,
    id_ui integer NOT NULL,
    fecha_desde date NOT NULL,
    fecha_hasta date NOT NULL,
    estado character varying NOT NULL
);
    DROP TABLE public.ui_funcion;
       public         heap    stevecas    false            H           0    0    TABLE ui_funcion    ACL     �   GRANT ALL ON TABLE public.ui_funcion TO jose;
GRANT ALL ON TABLE public.ui_funcion TO laura;
GRANT ALL ON TABLE public.ui_funcion TO andre;
          public          stevecas    false    218            �            1259    25221    usuario    TABLE     �   CREATE TABLE public.usuario (
    id_usuario integer NOT NULL,
    nombre_usuario character varying(255) NOT NULL,
    contrasena character varying(255) NOT NULL,
    active public.active NOT NULL
);
    DROP TABLE public.usuario;
       public         heap    stevecas    false    935            I           0    0    TABLE usuario    ACL     �   GRANT ALL ON TABLE public.usuario TO jose;
GRANT ALL ON TABLE public.usuario TO laura;
GRANT ALL ON TABLE public.usuario TO andre;
          public          stevecas    false    222            �            1259    25357    usuario_id_usuario_seq    SEQUENCE     �   ALTER TABLE public.usuario ALTER COLUMN id_usuario ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.usuario_id_usuario_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          stevecas    false    222            J           0    0    SEQUENCE usuario_id_usuario_seq    ACL     �   GRANT ALL ON SEQUENCE public.usuario_id_usuario_seq TO jose;
GRANT ALL ON SEQUENCE public.usuario_id_usuario_seq TO laura;
GRANT ALL ON SEQUENCE public.usuario_id_usuario_seq TO andre;
          public          stevecas    false    232            �            1259    25254    version    TABLE     �   CREATE TABLE public.version (
    id_version integer NOT NULL,
    id_archivo integer NOT NULL,
    id_usuario integer NOT NULL,
    num_version integer NOT NULL
);
    DROP TABLE public.version;
       public         heap    stevecas    false            K           0    0    TABLE version    ACL     �   GRANT ALL ON TABLE public.version TO jose;
GRANT ALL ON TABLE public.version TO laura;
GRANT ALL ON TABLE public.version TO andre;
          public          stevecas    false    228            :           2604    25239    sesion id_sesion    DEFAULT     t   ALTER TABLE ONLY public.sesion ALTER COLUMN id_sesion SET DEFAULT nextval('public.sesion_id_sesion_seq'::regclass);
 ?   ALTER TABLE public.sesion ALTER COLUMN id_sesion DROP DEFAULT;
       public          stevecas    false    225    224    225                      0    25247    archivo 
   TABLE DATA           �   COPY public.archivo (id_archivo, id_usuario, id_tipo, nombre_archivo, ruta_archivo, creacion_archivo, contenido_archivo) FROM stdin;
    public          stevecas    false    227   ��                 0    25264    carpeta 
   TABLE DATA           i   COPY public.carpeta (id_carpeta, id_usuario, nombre_carpeta, ruta_carpeta, creacion_carpeta) FROM stdin;
    public          stevecas    false    230   �                 0    25242    desarrollador 
   TABLE DATA           L   COPY public.desarrollador (id_usuario, email, creacion_usuario) FROM stdin;
    public          stevecas    false    226   ��                 0    25186    funcion 
   TABLE DATA           =   COPY public.funcion (id_funcion, nombre_funcion) FROM stdin;
    public          stevecas    false    217   �                 0    25207    funciones_rol 
   TABLE DATA           ]   COPY public.funciones_rol (id_rol, id_funcion, fecha_desde, fecha_hasta, estado) FROM stdin;
    public          stevecas    false    220   ��                 0    25172    log 
   TABLE DATA           y   COPY public.log (id_log, fecha_log, hora_log, operacion_log, dato_nuevo, dato_viejo, tabla_insertada, usern) FROM stdin;
    public          stevecas    false    215   �                 0    25259    permiso_archivo 
   TABLE DATA           t   COPY public.permiso_archivo (fecha_permiso, id_archivo, id_usuario, id_ususario_compartido, expiracion) FROM stdin;
    public          stevecas    false    229   @                0    25271    permiso_carpeta 
   TABLE DATA           t   COPY public.permiso_carpeta (fecha_permiso, id_carpeta, id_usuario, id_ususario_compartido, expiracion) FROM stdin;
    public          stevecas    false    231   �                0    25200    rol 
   TABLE DATA           1   COPY public.rol (id_rol, nombre_rol) FROM stdin;
    public          stevecas    false    219   �                0    25228 
   roles_user 
   TABLE DATA           Z   COPY public.roles_user (id_usuario, id_rol, fecha_desde, fecha_hasta, estado) FROM stdin;
    public          stevecas    false    223                   0    25236    sesion 
   TABLE DATA           <   COPY public.sesion (id_sesion, id_usuario, pid) FROM stdin;
    public          stevecas    false    225   _                0    25214    tipo 
   TABLE DATA           4   COPY public.tipo (id_tipo, nombre_tipo) FROM stdin;
    public          stevecas    false    221   �                0    25179    ui 
   TABLE DATA           (   COPY public.ui (id_ui, url) FROM stdin;
    public          stevecas    false    216   �                0    25193 
   ui_funcion 
   TABLE DATA           Y   COPY public.ui_funcion (id_funcion, id_ui, fecha_desde, fecha_hasta, estado) FROM stdin;
    public          stevecas    false    218                   0    25221    usuario 
   TABLE DATA           Q   COPY public.usuario (id_usuario, nombre_usuario, contrasena, active) FROM stdin;
    public          stevecas    false    222   f                0    25254    version 
   TABLE DATA           R   COPY public.version (id_version, id_archivo, id_usuario, num_version) FROM stdin;
    public          stevecas    false    228   �      L           0    0    mi_archivo_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.mi_archivo_id_seq', 9, true);
          public          stevecas    false    235            M           0    0    mi_carpeta_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.mi_carpeta_id_seq', 5, true);
          public          stevecas    false    236            N           0    0    mi_funcion_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.mi_funcion_id_seq', 6, true);
          public          stevecas    false    234            O           0    0    mi_log_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.mi_log_id_seq', 78, true);
          public          stevecas    false    233            P           0    0    sesion_id_sesion_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.sesion_id_sesion_seq', 7, true);
          public          stevecas    false    224            Q           0    0    usuario_id_usuario_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.usuario_id_usuario_seq', 7, true);
          public          stevecas    false    232            T           2606    25253    archivo archivo_pk 
   CONSTRAINT     d   ALTER TABLE ONLY public.archivo
    ADD CONSTRAINT archivo_pk PRIMARY KEY (id_archivo, id_usuario);
 <   ALTER TABLE ONLY public.archivo DROP CONSTRAINT archivo_pk;
       public            stevecas    false    227    227            Z           2606    25270    carpeta carpeta_pk 
   CONSTRAINT     d   ALTER TABLE ONLY public.carpeta
    ADD CONSTRAINT carpeta_pk PRIMARY KEY (id_carpeta, id_usuario);
 <   ALTER TABLE ONLY public.carpeta DROP CONSTRAINT carpeta_pk;
       public            stevecas    false    230    230            R           2606    25246    desarrollador desarrollador_pk 
   CONSTRAINT     d   ALTER TABLE ONLY public.desarrollador
    ADD CONSTRAINT desarrollador_pk PRIMARY KEY (id_usuario);
 H   ALTER TABLE ONLY public.desarrollador DROP CONSTRAINT desarrollador_pk;
       public            stevecas    false    226            B           2606    25192    funcion funcion_pk 
   CONSTRAINT     X   ALTER TABLE ONLY public.funcion
    ADD CONSTRAINT funcion_pk PRIMARY KEY (id_funcion);
 <   ALTER TABLE ONLY public.funcion DROP CONSTRAINT funcion_pk;
       public            stevecas    false    217            H           2606    25213    funciones_rol funciones_rol_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.funciones_rol
    ADD CONSTRAINT funciones_rol_pk PRIMARY KEY (id_rol, id_funcion, fecha_desde, fecha_hasta);
 H   ALTER TABLE ONLY public.funciones_rol DROP CONSTRAINT funciones_rol_pk;
       public            stevecas    false    220    220    220    220            >           2606    25178 
   log log_pk 
   CONSTRAINT     L   ALTER TABLE ONLY public.log
    ADD CONSTRAINT log_pk PRIMARY KEY (id_log);
 4   ALTER TABLE ONLY public.log DROP CONSTRAINT log_pk;
       public            stevecas    false    215            X           2606    25263 "   permiso_archivo permiso_archivo_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.permiso_archivo
    ADD CONSTRAINT permiso_archivo_pk PRIMARY KEY (fecha_permiso, id_archivo, id_usuario, id_ususario_compartido);
 L   ALTER TABLE ONLY public.permiso_archivo DROP CONSTRAINT permiso_archivo_pk;
       public            stevecas    false    229    229    229    229            \           2606    25275 "   permiso_carpeta permiso_carpeta_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.permiso_carpeta
    ADD CONSTRAINT permiso_carpeta_pk PRIMARY KEY (fecha_permiso, id_carpeta, id_usuario, id_ususario_compartido);
 L   ALTER TABLE ONLY public.permiso_carpeta DROP CONSTRAINT permiso_carpeta_pk;
       public            stevecas    false    231    231    231    231            F           2606    25206 
   rol rol_pk 
   CONSTRAINT     L   ALTER TABLE ONLY public.rol
    ADD CONSTRAINT rol_pk PRIMARY KEY (id_rol);
 4   ALTER TABLE ONLY public.rol DROP CONSTRAINT rol_pk;
       public            stevecas    false    219            N           2606    25234    roles_user roles_user_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.roles_user
    ADD CONSTRAINT roles_user_pk PRIMARY KEY (id_usuario, id_rol, fecha_desde, fecha_hasta);
 B   ALTER TABLE ONLY public.roles_user DROP CONSTRAINT roles_user_pk;
       public            stevecas    false    223    223    223    223            P           2606    25241    sesion sesion_pk 
   CONSTRAINT     a   ALTER TABLE ONLY public.sesion
    ADD CONSTRAINT sesion_pk PRIMARY KEY (id_sesion, id_usuario);
 :   ALTER TABLE ONLY public.sesion DROP CONSTRAINT sesion_pk;
       public            stevecas    false    225    225            J           2606    25220    tipo tipo_pk 
   CONSTRAINT     O   ALTER TABLE ONLY public.tipo
    ADD CONSTRAINT tipo_pk PRIMARY KEY (id_tipo);
 6   ALTER TABLE ONLY public.tipo DROP CONSTRAINT tipo_pk;
       public            stevecas    false    221            D           2606    25199    ui_funcion ui_funcion_pk 
   CONSTRAINT        ALTER TABLE ONLY public.ui_funcion
    ADD CONSTRAINT ui_funcion_pk PRIMARY KEY (id_funcion, id_ui, fecha_desde, fecha_hasta);
 B   ALTER TABLE ONLY public.ui_funcion DROP CONSTRAINT ui_funcion_pk;
       public            stevecas    false    218    218    218    218            @           2606    25185    ui ui_pk 
   CONSTRAINT     I   ALTER TABLE ONLY public.ui
    ADD CONSTRAINT ui_pk PRIMARY KEY (id_ui);
 2   ALTER TABLE ONLY public.ui DROP CONSTRAINT ui_pk;
       public            stevecas    false    216            L           2606    25227    usuario usuario_pk 
   CONSTRAINT     X   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pk PRIMARY KEY (id_usuario);
 <   ALTER TABLE ONLY public.usuario DROP CONSTRAINT usuario_pk;
       public            stevecas    false    222            V           2606    25258    version version_pk 
   CONSTRAINT     p   ALTER TABLE ONLY public.version
    ADD CONSTRAINT version_pk PRIMARY KEY (id_version, id_archivo, id_usuario);
 <   ALTER TABLE ONLY public.version DROP CONSTRAINT version_pk;
       public            stevecas    false    228    228    228            v           2620    25438    archivo tr_deletepmsachv    TRIGGER     y   CREATE TRIGGER tr_deletepmsachv BEFORE DELETE ON public.archivo FOR EACH ROW EXECUTE FUNCTION public.delete_permsachv();
 1   DROP TRIGGER tr_deletepmsachv ON public.archivo;
       public          stevecas    false    227    269            y           2620    25415    carpeta tr_deletepmscrp    TRIGGER     v   CREATE TRIGGER tr_deletepmscrp AFTER DELETE ON public.carpeta FOR EACH ROW EXECUTE FUNCTION public.delete_permscrp();
 0   DROP TRIGGER tr_deletepmscrp ON public.carpeta;
       public          stevecas    false    230    270            w           2620    25398    archivo tr_logarchivo    TRIGGER     �   CREATE TRIGGER tr_logarchivo AFTER INSERT OR DELETE OR UPDATE ON public.archivo FOR EACH ROW EXECUTE FUNCTION public.tf_changestable();
 .   DROP TRIGGER tr_logarchivo ON public.archivo;
       public          stevecas    false    271    227            z           2620    25399    carpeta tr_logcarpeta    TRIGGER     �   CREATE TRIGGER tr_logcarpeta AFTER INSERT OR DELETE OR UPDATE ON public.carpeta FOR EACH ROW EXECUTE FUNCTION public.tf_changestable();
 .   DROP TRIGGER tr_logcarpeta ON public.carpeta;
       public          stevecas    false    271    230            n           2620    25388    funcion tr_logfuncion    TRIGGER     �   CREATE TRIGGER tr_logfuncion AFTER INSERT OR DELETE OR UPDATE ON public.funcion FOR EACH ROW EXECUTE FUNCTION public.tf_changestable();
 .   DROP TRIGGER tr_logfuncion ON public.funcion;
       public          stevecas    false    217    271            q           2620    25396     funciones_rol tr_logfuncionesrol    TRIGGER     �   CREATE TRIGGER tr_logfuncionesrol AFTER INSERT OR DELETE OR UPDATE ON public.funciones_rol FOR EACH ROW EXECUTE FUNCTION public.tf_changestable();
 9   DROP TRIGGER tr_logfuncionesrol ON public.funciones_rol;
       public          stevecas    false    271    220            x           2620    25400 $   permiso_archivo tr_logpermisoarchivo    TRIGGER     �   CREATE TRIGGER tr_logpermisoarchivo AFTER INSERT OR DELETE OR UPDATE ON public.permiso_archivo FOR EACH ROW EXECUTE FUNCTION public.tf_changestable();
 =   DROP TRIGGER tr_logpermisoarchivo ON public.permiso_archivo;
       public          stevecas    false    229    271            {           2620    25401 $   permiso_carpeta tr_logpermisocarpeta    TRIGGER     �   CREATE TRIGGER tr_logpermisocarpeta AFTER INSERT OR DELETE OR UPDATE ON public.permiso_carpeta FOR EACH ROW EXECUTE FUNCTION public.tf_changestable();
 =   DROP TRIGGER tr_logpermisocarpeta ON public.permiso_carpeta;
       public          stevecas    false    271    231            p           2620    25392    rol tr_logrol    TRIGGER     �   CREATE TRIGGER tr_logrol AFTER INSERT OR DELETE OR UPDATE ON public.rol FOR EACH ROW EXECUTE FUNCTION public.tf_changestable();
 &   DROP TRIGGER tr_logrol ON public.rol;
       public          stevecas    false    271    219            t           2620    25395    roles_user tr_logrolesuser    TRIGGER     �   CREATE TRIGGER tr_logrolesuser AFTER INSERT OR DELETE OR UPDATE ON public.roles_user FOR EACH ROW EXECUTE FUNCTION public.tf_changestable();
 3   DROP TRIGGER tr_logrolesuser ON public.roles_user;
       public          stevecas    false    271    223            u           2620    25394    sesion tr_logsesion    TRIGGER     �   CREATE TRIGGER tr_logsesion AFTER INSERT OR DELETE OR UPDATE ON public.sesion FOR EACH ROW EXECUTE FUNCTION public.tf_changestable();
 ,   DROP TRIGGER tr_logsesion ON public.sesion;
       public          stevecas    false    271    225            r           2620    25402    tipo tr_logtipo    TRIGGER     �   CREATE TRIGGER tr_logtipo AFTER INSERT OR DELETE OR UPDATE ON public.tipo FOR EACH ROW EXECUTE FUNCTION public.tf_changestable();
 (   DROP TRIGGER tr_logtipo ON public.tipo;
       public          stevecas    false    221    271            m           2620    25391    ui tr_logui    TRIGGER     ~   CREATE TRIGGER tr_logui AFTER INSERT OR DELETE OR UPDATE ON public.ui FOR EACH ROW EXECUTE FUNCTION public.tf_changestable();
 $   DROP TRIGGER tr_logui ON public.ui;
       public          stevecas    false    271    216            o           2620    25397    ui_funcion tr_loguifuncion    TRIGGER     �   CREATE TRIGGER tr_loguifuncion AFTER INSERT OR DELETE OR UPDATE ON public.ui_funcion FOR EACH ROW EXECUTE FUNCTION public.tf_changestable();
 3   DROP TRIGGER tr_loguifuncion ON public.ui_funcion;
       public          stevecas    false    271    218            s           2620    25393    usuario tr_logusuario    TRIGGER     �   CREATE TRIGGER tr_logusuario AFTER INSERT OR DELETE OR UPDATE ON public.usuario FOR EACH ROW EXECUTE FUNCTION public.tf_changestable();
 .   DROP TRIGGER tr_logusuario ON public.usuario;
       public          stevecas    false    271    222            h           2606    25341 *   permiso_archivo archivo_permiso_archivo_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.permiso_archivo
    ADD CONSTRAINT archivo_permiso_archivo_fk FOREIGN KEY (id_archivo, id_usuario) REFERENCES public.archivo(id_archivo, id_usuario);
 T   ALTER TABLE ONLY public.permiso_archivo DROP CONSTRAINT archivo_permiso_archivo_fk;
       public          stevecas    false    227    229    229    3412    227            g           2606    25346    version archivo_version_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.version
    ADD CONSTRAINT archivo_version_fk FOREIGN KEY (id_archivo, id_usuario) REFERENCES public.archivo(id_archivo, id_usuario);
 D   ALTER TABLE ONLY public.version DROP CONSTRAINT archivo_version_fk;
       public          stevecas    false    228    227    227    3412    228            k           2606    25351 *   permiso_carpeta carpeta_permiso_carpeta_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.permiso_carpeta
    ADD CONSTRAINT carpeta_permiso_carpeta_fk FOREIGN KEY (id_usuario, id_carpeta) REFERENCES public.carpeta(id_usuario, id_carpeta);
 T   ALTER TABLE ONLY public.permiso_carpeta DROP CONSTRAINT carpeta_permiso_carpeta_fk;
       public          stevecas    false    231    3418    230    230    231            e           2606    25326     archivo desarrollador_archivo_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.archivo
    ADD CONSTRAINT desarrollador_archivo_fk FOREIGN KEY (id_usuario) REFERENCES public.desarrollador(id_usuario);
 J   ALTER TABLE ONLY public.archivo DROP CONSTRAINT desarrollador_archivo_fk;
       public          stevecas    false    226    227    3410            j           2606    25321     carpeta desarrollador_carpeta_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.carpeta
    ADD CONSTRAINT desarrollador_carpeta_fk FOREIGN KEY (id_usuario) REFERENCES public.desarrollador(id_usuario);
 J   ALTER TABLE ONLY public.carpeta DROP CONSTRAINT desarrollador_carpeta_fk;
       public          stevecas    false    3410    230    226            i           2606    25336 1   permiso_archivo desarrollador_permiso_archivo_fk1    FK CONSTRAINT     �   ALTER TABLE ONLY public.permiso_archivo
    ADD CONSTRAINT desarrollador_permiso_archivo_fk1 FOREIGN KEY (id_ususario_compartido) REFERENCES public.desarrollador(id_usuario);
 [   ALTER TABLE ONLY public.permiso_archivo DROP CONSTRAINT desarrollador_permiso_archivo_fk1;
       public          stevecas    false    226    3410    229            l           2606    25331 1   permiso_carpeta desarrollador_permiso_carpeta_fk1    FK CONSTRAINT     �   ALTER TABLE ONLY public.permiso_carpeta
    ADD CONSTRAINT desarrollador_permiso_carpeta_fk1 FOREIGN KEY (id_ususario_compartido) REFERENCES public.desarrollador(id_usuario);
 [   ALTER TABLE ONLY public.permiso_carpeta DROP CONSTRAINT desarrollador_permiso_carpeta_fk1;
       public          stevecas    false    231    3410    226            _           2606    25281 &   funciones_rol funcion_funciones_rol_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.funciones_rol
    ADD CONSTRAINT funcion_funciones_rol_fk FOREIGN KEY (id_funcion) REFERENCES public.funcion(id_funcion);
 P   ALTER TABLE ONLY public.funciones_rol DROP CONSTRAINT funcion_funciones_rol_fk;
       public          stevecas    false    217    220    3394            ]           2606    25286     ui_funcion funcion_ui_funcion_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.ui_funcion
    ADD CONSTRAINT funcion_ui_funcion_fk FOREIGN KEY (id_funcion) REFERENCES public.funcion(id_funcion);
 J   ALTER TABLE ONLY public.ui_funcion DROP CONSTRAINT funcion_ui_funcion_fk;
       public          stevecas    false    218    3394    217            `           2606    25296 "   funciones_rol rol_funciones_rol_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.funciones_rol
    ADD CONSTRAINT rol_funciones_rol_fk FOREIGN KEY (id_rol) REFERENCES public.rol(id_rol);
 L   ALTER TABLE ONLY public.funciones_rol DROP CONSTRAINT rol_funciones_rol_fk;
       public          stevecas    false    220    3398    219            a           2606    25291    roles_user rol_roles_user_fk    FK CONSTRAINT     |   ALTER TABLE ONLY public.roles_user
    ADD CONSTRAINT rol_roles_user_fk FOREIGN KEY (id_rol) REFERENCES public.rol(id_rol);
 F   ALTER TABLE ONLY public.roles_user DROP CONSTRAINT rol_roles_user_fk;
       public          stevecas    false    219    3398    223            f           2606    25301    archivo tipo_archivo_fk    FK CONSTRAINT     z   ALTER TABLE ONLY public.archivo
    ADD CONSTRAINT tipo_archivo_fk FOREIGN KEY (id_tipo) REFERENCES public.tipo(id_tipo);
 A   ALTER TABLE ONLY public.archivo DROP CONSTRAINT tipo_archivo_fk;
       public          stevecas    false    3402    221    227            ^           2606    25276    ui_funcion ui_ui_funcion_fk    FK CONSTRAINT     x   ALTER TABLE ONLY public.ui_funcion
    ADD CONSTRAINT ui_ui_funcion_fk FOREIGN KEY (id_ui) REFERENCES public.ui(id_ui);
 E   ALTER TABLE ONLY public.ui_funcion DROP CONSTRAINT ui_ui_funcion_fk;
       public          stevecas    false    218    3392    216            d           2606    25306 &   desarrollador usuario_desarrollador_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.desarrollador
    ADD CONSTRAINT usuario_desarrollador_fk FOREIGN KEY (id_usuario) REFERENCES public.usuario(id_usuario);
 P   ALTER TABLE ONLY public.desarrollador DROP CONSTRAINT usuario_desarrollador_fk;
       public          stevecas    false    222    3404    226            b           2606    25316     roles_user usuario_roles_user_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.roles_user
    ADD CONSTRAINT usuario_roles_user_fk FOREIGN KEY (id_usuario) REFERENCES public.usuario(id_usuario);
 J   ALTER TABLE ONLY public.roles_user DROP CONSTRAINT usuario_roles_user_fk;
       public          stevecas    false    223    222    3404            c           2606    25311    sesion usuario_sesion_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.sesion
    ADD CONSTRAINT usuario_sesion_fk FOREIGN KEY (id_usuario) REFERENCES public.usuario(id_usuario);
 B   ALTER TABLE ONLY public.sesion DROP CONSTRAINT usuario_sesion_fk;
       public          stevecas    false    222    3404    225               h  x��I������w���Xu4�d9$GB-�D�������_�h�����і�iu����Gb�ȟ�������w��r��۟��흿��?��w?���۷�|���������x����7_<��݇�')$�S���ٳO{�'�0�����������_m�AF�A����j)�$]��3�Y��G#����#)�d�ʶ`9���[-�LY�e�1S����{[���)��=�fCj�\�J�RuO��g�{�<��P��Qg�:%e���M���8�',aH�Y�ʽE�K{iZ�K�n���W+�
\<�i!�Uf����3.�Csw�s̬�R��ǰ���iҬt�^w��عz�ec�=Jٻ�t�w�X|9H�"�p�Q&t���o�7�*}��d��1O���]����2thLw溚b�3��Y]��*K�����WմV�s��G���Ίy��a��4<�[�-�h5s�Z%�5k��KC�΢���m4#�ҥ�Q�:{�F'k�OwB������f��������B�����*l���4f��Vp��'ҿX�m�rnzީ�#�8���h%u�N"W\%�9�9q��� �6e䡲��p[�NkR
҂�� �`���q��hS��{�Ĩ�j��zp��"u	����	����{YV��m�|��K���cjM'a�@���xm}�8�i�N	b���`�#�|i�ay�\�9�{�gm�r*��8ʐx)R+�JZ;���j�����i���������H�aY0�$Qj{L��f'������KP��&;��1���qpC8�BH#G	�u�{�B�԰�P��C�"���"��y�au�*1�f=��4bO;e����*�����lA ���
*Y}�nh�5�w���
w�΁bV���h�� �	���9�no�ǕS�N�C�W����`�e{�~)M���by+؟`��j�/W.Хm�h娡f�4����:�~Ï~�6g��%KY�{�O��Q��1���J�4������Ebh�.m�G��@v�T{�K�앷�Z�G�*���q�/�|�?�Y�:�
k����M(����}�QZ*���^�[��� �0�;Bh��!��
#�S B�
Y��тzZ�k	��|�=C�1n�eRL�p
�ط�0Je��� �sg���S(	rJ�Y`����Bm}�J�����3{A 6�l]r6ra����.���s�6�шiّ�sx��d�Îh��6�����%�͖��,&���� �4C�����3���G�`�{x��R>�م�P�ũ�:à��5��D�mʆ��!#XQ؏�G@�ݡ�VK׃��%4T��X��du�谐�a�F�u��j�w�d��j�D{pk���x �	�FUYN�c��)��EV��{�D�!
*��"7�R��J��\���L4�}1oO�#4�\Y�1K���"�F��A%����� ؔ��(���W�j#��� �@,�a�#@�;�W�D_3ŘF΋�얐��Z�pk	
�'��C�|Ov��sX3? t��J�.�g�_wzG�ǎ^K��
��Ɉ|�D�����cX�ؗ�໔vF9� �0J��n(��a8��C�*pTň��N��2��p�g$bBg��k�D�&�<6S�np
�6�n���":H3!Q��H6	>�˥�'ǔP3�,�O������	�1"��^s��'.Anp��ݏ8��nC�爄� .��0(n�>A:�I[���l�L5�D�ܛB��W�s~(���ᵾ;�̨
��xw;�w��x�e�!zT?��Kֶ�8��h-�q"y�Y/���n��"H}�� �^�]�o���Z�n�Zh�e4��̛7���Ta>�(�LUh�TTr�'�� ��9A�kU��Jx�S���6ܤ���f`	�2��)����� ���l���M�Ӓ�ƽR��:2̏t��	Iu4 K��!���^
JQN�53Hi%V���a���N.�j�?wQn�1ac���=bJ�� ����i��G�@*c�@>8�H��;�Kὁ���N���9���(h��D�-L�:D��pc����C�x���4��⠰"v�)�	�6$,�5�!�h�MܔfK��6��l������W�1���D����K���	[ 1��,�aQ���Tq��YC��7H	f��� �'?�+p2��pc?�G��"}܋F$�qb�ZA{�k�`��6��K#��&�eT��=�P؁��N	5������ٹ)N7�q��Q�����L>Bs�[�
 iu�Vl\<�"�#g��u'`6w+�Ϫ�?0+�Ju�N�R�I� �1mS$������\r��m��ŭ�]���I"�B��u�NtWlRIO�a��o߿/|���37_<�ks�l���M������{|z�׶)��3.��[����m.��|��o�gв�u������s_4�;�3h�Fw�yF�r������&��T�w��WEmhDsX�|�_f2(�����Pp)��n��=�ҍ��"ydgp�~�	h+�Y�F� ��R=�.V==���v��lM�e�+��c3$$����[ӥ�W���@bt�w�oF��Ô�W?v48�Ȝ#��Z=�;=əg�Ϙ@��p"�$a�18���~��0�<���'?"p���>�{O'�'H�4��MX:���U�
�nt���G0t�g\��y�u�q�g\��y�u�q�g\��y�h�aO�$௯�����+������?���u� �k���U~m Q/s��_�xq����/}z���b�4�x��������׿�^�oM/p������{M/�KAV�l�>�*
;3NUWt�!����G;)-soG���MMk8�`T>-�#Ax(C����I�F��������Ϩ�7�@hu��i���#*�m�~�׀{{�m>�Y�����ocLPp��I8t��))���rH���h�-<O�D���)�7�Qq֬�Q[42 �܍��<L/�7�����~�m����rԧ��qn��/N �+}#�5�g�"\����x�X���l��@�1E��A��/��hˁ7�8��j�@=���G1t�^\����uzq�^\����uzq�^\����hz�쇧O��t��         �   x�3�4�tN,*H-I��+M-K��O.)M*J�����M�/.I-K�w�O.�M�+�/�w,(�Ǯ����D�� ��L��"�q�HN��g �Z�Y�\ƨf��V��iD-�YF�f��1	Y�)<�2K	H<8̸b���� �wN         K   x�3�,-N-*(*MMJ4vH�M���K���4202�5��52�2CRb�]�)�C�J9�KR�R���ɛr��qqq )�)D         n   x�3�t�����K,r�O.�M�+��2�t��-H,*�D4�t.JER�Z����e�&�ZTk��_���ٌ3�4�$�fnJ�cQrFfY>�9� �Ģ�ԒD.�s`"1z\\\ SN:            x��б�0�9�� ��@;�?ؘ�X��FiQDN�pÓ峺� �A�S�c����yu�c hXu�I��O`}��� ���|��(�S�m �/ �2��p��2`�50��7�։            x���n\ّ���cxeY�3��Z�a��v���m�(p(�����I%�V�a_�
Le�='�����Q����&��|�ҩr뤬������ۿ�r�۰����U����çrqu���h�8�����oW�O���vv����j�:Z�|e�5���So�������f��s�o��:�t�p�=�x��e|�:�x�w�u�֮��ɦ-�������zԢW?���y��0>^�_�������7�߹ԫ�eE��y}Rn>}����;{��:xe��v�WfW����y̳*\_��O7;yv���>���vQ�h�ph�g�-6�V �+�Nf�A�p�x������w���F��҉��^���Ƅl��֐8������Zߋ��Diq�I��K�>�f��j�՛�o6�o�}��O��ܤ�9`}��j� b������o�����f_'jNXm�CX�J?�O����ًԺ;�kT���i�Ƈʎ�('�ή�_���1_���Q͜*EQ[e��$��=�w�[��M�SG�kIt��B�Mn�\.�ǿ���v}uvq������ݕ�~���,�5N;��R.u^{����[0�O���o
ٛ��֟�_~>��+W�UN;u�'����]�iՒ���ꛟ�?Tpa�U4aF��A�S�S衹���6c9ƹɪ#���Se�Q�;T˱�d��U��!��b��4{���R�2�V|j���O)1�[v��.4ƈnKּg�.!���SmĜ��=��
l\�!��kֶ��l��V�-#�V��Ø<r�5&�Sn��
���xU�M#�kӳ�0gZ�:��E��싥:{2��3���'�kye���p�:��Xg*����U[���.�G��⛢f�!�^u���r�n�J�~��ٕrƏhfls�8T,���JH,�MjR�cV�������*����;���7%�bZo=vkGFK� I��6d�3�O��-�r�.���i͹P��FI��(ް֎�Z!�����oLnR�X��a��K.��h�h���bFQ�����n�֝�1��F�b�:�l5���F�3��uT혾��qt3�f�Kd�5��9��׼���T��d�A�hj�f�9x�vg&X�l�N���ց��3V?��^�:�H�(2�EQ��3	���qE��DJÙ.������(����}�5�^l�.b�B(�Y�!HzI�P�ޤ)n�����n虼�>%Vb�.��"a��*qYsP}'�W�l!F���V�����c��)e7��Qz�d ��P�T0��E�ʜ�)U
YL{Oh*EN���5�l�S�RUɑ��5�󍕪.fKI*�z�!��C+Z�@��)��UWTf��S£���������}A!m}tڄ�S"����5l ��EwkHE����ga�8˖���$�\S��lԪ���K��ٳc�e��z��J��j��ܩ�#�o�
��'yU�:g]��v��k�X���+XDךG3�O
i��9�r�J����f�l������nv;c�}����ܔ�_�}r��T��B�Q�����Ev�~�}7( &�8{��� �)�i�X�Ѿ���2�5��J i�dH�ҥgMx��p��cXJ��$}h$S��蜃u����7��xj0m� ��2OEU��tC�)�M��1*��4��4�$&ct�cf���Z[.�Y�'���[iG�"G����G��.Ѣ4JQ>�]���6�ʓ�b��R�L���h���3T�9ix�o�Tl����|��Pl��#5p����*G��A�jS���1c㜧�%�=��Ny�k����r
�K��T�:�Κ�=^mZ�P�5�A�N}R ӌ��I�����r/�p`BD��bB�kL]�>^Bm�����H7G(m��+�z��!Rڛ������7�/YR	\���8C�(`z������%Iٺuj����g� �)W�;bl&u�j6�B����J7�Q�H�����!Ԫ����ZI9����:���}�hm*�5Og*e�Kx�����1����G)�|�n���>�	�ِ)@G�Y'�3���f]�l��:�H�&vE�)&byE����Rn|LU���DA���s ��I������#j( ��L�B��Q�(.)2����E�2a���1p8��\BI��a��L$HM牴Uf� ��7�ŏY�d��hZ�q6���}��DYsL�wSg�O�e�>F�?z�
�F�'+͚�?{H���a��9%��!�-S=OXj9/H�Jr�H�<�W�r��O��6&<��38o���d�B�9�Sb�m��Z�cZ�
ٛyw��F�����@�Q����l�6]Սa�^ˈAs��1�P�B�Ea/sJ��-�PF�(ΐ�6H�흲k#-��(h��'�o6O$��DW��$O��	Q��4]7��A��jS��cH��D�a')2{2�P%"�)\�������dtR5�8	rM��~kz��Ŗ�")lPG�o�0�2u��T�2C=���LX�M�@��i9F�R7�b����@�ҋ����LOy�luH3%ϼ#D� ׈�̀��14�D���%P|̤�y�7Ff"���tdE�H�b�!����r�
�$ۡ@�Y�i��4��h2�qe�e�LN�	�Q$��sG6�?X��(�
�"dD���	��l��X�ւ�c�� "�yFn�=u<h �5�e� &.x�E�(k���I�m�@2��J��L���iH�:j2�ӵb~��K�>��){�86�[Q�(�	��|ޘ���8���5-�(�61ސ����'�nJ���g�0LJtS]x�4e��<�T�� >�� ����L�J���lQ	؝�3�iQ/��K�(`��Ĭ-�M��A$*�U)J6J���bG+A�]�m|��#��TϴHK�*��ĉ�Ɏשv��Ę�<�w�s�өqkfq&���o������v<ytC�����o����w��t�(f�&���Q�=�O��>&�W�H>�(� La�JRc��{�tV%:0�%�0w`���
���Jz�+)��	V�k@V-�D��kYutF*S&�%�Zg��b-�e��PtP�X��"?���JJ�u�5fuf��̰4��7+ʞ���,Re�f�%���	'ݰ� ��A�24�N�Rh ��)�?7���dF{���щC0$5�pLj
���I���R�i��d@�5�#M���!�$C�0H�*$e.��f,Ҩ�D���@c���ΤG�;tg�g�l����=X؃�=X؃�=X؃�=X؃�=X؃�=��`�:d�_c2�xy�B#,4�B#,4�B#,4�B#,4�B#,4�B#,4�B#,4�B#�����>d�_kGp�C��{��s��9��۵tka4�?�r�	��	�1��T������n7?X}K��>�4.>�]��;���e�S��`2�E��̰��_�\�K����N7�����ܩK�L_7��/���k�H˽,˽,˽,���H���H���H���H���H�t���N�Z
 �����H��َx�����=k�P��'��S�.�q�W?]�r�S��4��S����,�Voߟ}8�������A�T	��h�v�⳵O^�ۗ?���'um�z}��P�>FD�&f_�?UzM=#�����D��Eܮ?.�]��ߒb���M�;F��ֽ��|�^¾�t��Hqʜ��Ͽ�Q2Ҭ�X>�}�~_������&�6O������ޗ�A��.�Yخ�)��L��<
�nI��d�[R�S������~��c���H2���{��~��X��O�/�������1�������2��}++l�2���r�	������c�`_��L�!�ʊ[�������3]�/�h�a˄�|܄�Y�P�~�?*#��?a�Gmz(e?��W�	�=j�C)��n�y~k�خ'zu[����z�Z��g���,�L�z��a���n����~a�Vڋ���(u��įV����_�X-�[]� ��L��3(�������U�9��%���խ��ĝ}Q���X�{�� �i�bL�l, � ��p�Z/Čc��(߁Kѧ��g� �DYӀ��u#��@i G6GJ�L �%<�0 �   g�8��
8
�]qA@NXp�P��
�Ƹl:��l.m�9��^j�~J�
��PAj� 4�u��� ���b��;��3Lv*�0�i��pB�$�)�!	��ځoĎ�`?	$`���z@��M2��7R�e5�E�@ I.*F�j�Ā�>N|_FI��AL���9P	�e��<���a�>A�pwR��&�
VR��ZNJ,'%���I���rRb9)���XNJ,'%���*'%�y�K�{\��BR'ܤw���^ׯ��>��I�jy���{"�֯{�ac.�p�:��Y�+���uZ�dC�W������Ƈ��c}��}�ho��J�>�u|�G�毿]S�`՗/�v_D���Sŕ~T��~�����ӧE���TNO�5�)�f���<��<����ֲ;_����a4�:��Ԫ5������ڿ�%W-�+������1��]U~y��ǩ�Q�쪂�g9Nnڗ��e�P)�3�/�GO�3�%0�o9�) ����o��\�w7�^�뇃�"Y���5Kyt��n�1���o�ݜUy٣"v~�>Tq���H�;�z�/��;��u�g�T��z�#�;۝��Q�pF= 4����i�YyZCLlN0e3�;����(bx���m�hG>T�]�][J� � ���(�h�	�{/b;�
14)݃o�����.M�`�L�*;e��6�a ���į���:��$ݝ����	�`��q��D���1�[�U��D9!ƄT��cW2������@��R=�R8�{��"�wFk5[��P��3��c�~b���n���`�	8���31������������������������&�zЇd�\��@��c�cع�_�/3����am@%�J��볏�M�ݓ�p�� m�1n��UG<�!�}n�{��9l]!7�ipy�1�kP_�}��ey@��Mn]���]v�Y��i��IM��Id$3[�P��_�}���/n�Iع
;�Ӓ~�h��d�/�v���ت[57/�Kgk_�
r��;��yK�.;�q�<0��C�����e�m0����C>N��&)Q'�|�}����;^(�'�~�{���[/^(��K��֎r��b�����y�f���������Uz/��*�ě��_E���kcr~�,��.�ʈy��߮�UJ�ܕBày�-���_v�,���U�>3�½O��_h�2��v�a�c:T��o����&��@�wJU�������ޫ2��{�^���}'S�C}�y0^e&M�悽�pJ�#���sv��svd��̭�)"Y_"�m�*z�'Zb�l���P���YT��PN��8������4����Ep�WkswA;�n�����`��y^su�,���奅YΌ�4�F8z4b7	���@z'v�*��&��f�8��M���w�;�\��s˽���o��>�N7O�a��Ԏ�_\6�y�������^���I$�aJQ.b����)w5v�w���d{˽�5���Dl<C��p���p���p���p���p���o½�m��ի�Lb�         M   x�U���0�7�BnH���sԊ�J�_>pg$8)�E���&m~�[ҖTq��G7��4O���X�s���&            x������ � �         H   x�3�tL����,.)JL�/�2��M��,(��\sRsS�J򋹌9��s�J2s3A"\&puE0�"�=... �']         =   x�3�4�4202�5��521M�L��̲|.sNc�c� �����3N�
b���� j�         7   x�Eȹ  ����.�?O��tA����\JR��x�t�-Fm��F� �            x�3�t�HN��2�I�(������ >�7         -   x�3�tN�M�L,�2�t��-H,*�,�2�tM�L�������� ��
�         F   x�3�4�4202�5��521͡L��̲|.NC�
���+0"d�!!0�@Q aB�R���� S�0�         U   x�%�K
�0E���b�~��K��DD�Q�o��ýv�k5��$��#�)|��X򏌣>��daJ1���zn����!q�Lιdy�            x������ � �     
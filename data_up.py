
// Crear Usuarios
CREATE (u1:Usuario {nombre_usuario: "steve", contrasena: "486579"});
CREATE (u2:Usuario {nombre_usuario: "andre", contrasena: "135792468"});
CREATE (u3:Usuario {nombre_usuario: "laura", contrasena: "987654321"});

// Crear Roles
CREATE (r1:Rol {nombre_rol: 'Administrador', description: 'Acceso completo a todas las funciones y UIs'});
CREATE (r2:Rol {nombre_rol: 'ManipuladorElementos', description: 'Puede crear y eliminar archivos'});
CREATE (r3:Rol {nombre_rol: 'ManipuladorExtrem', description: 'Puede crear, eliminar archivos y compartir elementos'});

// Relacionar Usuarios con Roles
MATCH (steve:Usuario {nombre_usuario: "steve"}), (admin:Rol {nombre_rol: 'Administrador'})
CREATE (steve)-[:TIENE_ROL {Active: 'Yes'}]->(admin);

MATCH (laura:Usuario {nombre_usuario: "laura"}), (manipElementos:Rol {nombre_rol: 'ManipuladorElementos'})
CREATE (laura)-[:TIENE_ROL {Active: 'Yes'}]->(manipElementos);

MATCH (andre:Usuario {nombre_usuario: "andre"}), (manipExtrem:Rol {nombre_rol: 'ManipuladorExtrem'})
CREATE (andre)-[:TIENE_ROL {Active: 'Yes'}]->(manipExtrem);

// Crear Funciones
CREATE (f1:Function {nombre_funcion: 'Crear', description: 'Permite crear nuevos elementos'});
CREATE (f2:Function {nombre_funcion: 'Eliminar', description: 'Permite eliminar elementos'});
CREATE (f3:Function {nombre_funcion: 'Compartir', description: 'Permite compartir elementos con otros usuarios'});
CREATE (f4:Function {nombre_funcion: 'Editar', description: 'Permite editar elementos existentes'});
CREATE (f5:Function {nombre_funcion: 'Cambiar', description: 'Permite cambiar configuraciones o atributos de elementos'});

// Relacionar Roles con Funciones con atributo Active
UNWIND [
    {rol: 'Administrador', funciones: ['Crear', 'Eliminar', 'Compartir', 'Editar', 'Cambiar']},
    {rol: 'ManipuladorElementos', funciones: ['Crear', 'Eliminar', 'Editar', 'Cambiar']},
    {rol: 'ManipuladorExtrem', funciones: ['Crear', 'Eliminar', 'Compartir']}
] AS relacion

MATCH (r:Rol {nombre_rol: relacion.rol})
UNWIND relacion.funciones AS funcion_nombre
MATCH (f:Function {nombre_funcion: funcion_nombre})
CREATE (r)-[:TIENE_FUNCION {Active: 'Yes'}]->(f);  

// Crear Interfaces de Usuario (UI)
CREATE (ui1:UI {nombre_ui: 'Edición', description: 'Interfaz para edición de elementos'});
CREATE (ui2:UI {nombre_ui: 'Compartir', description: 'Interfaz para compartir elementos'});
CREATE (ui3:UI {nombre_ui: 'Cambiar', description: 'Interfaz para cambiar configuraciones'});
CREATE (ui4:UI {nombre_ui: 'Administración', description: 'Interfaz para administrar el sistema'});

// Relacionar Funciones con UIs basándose en sus nombres
MATCH (f1:Function {nombre_funcion: 'Crear'})
MATCH (ui1:UI {nombre_ui: 'Edición'})
CREATE (f1)-[:PERTENECE_UI {Active: 'Yes'}]->(ui1);

MATCH (f2:Function {nombre_funcion: 'Eliminar'})
MATCH (ui1:UI {nombre_ui: 'Edición'})
CREATE (f2)-[:PERTENECE_UI {Active: 'Yes'}]->(ui1);

MATCH (f4:Function {nombre_funcion: 'Editar'})
MATCH (ui1:UI {nombre_ui: 'Edición'})
CREATE (f4)-[:PERTENECE_UI {Active: 'Yes'}]->(ui1);

MATCH (f3:Function {nombre_funcion: 'Compartir'})
MATCH (ui2:UI {nombre_ui: 'Compartir'})
CREATE (f3)-[:PERTENECE_UI {Active: 'Yes'}]->(ui2);

MATCH (f5:Function {nombre_funcion: 'Cambiar'})
MATCH (ui3:UI {nombre_ui: 'Cambiar'})
CREATE (f5)-[:PERTENECE_UI {Active: 'Yes'}]->(ui3);

// Crear Tipos de Archivos
CREATE (t1:Tipo {nombre_tipo: 'Texto'});
CREATE (t2:Tipo {nombre_tipo: 'Excel'});

// Crear Archivos
CREATE (a1:Archivo {nombre_archivo: 'Texto_Diciembre', ruta_archivo: '/home/steve/Documentos_App/Diciembre/Texto_Diciembre.txt', creacion_archivo: date('2023-12-01'), contenido_archivo: 'Contenido del archivo 1'});
CREATE (a2:Archivo {nombre_archivo: 'Apuntes_General', ruta_archivo: '/home/steve/Documentos_App/Apuntes/Apuntes_General.txt', creacion_archivo: date('2023-12-02'), contenido_archivo: 'Contenido del archivo 2'});
CREATE (a3:Archivo {nombre_archivo: 'Lugares_Aulas', ruta_archivo: '/home/steve/Documentos_App/Aulas/Lugares_Aulas.txt', creacion_archivo: date('2023-12-03'), contenido_archivo: 'Contenido del archivo 3'});
CREATE (a4:Archivo {nombre_archivo: 'Nombres_Estudiantes', ruta_archivo: '/home/steve/Documentos_App/General/Nombres_Estudiantes.txt', creacion_archivo: date('2023-12-04'), contenido_archivo: 'Contenido del archivo 4'});
CREATE (a5:Archivo {nombre_archivo: 'Archivo_Borrar', ruta_archivo: '/home/steve/Documentos_App/General/Archivo_Borrar.txt', creacion_archivo: date('2023-12-05'), contenido_archivo: 'Contenido del archivo 5'});
CREATE (a6:Archivo {nombre_archivo: 'Importante', ruta_archivo: '/home/steve/Documentos_App/General/Importante.txt', creacion_archivo: date('2023-12-06'), contenido_archivo: 'Contenido del archivo 6'});
CREATE (a7:Archivo {nombre_archivo: 'Indicaciones_Codigo', ruta_archivo: '/home/steve/Documentos_App/Semestre5/Indicaciones_Codigo.txt', creacion_archivo: date('2023-12-07'), contenido_archivo: 'Contenido del archivo 7'});
CREATE (a8:Archivo {nombre_archivo: 'Bad_Smells', ruta_archivo: '/home/steve/Documentos_App/Semestre5/Bad_Smells.txt', creacion_archivo: date('2023-12-08'), contenido_archivo: 'Contenido del archivo 8'});
CREATE (a9:Archivo {nombre_archivo: 'Texto_Movible', ruta_archivo: '/home/steve/Documentos_App/Semestre5/Texto_Movible.txt', creacion_archivo: date('2023-12-09'), contenido_archivo: 'Contenido del archivo 9'});
CREATE (a10:Archivo {nombre_archivo: 'Apuntes_Base1', ruta_archivo: '/home/steve/Documentos_App/Semestre5/Apuntes_Base1.txt', creacion_archivo: date('2023-12-10'), contenido_archivo: 'Contenido del archivo 10'});
CREATE (a11:Archivo {nombre_archivo: 'Apuntes_Base2', ruta_archivo: '/home/steve/Documentos_App/Semestre5/Apuntes_Base2.txt', creacion_archivo: date('2023-12-11'), contenido_archivo: 'Contenido del archivo 11'});
CREATE (a12:Archivo {nombre_archivo: 'Apuntes_TBD', ruta_archivo: '/home/steve/Documentos_App/Documentos_Texto/Apuntes_TBD.txt', creacion_archivo: date('2023-12-12'), contenido_archivo: 'Contenido del archivo 12'});
CREATE (a13:Archivo {nombre_archivo: 'Apuntes_ASO', ruta_archivo: '/home/steve/Documentos_App/Documentos_Texto/Apuntes_ASO.txt', creacion_archivo: date('2023-12-13'), contenido_archivo: 'Contenido del archivo 13'});
CREATE (a14:Archivo {nombre_archivo: 'Apuntes_Redes', ruta_archivo: '/home/steve/Documentos_App/Documentos_Texto/Apuntes_Redes.txt', creacion_archivo: date('2023-12-14'), contenido_archivo: 'Contenido del archivo 14'});
CREATE (a15:Archivo {nombre_archivo: 'Apuntes_TSO', ruta_archivo: '/home/steve/Documentos_App/Documentos_Texto/Apuntes_TSO.txt', creacion_archivo: date('2023-12-15'), contenido_archivo: 'Contenido del archivo 15'});
CREATE (a16:Archivo {nombre_archivo: 'Notas_TSO', ruta_archivo: '/home/steve/Documentos_App/Documentos_Texto/Notas_TSO.xlsx', creacion_archivo: date('2023-12-16'), contenido_archivo: 'Contenido del archivo 16'});
CREATE (a17:Archivo {nombre_archivo: 'Notas_Redes', ruta_archivo: '/home/steve/Documentos_App/Documentos_Texto/Notas_Redes.xlsx', creacion_archivo: date('2023-12-17'), contenido_archivo: 'Contenido del archivo 17'});
CREATE (a18:Archivo {nombre_archivo: 'Puntos_Participacion', ruta_archivo: '/home/steve/Documentos_App/Documentos_Texto/Puntos_Participacion.xlsx', creacion_archivo: date('2023-12-18'), contenido_archivo: 'Contenido del archivo 18'});
CREATE (a19:Archivo {nombre_archivo: 'Lista_Materias', ruta_archivo: '/home/steve/Documentos_App/Documentos_Texto/Lista_Materias.xlsx', creacion_archivo: date('2023-12-19'), contenido_archivo: 'Contenido del archivo 19'});
CREATE (a20:Archivo {nombre_archivo: 'Precios_Laptops', ruta_archivo: '/home/steve/Documentos_App/Documentos_Texto/Precios_Laptops.xlsx', creacion_archivo: date('2023-12-20'), contenido_archivo: 'Contenido del archivo 20'});


UNWIND [
    {tipo: 'Texto', archivos: ['Texto_Diciembre', 'Apuntes_General', 'Lugares_Aulas', 'Nombres_Estudiantes', 'Archivo_Borrar', 'Importante', 'Indicaciones_Codigo', 'Bad_Smells', 'Texto_Movible', 'Apuntes_Base1', 'Apuntes_Base2', 'Apuntes_TBD', 'Apuntes_ASO', 'Apuntes_Redes', 'Apuntes_TSO']},
    {tipo: 'Excel', archivos: ['Notas_TSO', 'Notas_Redes', 'Puntos_Participacion', 'Lista_Materias', 'Precios_Laptops']}
] AS relax
MATCH (t:Tipo {nombre_tipo: relax.tipo})
UNWIND relax.archivos AS archivo
MATCH (a:Archivo {nombre_archivo: archivo})
MERGE (a)-[r:ES_TIPO]->(t)
ON CREATE SET r.Active = 'Yes';

UNWIND [
    {usuario: 'steve', archivos: ['Texto_Diciembre', 'Apuntes_General', 'Lugares_Aulas', 'Nombres_Estudiantes', 'Archivo_Borrar', 'Importante', 'Indicaciones_Codigo', 'Bad_Smells', 'Texto_Movible', 'Apuntes_Base1']},
    {usuario: 'laura', archivos: ['Apuntes_Base2', 'Apuntes_TBD', 'Apuntes_ASO', 'Apuntes_Redes', 'Apuntes_TSO', 'Notas_TSO']},
    {usuario: 'andre', archivos: ['Notas_Redes', 'Puntos_Participacion', 'Lista_Materias', 'Precios_Laptops']}
] AS relacion
MATCH (u:Usuario {nombre_usuario: relacion.usuario})
UNWIND relacion.archivos AS archivo
MATCH (a:Archivo {nombre_archivo: archivo})
CREATE (u)-[:POSEE {Active: 'Yes'}]->(a);

CREATE (p1:Permiso {fecha_inicio: date('2023-12-01'), fecha_expiracion: date('2023-12-10')});
CREATE (p2:Permiso {fecha_inicio: date('2023-12-02'), fecha_expiracion: date('2023-12-11')});
CREATE (p3:Permiso {fecha_inicio: date('2023-12-03'), fecha_expiracion: date('2023-12-12')});
CREATE (p4:Permiso {fecha_inicio: date('2023-12-04'), fecha_expiracion: date('2023-12-13')});
CREATE (p5:Permiso {fecha_inicio: date('2023-12-05'), fecha_expiracion: date('2023-12-14')});
CREATE (p6:Permiso {fecha_inicio: date('2023-12-06'), fecha_expiracion: date('2023-12-15')});
CREATE (p7:Permiso {fecha_inicio: date('2023-12-07'), fecha_expiracion: date('2023-12-16')});
CREATE (p8:Permiso {fecha_inicio: date('2023-12-08'), fecha_expiracion: date('2023-12-17')});
CREATE (p9:Permiso {fecha_inicio: date('2023-12-09'), fecha_expiracion: date('2023-12-18')});

MATCH (u_origen:Usuario {nombre_usuario: 'steve'}),
      (u_destino:Usuario {nombre_usuario: 'laura'}),
      (a:Archivo {nombre_archivo: 'Texto_Diciembre'}),
      (p:Permiso {fecha_inicio: date('2023-12-01'), fecha_expiracion: date('2023-12-10')})
MERGE (u_origen)-[:COMPARTE {Active: 'Yes'}]->(p)
MERGE (p)-[:A_USUARIO]->(u_destino)
MERGE (p)-[:DE_ARCHIVO]->(a);

MATCH (u_origen:Usuario {nombre_usuario: 'steve'}),
      (u_destino:Usuario {nombre_usuario: 'laura'}),
      (a:Archivo {nombre_archivo: 'Apuntes_General'}),
      (p:Permiso {fecha_inicio: date('2023-12-02'), fecha_expiracion: date('2023-12-11')})
MERGE (u_origen)-[:COMPARTE {Active: 'Yes'}]->(p)
MERGE (p)-[:A_USUARIO]->(u_destino)
MERGE (p)-[:DE_ARCHIVO]->(a);

MATCH (u_origen:Usuario {nombre_usuario: 'steve'}),
      (u_destino:Usuario {nombre_usuario: 'laura'}),
      (a:Archivo {nombre_archivo: 'Lugares_Aulas'}),
      (p:Permiso {fecha_inicio: date('2023-12-03'), fecha_expiracion: date('2023-12-12')})
MERGE (u_origen)-[:COMPARTE {Active: 'Yes'}]->(p)
MERGE (p)-[:A_USUARIO]->(u_destino)
MERGE (p)-[:DE_ARCHIVO]->(a);

MATCH (u_origen:Usuario {nombre_usuario: 'steve'}),
      (u_destino:Usuario {nombre_usuario: 'laura'}),
      (a:Archivo {nombre_archivo: 'Nombres_Estudiantes'}),
      (p:Permiso {fecha_inicio: date('2023-12-04'), fecha_expiracion: date('2023-12-13')})
MERGE (u_origen)-[:COMPARTE {Active: 'Yes'}]->(p)
MERGE (p)-[:A_USUARIO]->(u_destino)
MERGE (p)-[:DE_ARCHIVO]->(a);

MATCH (u_origen:Usuario {nombre_usuario: 'steve'}),
      (u_destino:Usuario {nombre_usuario: 'andre'}),
      (a:Archivo {nombre_archivo: 'Archivo_Borrar'}),
      (p:Permiso {fecha_inicio: date('2023-12-05'), fecha_expiracion: date('2023-12-14')})
MERGE (u_origen)-[:COMPARTE {Active: 'Yes'}]->(p)
MERGE (p)-[:A_USUARIO]->(u_destino)
MERGE (p)-[:DE_ARCHIVO]->(a);

MATCH (u_origen:Usuario {nombre_usuario: 'steve'}),
      (u_destino:Usuario {nombre_usuario: 'andre'}),
      (a:Archivo {nombre_archivo: 'Importante'}),
      (p:Permiso {fecha_inicio: date('2023-12-06'), fecha_expiracion: date('2023-12-15')})
MERGE (u_origen)-[:COMPARTE {Active: 'Yes'}]->(p)
MERGE (p)-[:A_USUARIO]->(u_destino)
MERGE (p)-[:DE_ARCHIVO]->(a);

MATCH (u_origen:Usuario {nombre_usuario: 'steve'}),
      (u_destino:Usuario {nombre_usuario: 'andre'}),
      (a:Archivo {nombre_archivo: 'Indicaciones_Codigo'}),
      (p:Permiso {fecha_inicio: date('2023-12-07'), fecha_expiracion: date('2023-12-16')})
MERGE (u_origen)-[:COMPARTE {Active: 'Yes'}]->(p)
MERGE (p)-[:A_USUARIO]->(u_destino)
MERGE (p)-[:DE_ARCHIVO]->(a);

MATCH (u_origen:Usuario {nombre_usuario: 'andre'}),
      (u_destino:Usuario {nombre_usuario: 'steve'}),
      (a:Archivo {nombre_archivo: 'Bad_Smells'}),
      (p:Permiso {fecha_inicio: date('2023-12-08'), fecha_expiracion: date('2023-12-17')})
MERGE (u_origen)-[:COMPARTE {Active: 'Yes'}]->(p)
MERGE (p)-[:A_USUARIO]->(u_destino)
MERGE (p)-[:DE_ARCHIVO]->(a);

MATCH (u_origen:Usuario {nombre_usuario: 'andre'}),
      (u_destino:Usuario {nombre_usuario: 'laura'}),
      (a:Archivo {nombre_archivo: 'Texto_Movible'}),
      (p:Permiso {fecha_inicio: date('2023-12-09'), fecha_expiracion: date('2023-12-18')})
MERGE (u_origen)-[:COMPARTE {Active: 'Yes'}]->(p)
MERGE (p)-[:A_USUARIO]->(u_destino)
MERGE (p)-[:DE_ARCHIVO]->(a);


CREATE (c1:Carpeta {nombre_carpeta: 'Diciembre', ruta_carpeta: '/home/steve/Documentos_App/Diciembre', creacion_carpeta: date('2023-12-01')});
CREATE (c2:Carpeta {nombre_carpeta: 'Apuntes', ruta_carpeta: '/home/steve/Documentos_App/Apuntes', creacion_carpeta: date('2023-12-02')});
CREATE (c3:Carpeta {nombre_carpeta: 'Aulas', ruta_carpeta: '/home/steve/Documentos_App/Aulas', creacion_carpeta: date('2023-12-03')});
CREATE (c4:Carpeta {nombre_carpeta: 'General', ruta_carpeta: '/home/steve/Documentos_App/General', creacion_carpeta: date('2023-12-04')});
CREATE (c5:Carpeta {nombre_carpeta: 'Semestre5', ruta_carpeta: '/home/steve/Documentos_App/Semestre5', creacion_carpeta: date('2023-12-05')});

UNWIND [
    {carpeta: 'Diciembre', archivos: ['Texto_Diciembre']},
    {carpeta: 'Apuntes', archivos: ['Apuntes_General']},
    {carpeta: 'Aulas', archivos: ['Lugares_Aulas']},
    {carpeta: 'General', archivos: ['Nombres_Estudiantes', 'Archivo_Borrar', 'Importante']},
    {carpeta: 'Semestre5', archivos: ['Indicaciones_Codigo', 'Bad_Smells', 'Texto_Movible', 'Apuntes_Base1', 'Apuntes_Base2']}
] AS relacion

MATCH (c:Carpeta {nombre_carpeta: relacion.carpeta})
UNWIND relacion.archivos AS archivo
MATCH (a:Archivo {nombre_archivo: archivo})

MERGE (c)-[:CONTIENE {Active: 'Yes'}]->(a);

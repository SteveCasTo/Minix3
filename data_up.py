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

// Relacionar Funciones con Roles
MATCH (admin:Rol {nombre_rol: 'Administrador'})
MATCH (crear:Function)
WHERE crear.nombre_funcion IN ['Crear', 'Eliminar', 'Compartir', 'Editar', 'Cambiar']
CREATE (admin)-[:TIENE_FUNCION {Active: 'Yes'}]->(crear);

MATCH (admin:Rol {nombre_rol: 'Administrador'})
MATCH (crear:Function)
WHERE crear.nombre_funcion IN ['Crear', 'Eliminar', 'Editar', 'Cambiar']
CREATE (admin)-[:TIENE_FUNCION {Active: 'Yes'}]->(crear);

MATCH (admin:Rol {nombre_rol: 'Administrador'})
MATCH (crear:Function)
WHERE crear.nombre_funcion IN ['Crear', 'Eliminar', 'Compartir']
CREATE (admin)-[:TIENE_FUNCION {Active: 'Yes'}]->(crear);

// Crear Tipos de Archivos
CREATE (t1:Tipo {nombre_tipo: 'Texto'});
CREATE (t2:Tipo {nombre_tipo: 'Excel'});

// Crear Archivos
CREATE (a1:Archivo {nombre_archivo: 'Archivo1', ruta_archivo: '/ruta/archivo1.txt', creacion_archivo: date('2023-12-01'), contenido_archivo: 'Contenido del archivo 1'});
CREATE (a2:Archivo {nombre_archivo: 'Archivo2', ruta_archivo: '/ruta/archivo2.txt', creacion_archivo: date('2023-12-02'), contenido_archivo: 'Contenido del archivo 2'});
CREATE (a3:Archivo {nombre_archivo: 'Archivo3', ruta_archivo: '/ruta/archivo3.txt', creacion_archivo: date('2023-12-03'), contenido_archivo: 'Contenido del archivo 3'});
CREATE (a4:Archivo {nombre_archivo: 'Archivo4', ruta_archivo: '/ruta/archivo4.txt', creacion_archivo: date('2023-12-04'), contenido_archivo: 'Contenido del archivo 4'});
CREATE (a5:Archivo {nombre_archivo: 'Archivo5', ruta_archivo: '/ruta/archivo5.txt', creacion_archivo: date('2023-12-05'), contenido_archivo: 'Contenido del archivo 5'});
CREATE (a6:Archivo {nombre_archivo: 'Archivo6', ruta_archivo: '/ruta/archivo6.txt', creacion_archivo: date('2023-12-06'), contenido_archivo: 'Contenido del archivo 6'});
CREATE (a7:Archivo {nombre_archivo: 'Archivo7', ruta_archivo: '/ruta/archivo7.txt', creacion_archivo: date('2023-12-07'), contenido_archivo: 'Contenido del archivo 7'});
CREATE (a8:Archivo {nombre_archivo: 'Archivo8', ruta_archivo: '/ruta/archivo8.txt', creacion_archivo: date('2023-12-08'), contenido_archivo: 'Contenido del archivo 8'});
CREATE (a9:Archivo {nombre_archivo: 'Archivo9', ruta_archivo: '/ruta/archivo9.txt', creacion_archivo: date('2023-12-09'), contenido_archivo: 'Contenido del archivo 9'});
CREATE (a10:Archivo {nombre_archivo: 'Archivo10', ruta_archivo: '/ruta/archivo10.txt', creacion_archivo: date('2023-12-10'), contenido_archivo: 'Contenido del archivo 10'});
CREATE (a11:Archivo {nombre_archivo: 'Archivo11', ruta_archivo: '/ruta/archivo11.txt', creacion_archivo: date('2023-12-11'), contenido_archivo: 'Contenido del archivo 11'});
CREATE (a12:Archivo {nombre_archivo: 'Archivo12', ruta_archivo: '/ruta/archivo12.txt', creacion_archivo: date('2023-12-12'), contenido_archivo: 'Contenido del archivo 12'});
CREATE (a13:Archivo {nombre_archivo: 'Archivo13', ruta_archivo: '/ruta/archivo13.txt', creacion_archivo: date('2023-12-13'), contenido_archivo: 'Contenido del archivo 13'});
CREATE (a14:Archivo {nombre_archivo: 'Archivo14', ruta_archivo: '/ruta/archivo14.txt', creacion_archivo: date('2023-12-14'), contenido_archivo: 'Contenido del archivo 14'});
CREATE (a15:Archivo {nombre_archivo: 'Archivo15', ruta_archivo: '/ruta/archivo15.txt', creacion_archivo: date('2023-12-15'), contenido_archivo: 'Contenido del archivo 15'});
CREATE (a16:Archivo {nombre_archivo: 'Archivo16', ruta_archivo: '/ruta/archivo16.xlsx', creacion_archivo: date('2023-12-16'), contenido_archivo: 'Contenido del archivo 16'});
CREATE (a17:Archivo {nombre_archivo: 'Archivo17', ruta_archivo: '/ruta/archivo17.xlsx', creacion_archivo: date('2023-12-17'), contenido_archivo: 'Contenido del archivo 17'});
CREATE (a18:Archivo {nombre_archivo: 'Archivo18', ruta_archivo: '/ruta/archivo18.xlsx', creacion_archivo: date('2023-12-18'), contenido_archivo: 'Contenido del archivo 18'});
CREATE (a19:Archivo {nombre_archivo: 'Archivo19', ruta_archivo: '/ruta/archivo19.xlsx', creacion_archivo: date('2023-12-19'), contenido_archivo: 'Contenido del archivo 19'});
CREATE (a20:Archivo {nombre_archivo: 'Archivo20', ruta_archivo: '/ruta/archivo20.xlsx', creacion_archivo: date('2023-12-20'), contenido_archivo: 'Contenido del archivo 20'});


UNWIND [
    {tipo: 't1', archivos: ['Archivo1', 'Archivo2', 'Archivo3', 'Archivo4', 'Archivo5', 'Archivo6', 'Archivo7', 'Archivo8', 'Archivo9', 'Archivo10', 'Archivo11', 'Archivo12', 'Archivo13', 'Archivo14', 'Archivo15']},
    {tipo: 't2', archivos: ['Archivo16', 'Archivo17', 'Archivo18', 'Archivo19', 'Archivo20']}
] AS relacion
MATCH (t:Tipo {nombre_tipo: relacion.tipo})
UNWIND relacion.archivos AS archivo
MATCH (a:Archivo {nombre_archivo: archivo})
CREATE (a)-[:ES_TIPO {Active: 'Yes'}]->(t);


UNWIND [
    {usuario: 'steve', archivos: ['Archivo1', 'Archivo2', 'Archivo3', 'Archivo4', 'Archivo5', 'Archivo6', 'Archivo7', 'Archivo8', 'Archivo9', 'Archivo10']},
    {usuario: 'laura', archivos: ['Archivo11', 'Archivo12', 'Archivo13', 'Archivo14', 'Archivo15', 'Archivo16']},
    {usuario: 'andre', archivos: ['Archivo17', 'Archivo18', 'Archivo19', 'Archivo20']}
] AS relacion
MATCH (u:Usuario {nombre_usuario: relacion.usuario})
UNWIND relacion.archivos AS archivo
MATCH (a:Archivo {nombre_archivo: archivo})
CREATE (u)-[:POSEE {Active: 'Yes'}]->(a);

CREATE (p1:Permiso {fecha_compartido: date('2023-12-01'), fecha_expiracion: date('2023-12-10')});
CREATE (p2:Permiso {fecha_compartido: date('2023-12-02'), fecha_expiracion: date('2023-12-11')});
CREATE (p3:Permiso {fecha_compartido: date('2023-12-03'), fecha_expiracion: date('2023-12-12')});
CREATE (p4:Permiso {fecha_compartido: date('2023-12-04'), fecha_expiracion: date('2023-12-13')});
CREATE (p5:Permiso {fecha_compartido: date('2023-12-05'), fecha_expiracion: date('2023-12-14')});
CREATE (p6:Permiso {fecha_compartido: date('2023-12-06'), fecha_expiracion: date('2023-12-15')});
CREATE (p7:Permiso {fecha_compartido: date('2023-12-07'), fecha_expiracion: date('2023-12-16')});
CREATE (p8:Permiso {fecha_compartido: date('2023-12-08'), fecha_expiracion: date('2023-12-17')});
CREATE (p9:Permiso {fecha_compartido: date('2023-12-09'), fecha_expiracion: date('2023-12-18')});

UNWIND [
    {permiso: 'p1', usuario_origen: 'steve', usuario_destino: 'laura', archivo: 'Archivo1'},
    {permiso: 'p2', usuario_origen: 'steve', usuario_destino: 'laura', archivo: 'Archivo2'},
    {permiso: 'p3', usuario_origen: 'steve', usuario_destino: 'laura', archivo: 'Archivo3'},
    {permiso: 'p4', usuario_origen: 'steve', usuario_destino: 'laura', archivo: 'Archivo4'},
    {permiso: 'p5', usuario_origen: 'steve', usuario_destino: 'andre', archivo: 'Archivo5'},
    {permiso: 'p6', usuario_origen: 'steve', usuario_destino: 'andre', archivo: 'Archivo6'},
    {permiso: 'p7', usuario_origen: 'steve', usuario_destino: 'andre', archivo: 'Archivo7'},
    {permiso: 'p8', usuario_origen: 'andre', usuario_destino: 'steve', archivo: 'Archivo8'},
    {permiso: 'p9', usuario_origen: 'andre', usuario_destino: 'laura', archivo: 'Archivo9'}
] AS relacion
MATCH (u_origen:Usuario {nombre_usuario: relacion.usuario_origen})
MATCH (u_destino:Usuario {nombre_usuario: relacion.usuario_destino})
MATCH (a:Archivo {nombre: relacion.archivo})
MATCH (p:Permiso {fecha_compartido: date('2023-12-' + substring(relacion.permiso, 1, 1))})
CREATE (u_origen)-[:COMPARTE {Active: 'Yes'}]->(p)
CREATE (p)-[:A_USUARIO]->(u_destino)
CREATE (p)-[:DE_ARCHIVO]->(a);


CREATE (c1:Carpeta {nombre_carpeta: 'Carpeta1', ruta_carpeta: '/ruta/carpeta1', creacion_carpeta: date('2023-12-01')});
CREATE (c2:Carpeta {nombre_carpeta: 'Carpeta2', ruta_carpeta: '/ruta/carpeta2', creacion_carpeta: date('2023-12-02')});
CREATE (c3:Carpeta {nombre_carpeta: 'Carpeta3', ruta_carpeta: '/ruta/carpeta3', creacion_carpeta: date('2023-12-03')});
CREATE (c4:Carpeta {nombre_carpeta: 'Carpeta4', ruta_carpeta: '/ruta/carpeta4', creacion_carpeta: date('2023-12-04')});
CREATE (c5:Carpeta {nombre_carpeta: 'Carpeta5', ruta_carpeta: '/ruta/carpeta5', creacion_carpeta: date('2023-12-05')});

UNWIND [
    {carpeta: 'c1', archivos: ['Archivo1']},
    {carpeta: 'c2', archivos: ['Archivo2']},
    {carpeta: 'c3', archivos: ['Archivo3']},
    {carpeta: 'c4', archivos: ['Archivo4', 'Archivo5', 'Archivo6']},
    {carpeta: 'c5', archivos: ['Archivo7', 'Archivo8', 'Archivo9', 'Archivo10', 'Archivo11']}
] AS relacion
MATCH (c:Carpeta {nombre_carpeta: relacion.carpeta})
UNWIND relacion.archivos AS archivo
MATCH (a:Archivo {nombre_archivo: archivo})
CREATE (c)-[:CONTIENE {Active: 'Yes'}]->(a);


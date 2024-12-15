// Crear Usuarios
CREATE (u1:Usuario {nombre_usuario: "steve", contrasena: "486579"});
CREATE (u2:Usuario {nombre_usuario: "andre", contrasena: "135792468"});
CREATE (u3:Usuario {nombre_usuario: "laura", contrasena: "987654321"});

// Crear Roles
CREATE (r1:Role {nombre_rol: 'Administrador', description: 'Acceso completo a todas las funciones y UIs'});
CREATE (r2:Role {nombre_rol: 'ManipuladorElementos', description: 'Puede crear y eliminar archivos'});
CREATE (r3:Role {nombre_rol: 'ManipuladorExtrem', description: 'Puede crear, eliminar archivos y compartir elementos'});

// Relacionar Usuarios con Roles con atributo Active
CREATE (u1)-[:TIENE_ROL {Active: 'Yes'}]->(r1);
CREATE (u3)-[:TIENE_ROL {Active: 'Yes'}]->(r2);
CREATE (u2)-[:TIENE_ROL {Active: 'Yes'}]->(r3);

// Crear Funciones
CREATE (f1:Function {nombre_funcion: 'Crear', description: 'Permite crear nuevos elementos'});
CREATE (f2:Function {nombre_funcion: 'Eliminar', description: 'Permite eliminar elementos'});
CREATE (f3:Function {nombre_funcion: 'Compartir', description: 'Permite compartir elementos con otros usuarios'});
CREATE (f4:Function {nombre_funcion: 'Editar', description: 'Permite editar elementos existentes'});
CREATE (f5:Function {nombre_funcion: 'Cambiar', description: 'Permite cambiar configuraciones o atributos de elementos'});

// Relacionar Roles con Funciones con atributo Active
// Administrador
CREATE (r1)-[:TIENE_FUNCION {Active: 'Yes'}]->(f1);
CREATE (r1)-[:TIENE_FUNCION {Active: 'Yes'}]->(f2);
CREATE (r1)-[:TIENE_FUNCION {Active: 'Yes'}]->(f3);
CREATE (r1)-[:TIENE_FUNCION {Active: 'Yes'}]->(f4);
CREATE (r1)-[:TIENE_FUNCION {Active: 'Yes'}]->(f5);

// ManipuladorElementos
CREATE (r2)-[:TIENE_FUNCION {Active: 'Yes'}]->(f1);
CREATE (r2)-[:TIENE_FUNCION {Active: 'Yes'}]->(f2);
CREATE (r2)-[:TIENE_FUNCION {Active: 'Yes'}]->(f4);
CREATE (r2)-[:TIENE_FUNCION {Active: 'Yes'}]->(f5);

// ManipuladorExtrem
CREATE (r3)-[:TIENE_FUNCION {Active: 'Yes'}]->(f1);
CREATE (r3)-[:TIENE_FUNCION {Active: 'Yes'}]->(f2);
CREATE (r3)-[:TIENE_FUNCION {Active: 'Yes'}]->(f3);

// Crear Interfaces de Usuario (UI)
CREATE (ui1:UI {nombre_ui: 'Edición', description: 'Interfaz para edición de elementos'});
CREATE (ui2:UI {nombre_ui: 'Compartir', description: 'Interfaz para compartir elementos'});
CREATE (ui3:UI {nombre_ui: 'Cambiar', description: 'Interfaz para cambiar configuraciones'});
CREATE (ui4:UI {nombre_ui: 'Administración', description: 'Interfaz para administrar el sistema'});

// Relacionar Funciones con UIs con atributo Active
CREATE (f1)-[:PERTENECE_UI {Active: 'Yes'}]->(ui1);
CREATE (f2)-[:PERTENECE_UI {Active: 'Yes'}]->(ui1);
CREATE (f4)-[:PERTENECE_UI {Active: 'Yes'}]->(ui1);
CREATE (f3)-[:PERTENECE_UI {Active: 'Yes'}]->(ui2);
CREATE (f5)-[:PERTENECE_UI {Active: 'Yes'}]->(ui3);

// Crear Tipos de Archivos
CREATE (t1:TipoArchivo {name: 'Texto'});
CREATE (t2:TipoArchivo {name: 'Excel'});

// Crear Archivos
CREATE (a1:Archivo {nombre: 'Archivo1', ruta: '/ruta/archivo1.txt', fecha_creacion: date('2023-12-01'), contenido: 'Contenido del archivo 1'});
CREATE (a2:Archivo {nombre: 'Archivo2', ruta: '/ruta/archivo2.txt', fecha_creacion: date('2023-12-02'), contenido: 'Contenido del archivo 2'});
CREATE (a3:Archivo {nombre: 'Archivo3', ruta: '/ruta/archivo3.txt', fecha_creacion: date('2023-12-03'), contenido: 'Contenido del archivo 3'});
CREATE (a4:Archivo {nombre: 'Archivo4', ruta: '/ruta/archivo4.txt', fecha_creacion: date('2023-12-04'), contenido: 'Contenido del archivo 4'});
CREATE (a5:Archivo {nombre: 'Archivo5', ruta: '/ruta/archivo5.txt', fecha_creacion: date('2023-12-05'), contenido: 'Contenido del archivo 5'});
CREATE (a6:Archivo {nombre: 'Archivo6', ruta: '/ruta/archivo6.txt', fecha_creacion: date('2023-12-06'), contenido: 'Contenido del archivo 6'});
CREATE (a7:Archivo {nombre: 'Archivo7', ruta: '/ruta/archivo7.txt', fecha_creacion: date('2023-12-07'), contenido: 'Contenido del archivo 7'});
CREATE (a8:Archivo {nombre: 'Archivo8', ruta: '/ruta/archivo8.txt', fecha_creacion: date('2023-12-08'), contenido: 'Contenido del archivo 8'});
CREATE (a9:Archivo {nombre: 'Archivo9', ruta: '/ruta/archivo9.txt', fecha_creacion: date('2023-12-09'), contenido: 'Contenido del archivo 9'});
CREATE (a10:Archivo {nombre: 'Archivo10', ruta: '/ruta/archivo10.txt', fecha_creacion: date('2023-12-10'), contenido: 'Contenido del archivo 10'});
CREATE (a11:Archivo {nombre: 'Archivo11', ruta: '/ruta/archivo11.txt', fecha_creacion: date('2023-12-11'), contenido: 'Contenido del archivo 11'});
CREATE (a12:Archivo {nombre: 'Archivo12', ruta: '/ruta/archivo12.txt', fecha_creacion: date('2023-12-12'), contenido: 'Contenido del archivo 12'});
CREATE (a13:Archivo {nombre: 'Archivo13', ruta: '/ruta/archivo13.txt', fecha_creacion: date('2023-12-13'), contenido: 'Contenido del archivo 13'});
CREATE (a14:Archivo {nombre: 'Archivo14', ruta: '/ruta/archivo14.txt', fecha_creacion: date('2023-12-14'), contenido: 'Contenido del archivo 14'});
CREATE (a15:Archivo {nombre: 'Archivo15', ruta: '/ruta/archivo15.txt', fecha_creacion: date('2023-12-15'), contenido: 'Contenido del archivo 15'});
CREATE (a16:Archivo {nombre: 'Archivo16', ruta: '/ruta/archivo16.xlsx', fecha_creacion: date('2023-12-16'), contenido: 'Contenido del archivo 16'});
CREATE (a17:Archivo {nombre: 'Archivo17', ruta: '/ruta/archivo17.xlsx', fecha_creacion: date('2023-12-17'), contenido: 'Contenido del archivo 17'});
CREATE (a18:Archivo {nombre: 'Archivo18', ruta: '/ruta/archivo18.xlsx', fecha_creacion: date('2023-12-18'), contenido: 'Contenido del archivo 18'});
CREATE (a19:Archivo {nombre: 'Archivo19', ruta: '/ruta/archivo19.xlsx', fecha_creacion: date('2023-12-19'), contenido: 'Contenido del archivo 19'});
CREATE (a20:Archivo {nombre: 'Archivo20', ruta: '/ruta/archivo20.xlsx', fecha_creacion: date('2023-12-20'), contenido: 'Contenido del archivo 20'});

// Relacionar Archivos con Tipos
CREATE (a1)-[:ES_TIPO {Active: 'Yes'}]->(t1);
CREATE (a2)-[:ES_TIPO {Active: 'Yes'}]->(t1);
CREATE (a3)-[:ES_TIPO {Active: 'Yes'}]->(t1);
CREATE (a4)-[:ES_TIPO {Active: 'Yes'}]->(t1);
CREATE (a5)-[:ES_TIPO {Active: 'Yes'}]->(t1);
CREATE (a6)-[:ES_TIPO {Active: 'Yes'}]->(t1);
CREATE (a7)-[:ES_TIPO {Active: 'Yes'}]->(t1);
CREATE (a8)-[:ES_TIPO {Active: 'Yes'}]->(t1);
CREATE (a9)-[:ES_TIPO {Active: 'Yes'}]->(t1);
CREATE (a10)-[:ES_TIPO {Active: 'Yes'}]->(t1);
CREATE (a11)-[:ES_TIPO {Active: 'Yes'}]->(t1);
CREATE (a12)-[:ES_TIPO {Active: 'Yes'}]->(t1);
CREATE (a13)-[:ES_TIPO {Active: 'Yes'}]->(t1);
CREATE (a14)-[:ES_TIPO {Active: 'Yes'}]->(t1);
CREATE (a15)-[:ES_TIPO {Active: 'Yes'}]->(t1);
CREATE (a16)-[:ES_TIPO {Active: 'Yes'}]->(t2);
CREATE (a17)-[:ES_TIPO {Active: 'Yes'}]->(t2);
CREATE (a18)-[:ES_TIPO {Active: 'Yes'}]->(t2);
CREATE (a19)-[:ES_TIPO {Active: 'Yes'}]->(t2);
CREATE (a20)-[:ES_TIPO {Active: 'Yes'}]->(t2);

// Relacionar Usuarios con Archivos como Propietarios
CREATE (u1)-[:POSEE {Active: 'Yes'}]->(a1);
CREATE (u1)-[:POSEE {Active: 'Yes'}]->(a2);
CREATE (u1)-[:POSEE {Active: 'Yes'}]->(a3);
CREATE (u1)-[:POSEE {Active: 'Yes'}]->(a4);
CREATE (u1)-[:POSEE {Active: 'Yes'}]->(a5);
CREATE (u1)-[:POSEE {Active: 'Yes'}]->(a6);
CREATE (u1)-[:POSEE {Active: 'Yes'}]->(a7);
CREATE (u1)-[:POSEE {Active: 'Yes'}]->(a8);
CREATE (u1)-[:POSEE {Active: 'Yes'}]->(a9);
CREATE (u1)-[:POSEE {Active: 'Yes'}]->(a10);
CREATE (u3)-[:POSEE {Active: 'Yes'}]->(a11);
CREATE (u3)-[:POSEE {Active: 'Yes'}]->(a12);
CREATE (u3)-[:POSEE {Active: 'Yes'}]->(a13);
CREATE (u3)-[:POSEE {Active: 'Yes'}]->(a14);
CREATE (u3)-[:POSEE {Active: 'Yes'}]->(a15);
CREATE (u3)-[:POSEE {Active: 'Yes'}]->(a16);
CREATE (u2)-[:POSEE {Active: 'Yes'}]->(a17);
CREATE (u2)-[:POSEE {Active: 'Yes'}]->(a18);
CREATE (u2)-[:POSEE {Active: 'Yes'}]->(a19);
CREATE (u2)-[:POSEE {Active: 'Yes'}]->(a20);

// Crear Permisos de Archivos
CREATE (p1:Permiso {fecha_compartido: date('2023-12-01'), fecha_expiracion: date('2023-12-10')});
CREATE (p2:Permiso {fecha_compartido: date('2023-12-02'), fecha_expiracion: date('2023-12-11')});
CREATE (p3:Permiso {fecha_compartido: date('2023-12-03'), fecha_expiracion: date('2023-12-12')});
CREATE (p4:Permiso {fecha_compartido: date('2023-12-04'), fecha_expiracion: date('2023-12-13')});
CREATE (p5:Permiso {fecha_compartido: date('2023-12-05'), fecha_expiracion: date('2023-12-14')});
CREATE (p6:Permiso {fecha_compartido: date('2023-12-06'), fecha_expiracion: date('2023-12-15')});
CREATE (p7:Permiso {fecha_compartido: date('2023-12-07'), fecha_expiracion: date('2023-12-16')});
CREATE (p8:Permiso {fecha_compartido: date('2023-12-08'), fecha_expiracion: date('2023-12-17')});
CREATE (p9:Permiso {fecha_compartido: date('2023-12-09'), fecha_expiracion: date('2023-12-18')});

// Relacionar Permisos con Usuarios y Archivos
CREATE (u1)-[:COMPARTE {Active: 'Yes'}]->(p1);
CREATE (p1)-[:A_USUARIO]->(u3);
CREATE (p1)-[:DE_ARCHIVO]->(a1);
CREATE (u1)-[:COMPARTE {Active: 'Yes'}]->(p2);
CREATE (p2)-[:A_USUARIO]->(u3);
CREATE (p2)-[:DE_ARCHIVO]->(a2);
CREATE (u1)-[:COMPARTE {Active: 'Yes'}]->(p3);
CREATE (p3)-[:A_USUARIO]->(u3);
CREATE (p3)-[:DE_ARCHIVO]->(a3);
CREATE (u1)-[:COMPARTE {Active: 'Yes'}]->(p4);
CREATE (p4)-[:A_USUARIO]->(u3);
CREATE (p4)-[:DE_ARCHIVO]->(a4);
CREATE (u1)-[:COMPARTE {Active: 'Yes'}]->(p5);
CREATE (p5)-[:A_USUARIO]->(u2);
CREATE (p5)-[:DE_ARCHIVO]->(a5);
CREATE (u1)-[:COMPARTE {Active: 'Yes'}]->(p6);
CREATE (p6)-[:A_USUARIO]->(u2);
CREATE (p6)-[:DE_ARCHIVO]->(a6);
CREATE (u1)-[:COMPARTE {Active: 'Yes'}]->(p7);
CREATE (p7)-[:A_USUARIO]->(u2);
CREATE (p7)-[:DE_ARCHIVO]->(a7);
CREATE (u2)-[:COMPARTE {Active: 'Yes'}]->(p8);
CREATE (p8)-[:A_USUARIO]->(u1);
CREATE (p8)-[:DE_ARCHIVO]->(a8);
CREATE (u2)-[:COMPARTE {Active: 'Yes'}]->(p9);
CREATE (p9)-[:A_USUARIO]->(u3);
CREATE (p9)-[:DE_ARCHIVO]->(a9);

// Crear Carpetas
CREATE (c1:Carpeta {nombre: 'Carpeta1', ruta: '/ruta/carpeta1', fecha_creacion: date('2023-12-01')});
CREATE (c2:Carpeta {nombre: 'Carpeta2', ruta: '/ruta/carpeta2', fecha_creacion: date('2023-12-02')});
CREATE (c3:Carpeta {nombre: 'Carpeta3', ruta: '/ruta/carpeta3', fecha_creacion: date('2023-12-03')});
CREATE (c4:Carpeta {nombre: 'Carpeta4', ruta: '/ruta/carpeta4', fecha_creacion: date('2023-12-04')});
CREATE (c5:Carpeta {nombre: 'Carpeta5', ruta: '/ruta/carpeta5', fecha_creacion: date('2023-12-05')});

// Relacionar Carpetas con Archivos
CREATE (c1)-[:CONTIENE {Active: 'Yes'}]->(a1);
CREATE (c2)-[:CONTIENE {Active: 'Yes'}]->(a2);
CREATE (c3)-[:CONTIENE {Active: 'Yes'}]->(a3);
CREATE (c4)-[:CONTIENE {Active: 'Yes'}]->(a4);
CREATE (c4)-[:CONTIENE {Active: 'Yes'}]->(a5);
CREATE (c4)-[:CONTIENE {Active: 'Yes'}]->(a6);
CREATE (c5)-[:CONTIENE {Active: 'Yes'}]->(a7);
CREATE (c5)-[:CONTIENE {Active: 'Yes'}]->(a8);
CREATE (c5)-[:CONTIENE {Active: 'Yes'}]->(a9);
CREATE (c5)-[:CONTIENE {Active: 'Yes'}]->(a10);
CREATE (c5)-[:CONTIENE {Active: 'Yes'}]->(a11);

// Crear usuarios
CREATE (u1:Usuario {nombre_usuario: "admin", contrasena: "admin123", active: true});
CREATE (u2:Usuario {nombre_usuario: "elementosUser", contrasena: "user123", active: true});
CREATE (u3:Usuario {nombre_usuario: "extremUser", contrasena: "extrem123", active: true});

// Crear roles
CREATE (r1:Rol {id_rol: 1, nombre_rol: "Administrador"});
CREATE (r2:Rol {id_rol: 2, nombre_rol: "ManipuladorElementos"});
CREATE (r3:Rol {id_rol: 3, nombre_rol: "ManipuladorExtrem"});

// Asignar roles a usuarios
MATCH (u1:Usuario {nombre_usuario: "admin"}), (r1:Rol {nombre_rol: "Administrador"})
CREATE (u1)-[:TIENE_ROL]->(r1);

MATCH (u2:Usuario {nombre_usuario: "elementosUser"}), (r2:Rol {nombre_rol: "ManipuladorElementos"})
CREATE (u2)-[:TIENE_ROL]->(r2);

MATCH (u3:Usuario {nombre_usuario: "extremUser"}), (r3:Rol {nombre_rol: "ManipuladorExtrem"})
CREATE (u3)-[:TIENE_ROL]->(r3);

// Crear funciones
CREATE (f1:Funcion {id_funcion: 1, nombre_funcion: "CrearArchivo"});
CREATE (f2:Funcion {id_funcion: 2, nombre_funcion: "EliminarArchivo"});
CREATE (f3:Funcion {id_funcion: 3, nombre_funcion: "CompartirArchivo"});

// Asignar funciones a roles
MATCH (r1:Rol {nombre_rol: "Administrador"}), (f1:Funcion {nombre_funcion: "CrearArchivo"})
CREATE (r1)-[:TIENE_FUNCION]->(f1);

MATCH (r1:Rol {nombre_rol: "Administrador"}), (f2:Funcion {nombre_funcion: "EliminarArchivo"})
CREATE (r1)-[:TIENE_FUNCION]->(f2);

MATCH (r1:Rol {nombre_rol: "Administrador"}), (f3:Funcion {nombre_funcion: "CompartirArchivo"})
CREATE (r1)-[:TIENE_FUNCION]->(f3);

MATCH (r2:Rol {nombre_rol: "ManipuladorElementos"}), (f1:Funcion {nombre_funcion: "CrearArchivo"})
CREATE (r2)-[:TIENE_FUNCION]->(f1);

MATCH (r2:Rol {nombre_rol: "ManipuladorElementos"}), (f2:Funcion {nombre_funcion: "EliminarArchivo"})
CREATE (r2)-[:TIENE_FUNCION]->(f2);

MATCH (r3:Rol {nombre_rol: "ManipuladorExtrem"}), (f1:Funcion {nombre_funcion: "CrearArchivo"})
CREATE (r3)-[:TIENE_FUNCION]->(f1);

MATCH (r3:Rol {nombre_rol: "ManipuladorExtrem"}), (f2:Funcion {nombre_funcion: "EliminarArchivo"})
CREATE (r3)-[:TIENE_FUNCION]->(f2);

MATCH (r3:Rol {nombre_rol: "ManipuladorExtrem"}), (f3:Funcion {nombre_funcion: "CompartirArchivo"})
CREATE (r3)-[:TIENE_FUNCION]->(f3);

// Crear UIs
CREATE (ui1:UI {id_ui: 1, url: "edicion.com"});
CREATE (ui2:UI {id_ui: 2, url: "compartir.com"});
CREATE (ui3:UI {id_ui: 3, url: "cambiar.com"});

// Asignar funciones a UIs
MATCH (ui1:UI {url: "edicion.com"}), (f1:Funcion {nombre_funcion: "CrearArchivo"})
CREATE (ui1)-[:TIENE_FUNCION]->(f1);

MATCH (ui2:UI {url: "compartir.com"}), (f3:Funcion {nombre_funcion: "CompartirArchivo"})
CREATE (ui2)-[:TIENE_FUNCION]->(f3);

MATCH (ui3:UI {url: "cambiar.com"}), (f2:Funcion {nombre_funcion: "EliminarArchivo"})
CREATE (ui3)-[:TIENE_FUNCION]->(f2);

// Crear carpetas
CREATE (c1:Carpeta {id_carpeta: apoc.create.uuid(), nombre_carpeta: "Carpeta1", ruta_carpeta: "/docs/", creacion_carpeta: date()});

// Asignar carpetas a usuarios
MATCH (u1:Usuario {nombre_usuario: "admin"}), (c1:Carpeta {nombre_carpeta: "Carpeta1"})
CREATE (u1)-[:POSEE]->(c1);

// Crear archivos
CREATE (a1:Archivo {id_tipo: 1, nombre_archivo: "Archivo1", ruta_archivo: "/docs/", creacion_archivo: date(), contenido_archivo: "Contenido archivo 1"});
CREATE (a2:Archivo {id_tipo: 2, nombre_archivo: "Archivo2", ruta_archivo: "/docs/", creacion_archivo: date(), contenido_archivo: "Contenido archivo 2"});

// Asignar archivos a usuarios
MATCH (u1:Usuario {nombre_usuario: "admin"}), (a1:Archivo {nombre_archivo: "Archivo1"})
CREATE (u1)-[:POSEE]->(a1);

MATCH (u2:Usuario {nombre_usuario: "elementosUser"}), (a2:Archivo {nombre_archivo: "Archivo2"})
CREATE (u2)-[:POSEE]->(a2);

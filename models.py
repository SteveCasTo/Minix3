CREATE (u1:Usuario {nombre_usuario: "steve", contrasena: "486579"});
CREATE (u2:Usuario {nombre_usuario: "andre", contrasena: "135792468"});
CREATE (u3:Usuario {nombre_usuario: "laura", contrasena: "987654321"});

CREATE (:Role {name: 'Administrador', description: 'Acceso completo a todas las funciones y UIs'});
CREATE (:Role {name: 'ManipuladorElementos', description: 'Puede crear y eliminar archivos'});
CREATE (:Role {name: 'ManipuladorExtrem', description: 'Puede crear, eliminar archivos y compartir elementos'});

// Creación de Funciones
CREATE (:Function {name: 'Crear', description: 'Permite crear nuevos elementos'});
CREATE (:Function {name: 'Eliminar', description: 'Permite eliminar elementos'});
CREATE (:Function {name: 'Compartir', description: 'Permite compartir elementos con otros usuarios'});
CREATE (:Function {name: 'Editar', description: 'Permite editar elementos existentes'});
CREATE (:Function {name: 'Cambiar', description: 'Permite cambiar configuraciones o atributos de elementos'});

// Creación de UIs
CREATE (:UI {name: 'Edición', description: 'Interfaz para edición de elementos'});
CREATE (:UI {name: 'Compartir', description: 'Interfaz para compartir elementos'});
CREATE (:UI {name: 'Cambiar', description: 'Interfaz para cambiar configuraciones'});
CREATE (:UI {name: 'Administración', description: 'Interfaz para administrar el sistema'});

// Relaciones entre Roles y Funciones
MATCH (r:Role {name: 'Administrador'}), (f:Function)
CREATE (r)-[:CAN_DO]->(f);

MATCH (r:Role {name: 'ManipuladorElementos'}), (f:Function)
WHERE f.name IN ['Crear', 'Eliminar', 'Edición', 'Cambiar']
CREATE (r)-[:CAN_DO]->(f);

MATCH (r:Role {name: 'ManipuladorExtrem'}), (f:Function)
WHERE f.name IN ['Crear', 'Eliminar', 'Compartir']
CREATE (r)-[:CAN_DO]->(f);

// Relaciones entre Funciones y UIs
MATCH (f:Function {name: 'Crear'}), (ui:UI {name: 'Edición'})
CREATE (f)-[:AVAILABLE_IN]->(ui);

MATCH (f:Function {name: 'Eliminar'}), (ui:UI {name: 'Edición'})
CREATE (f)-[:AVAILABLE_IN]->(ui);

MATCH (f:Function {name: 'Compartir'}), (ui:UI {name: 'Compartir'})
CREATE (f)-[:AVAILABLE_IN]->(ui);

MATCH (f:Function {name: 'Editar'}), (ui:UI {name: 'Edición'})
CREATE (f)-[:AVAILABLE_IN]->(ui);

MATCH (f:Function {name: 'Cambiar'}), (ui:UI {name: 'Cambiar'})
CREATE (f)-[:AVAILABLE_IN]->(ui);




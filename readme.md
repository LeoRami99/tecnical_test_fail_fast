# Prueba Técnica: Sistema de Permisos

### Requisitos Técnicos Obligatorios:
- **Base de Datos:** PostgreSQL
- **Backend:** Django Rest Framework
- **Frontend:** React.js

### Objetivo
El objetivo de esta prueba técnica es desarrollar un sistema de permisos que permita asignar privilegios a usuarios, ya sea por entidad o por registro individual. Este sistema gestionará los permisos de manera flexible, asociándolos tanto a roles como a usuarios específicos.

### Modelos Implementados
Para lograr esta funcionalidad, se han creado los siguientes modelos:

- **PermiUser:** Gestiona los permisos asignados a un usuario.
- **PermiRole:** Gestiona los permisos asignados a un rol.
- **PermiUserRecord:** Asigna permisos a un usuario sobre registros específicos.
- **PermiRoleRecord:** Asigna permisos a un rol sobre registros específicos.
- **Permission:** Define la combinatoria de permisos que pueden ser otorgados a usuarios o roles.

### Funcionalidad del Sistema de Permisos
El sistema permite asignar permisos tanto a nivel de entidad como a nivel de registro individual dentro de una entidad. Esto proporciona una mayor granularidad en el control de acceso, ya que se pueden combinar distintos permisos según las necesidades del usuario o del rol.

### Entidades Para Pruebas
En la aplicación ERP de ejemplo, se gestionan dos entidades principales:

- **Sucursal (Branch Office):** Representa una oficina de la empresa.
- **Centro de Costos (Cost Center):** Representa una unidad dentro de la empresa a la que se le asignan costos.

Cada una de estas entidades puede tener permisos específicos asociados, tanto a nivel de entidad como a nivel de registros individuales dentro de ellas.

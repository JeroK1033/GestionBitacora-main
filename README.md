# GestionBitacora

Este repositorio contiene la implementación y pruebas para el sistema de gestión de bitácora. La aplicación permite a los supervisores de obra registrar, consultar y gestionar la bitácora diaria de una construcción, garantizando la trazabilidad de las actividades realizadas en la obra.



## Funcionalidad 1: Registrar una actividad

Permite a los supervisores registrar una actividad en un día y una hora específica.


### Caso de Prueba #1: Caso Normal - Registro de Actividad

| ID Actividad |    Fecha/Hora    | Supervisor |        Descripcion       | Condiciones Climaticas |      Anexos      |
|--------------|------------------|------------|--------------------------|------------------------|------------------|
|    232245    | 08/03/2025 15:36 | Supervisor | Inicio de Nuevo Proyecto |   Nublado y Lluvioso   | InfoProyecto.pdf | 

|                  Supervisor                  |
|   Nombre   |       Correo       | Contraseña | 
|------------|--------------------|------------| 
| Juan Perez | juanp225@gmail.com | JuanPz4875 |


### Caso de Prueba #2: Caso Normal - Registro de Actividad con Fecha y Hora

| ID Actividad |    Fecha/Hora    | Supervisor |        Descripcion       | Condiciones Climaticas |           Anexos          |
|--------------|------------------|------------|--------------------------|------------------------|---------------------------|
|    498521    | 16/11/2024 22:45 | Supervisor |   Revision de Proyecto   |         Soleado        | ProyectoReorganizado.docx | 

|                    Supervisor                   |
|    Nombre    |       Correo        | Contraseña | 
|--------------|---------------------|------------| 
| Lucas Correa | lucasc998@gmail.com | LucasC2024 |

### Caso de Prueba #3: Caso Normal - Registro de Actividad con un Anexo Incluido

| ID Actividad |    Fecha/Hora    | Supervisor |            Descripcion            | Condiciones Climaticas |        Anexos       |
|--------------|------------------|------------|-----------------------------------|------------------------|---------------------|
|    984216    | 01/08/2025 08:27 | Supervisor | Evidencias y Avances Metro Bogota |        Neblina         | EvidenciasMetro.pdf | 

|                       Supervisor                     |
|      Nombre     |        Correo         | Contraseña | 
|-----------------|-----------------------|------------| 
| Maria Hernandez | maria_hdz87@gmail.com | MariaH3056 |


### Caso de Prueba #4: Caso Extremo - Registro de Actividad en el limite del dia

| ID Actividad |    Fecha/Hora    | Supervisor |                Descripcion                | Condiciones Climaticas  |             Anexos            |
|--------------|------------------|------------|-------------------------------------------|-------------------------|-------------------------------|
|    284719    | 03/11/2025 19:40 | Supervisor | Detalles técnicos y normativas del diseño |        Tormenta         | Especificaciones_Tecnicas.pdf | 

|                    Supervisor                   |
|    Nombre    |       Correo        | Contraseña | 
|--------------|---------------------|------------| 
| Mateo Herrera | mateoh993@gmail.com | MateoH7621 |


### Caso de Prueba #5: Caso Extremo - Registro de Actividad con multiples anexos

| ID Actividad |    Fecha/Hora    | Supervisor |                    Descripcion                    | Condiciones Climaticas |           Anexos           |
|--------------|------------------|------------|---------------------------------------------------|------------------------|----------------------------|
|    630582    | 18/06/2024 14:20 | Supervisor | Diapositivas con información general del proyecto |        Soleado         | Presentacion_Proyecto.pptx | 

|                    Supervisor                          |
|      Nombre      |        Correo         | Contraseña  | 
|------------------|-----------------------|-------------| 
| Camila Rodriguez | camila.rodr@gmail.com | CamilaR4823 |


### Caso de Prueba #6: Caso Extremo - Registro de Actividad con descripcion larga

| ID Actividad |    Fecha/Hora    | Supervisor |                   Descripcion                   | Condiciones Climaticas |       Anexos       |
|--------------|------------------|------------|-------------------------------------------------|------------------------|--------------------|
|    157943    | 25/12/2023 08:55 | Supervisor | Imagen digital del diseño exterior del proyecto |        Soleado         | Render_Fachada.png | 

|                        Supervisor                          |
|        Nombre       |         Correo          | Contraseña | 
|---------------------|-------------------------|------------| 
| Alejandro Fernandez | alejandrofz23@gmail.com | AlexF9052  |


### Caso de Prueba #7: Caso de Error - Registro de Actividad sin descripcion

| ID Actividad |    Fecha/Hora    | Supervisor | Descripcion | Condiciones Climaticas |         Anexos        |
|--------------|------------------|------------|-------------|------------------------|-----------------------|
|    902356    | 07/07/2025 22:30 | Supervisor |    None     |       No Aplica        | Presupuesto_Obra.xlsx | 

|                    Supervisor                   |
|    Nombre    |       Correo        | Contraseña | 
|--------------|---------------------|------------| 
| Lucas Correa | santi_rz99@gmail.com | SantiR6638 |


### Caso de Prueba #8: Caso de Error - Registro de Actividad con Fecha y Hora Invalida

| ID Actividad |      Fecha/Hora       | Supervisor |                      Descripcion                     | Condiciones Climaticas |           Anexos         |
|--------------|-----------------------|------------|------------------------------------------------------|------------------------|--------------------------|
|    418275    | 30 de Octubre de 2025 | Supervisor | La cubierta del edificio ha sido instalada con éxito |        LLuvioso        | Planos_Estructurales.pdf | 

|                        Supervisor                       |
|     Nombre      |          Correo          | Contraseña | 
|-----------------|--------------------------|------------| 
| Valentina Gomez | valentina.gm12@gmail.com | ValenG3721 |


### Caso de Prueba #9: Caso de Error - Registro de Actividad sin Anexos

| ID Actividad |    Fecha/Hora    | Supervisor |                                 Descripcion                                | Condiciones Climaticas | Anexos |
|--------------|------------------|------------|----------------------------------------------------------------------------|------------------------|--------|
|    765901    | 14/02/2023 16:45 | Supervisor | Las paredes del proyecto han sido construidas y están listas para acabados |        Nublado         |  None  | 

|                    Supervisor                          |
|    Nombre        |       Correo          | Contraseña  | 
|------------------|-----------------------|-------------| 
| Camila Rodriguez | camila.rodr@gmail.com | CamilaR4823 |




## Funcionalidad 2: Consultar actividades

Permite consultar actividades en un rango de fechas determinado.

### Caso de Prueba #1: Caso Normal - Consulta de actividades en un rango válido.

| Fecha Incio |  Fecha Fin | Supervisor | 
|-------------|------------|------------| 
| 01/06/2024  | 10/06/2024 | Juan Perez |

|   Resultado   |  
|---------------|
| 3 Actividades |




### Caso de Prueba #2: Caso Normal - Consulta de actividades con fecha específica.

| Fecha Consulta | Supervisor | 
|----------------|------------| 
|   01/06/2024   | Juan Perez |

|   Resultado |  
|-------------|
| 1 Actividad |


### Caso de Prueba #3: Caso Normal - Consulta de actividades con múltiples filtros.

| Fecha Incio |  Fecha Fin | Condiciones Climaticas | Supervisor | 
|-------------|------------|------------------------|------------| 
| 01/06/2024  | 10/06/2024 |         Neblina        | Juan Perez |

|   Resultado  |  
|--------------|
| 1 Actividad  |

### Caso de Prueba #4: Caso Extremo - Consulta de actividades en un rango de fechas de varios años.

| Fecha Incio |  Fecha Fin | Supervisor | 
|-------------|------------|------------| 
| 01/01/2023  | 31/12/2025 | Juan Perez |

|   Resultado   |  
|---------------|
| 3 Actividades |

### Caso de Prueba #5: Caso Extremo - Consulta con múltiples filtros aplicados.

| Fecha Incio |  Fecha Fin |    Supervisor    | Condiciones CLimaticas | %Descripcion% |
|-------------|------------|------------------|------------------------|---------------|
| 01/06/2024  | 10/06/2024 | Camila Rodriguez |         Soleado        |   "Proyecto"  |

|  Resultado  |  
|-------------|
| 1 Actividad |

### Caso de Prueba #6: Caso Extremo - Consulta con Fecha Futura

| Fecha Incio |  Fecha Fin | Supervisor | 
|-------------|------------|------------| 
| 01/01/2030  | 31/12/2030 | Juan Perez |

|   Resultado   |  
|---------------|
| 0 Actividades |

### Caso de Prueba #7: Caso de Error - Consulta sin definir fechas.

| Fecha Incio |  Fecha Fin | Supervisor | 
|-------------|------------|------------| 
|    None     |   None     | Juan Perez |

|   Resultado  |  
|--------------|
|     Error    |

### Caso de Prueba #8: Caso de Error - Consulta con fecha de inicio mayor que la fecha de fin.

| Fecha Incio |  Fecha Fin | Supervisor | 
|-------------|------------|------------| 
| 08/08/2025  | 07/07/2024 | Juan Perez |

|   Resultado  |  
|--------------|
|     Error    |

### Caso de Prueba #9: Caso de Error - Intento de consulta sin autenticación.

| Fecha Incio |  Fecha Fin | Supervisor | 
|-------------|------------|------------| 
| 01/01/2023  | 31/12/2025 |    None    |

|   Resultado  |  
|--------------|
|    Error     |


## Funcionalidad 3: Generar reporte de la bitácora

Genera un informe en PDF sobre actividades en un rango de fechas.

### Caso de Prueba #1: Caso Normal - Generación de reporte con datos completos

| Fecha Inicio | Fecha Fin | Supervisor | Anexos Incluidos | Resultado |
|-------------|----------|------------|------------------|-----------|
| 01/01/2025 | 31/01/2025 | Juan Perez | Sí | PDF generado correctamente |

### Caso de Prueba #2: Caso Normal - Generación de reporte sin actividades en el rango de fechas

| Fecha Inicio | Fecha Fin | Supervisor | Resultado |
|-------------|----------|------------|-----------|
| 01/01/2030 | 31/01/2030 | Maria Hernandez | No hay actividades registradas en este rango |

### Caso de Prueba #3: Caso Normal - Generación de reporte con anexos

| Fecha Inicio | Fecha Fin | Supervisor | Anexos Incluidos | Resultado |
|-------------|----------|------------|------------------|-----------|
| 01/06/2024 | 10/06/2024 | Camila Rodriguez | Sí | PDF generado con anexos |

### Caso de Prueba #4: Caso Extremo - Generación de un reporte con miles de actividades

| Fecha Inicio | Fecha Fin | Supervisor | Número de Actividades | Resultado |
|-------------|----------|------------|----------------------|-----------|
| 01/01/2020 | 31/12/2025 | Mateo Herrera | 5000+ | PDF generado correctamente |

### Caso de Prueba #5: Caso Extremo - Generación de reporte en el formato más grande permitido

| Fecha Inicio | Fecha Fin | Supervisor | Formato | Resultado |
|-------------|----------|------------|---------|-----------|
| 01/01/2024 | 31/12/2024 | Alejandro Fernandez | A3 | PDF generado en formato A3 |

### Caso de Prueba #6: Caso Extremo - Generación de reporte con filtros avanzados

| Fecha Inicio | Fecha Fin | Supervisor | Condiciones Climáticas | Resultado |
|-------------|----------|------------|------------------------|-----------|
| 01/06/2024 | 10/06/2024 | Lucas Correa | Lluvioso | PDF generado correctamente |

### Caso de Prueba #7: Caso de Error - Intento de generar un reporte sin definir fechas

| Fecha Inicio | Fecha Fin | Supervisor | Error esperado |
|-------------|----------|------------|---------------|
| None | None | Valentina Gomez | Debe ingresar un rango de fechas válido |

### Caso de Prueba #8: Caso de Error - Intento de generar un reporte con fechas inválidas

| Fecha Inicio | Fecha Fin | Supervisor | Error esperado |
|-------------|----------|------------|---------------|
| 32/06/2024 | 10/06/2024 | Camila Rodriguez | Formato de fecha incorrecto |

### Caso de Prueba #9: Caso de Error - Intento de generar un reporte sin autenticación

| Fecha Inicio | Fecha Fin | Supervisor | Error esperado |
|-------------|----------|------------|---------------|
| 01/06/2024 | 10/06/2024 | None | Usuario no autenticado |


## Funcionalidad 4: Crear cuenta

Permite a los supervisores registrarse en el sistema.

### Caso de Prueba #1: Caso Normal - Registro exitoso con datos válidos

| Nombre | Correo | Contraseña | Resultado |
|--------|--------|------------|-----------|
| Juan Perez | juan.perez@example.com | JuanP@123 | Cuenta creada exitosamente |

### Caso de Prueba #2: Caso Normal - Registro con correo válido y contraseña fuerte

| Nombre | Correo | Contraseña | Resultado |
|--------|--------|------------|-----------|
| Maria Lopez | maria.lopez@example.com | Maria2024# | Cuenta creada exitosamente |

### Caso de Prueba #3: Caso Normal - Registro con nombre y apellido válidos

| Nombre | Correo | Contraseña | Resultado |
|--------|--------|------------|-----------|
| Carlos Rivera | carlos.r@example.com | Carlos2024# | Cuenta creada exitosamente |

### Caso de Prueba #4: Caso Extremo - Registro con la contraseña más larga permitida

| Nombre | Correo | Contraseña | Resultado |
|--------|--------|------------|-----------|
| Luis Gómez | luis.gomez@example.com | 32CaracteresLargos1234#@ | Cuenta creada exitosamente |

### Caso de Prueba #5: Caso Extremo - Registro con caracteres especiales en el nombre

| Nombre | Correo | Contraseña | Resultado |
|--------|--------|------------|-----------|
| Ana-María López | ana.lopez@example.com | AnaFuerte2024! | Cuenta creada exitosamente |

### Caso de Prueba #6: Caso Extremo - Registro con un email en el límite de longitud permitida

| Nombre | Correo | Contraseña | Resultado |
|--------|--------|------------|-----------|
| Ricardo Fernández | rfernandezsuperlargocorreo@example.com | Rf2024#@ | Cuenta creada exitosamente |

### Caso de Prueba #7: Caso de Error - Registro sin correo electrónico

| Nombre | Correo | Contraseña | Error esperado |
|--------|--------|------------|---------------|
| Carlos Rivera | None | Carlos2024 | "Debe ingresar un correo válido" |

### Caso de Prueba #8: Caso de Error - Registro con una contraseña muy corta

| Nombre | Correo | Contraseña | Error esperado |
|--------|--------|------------|---------------|
| Luis Gómez | luis.gomez@example.com | 123 | "La contraseña debe tener al menos 8 caracteres" |

### Caso de Prueba #9: Caso de Error - Registro con un email ya registrado

| Nombre | Correo | Contraseña | Error esperado |
|--------|--------|------------|---------------|
| Juan Perez | juan.perez@example.com | JuanP@123 | "El correo ya está registrado" |



## Funcionalidad 5: Iniciar sesión

Facilita el acceso de los supervisores al sistema.

### Caso de Prueba #1: Caso Normal - Inicio de sesión exitoso

| Correo | Contraseña | Resultado |
|--------|------------|-----------|
| juan.perez@gmail.com | JuanP@123 | Sesión iniciada correctamente |

### Caso de Prueba #2: Caso Normal - Inicio de sesión con recordar sesión activado

| Correo | Contraseña | Recordar Sesión | Resultado |
|--------|------------|----------------|-----------|
| maria.lopez@gmail.com | Maria2024# | Sí | Sesión iniciada y recordada |

### Caso de Prueba #3: Caso Normal - Inicio de sesión con múltiples intentos

| Correo | Contraseña | Intentos | Resultado |
|--------|------------|----------|-----------|
| carlos.r@gmail.com | Carlos2024# | 2 | Sesión iniciada correctamente |

### Caso de Prueba #4: Caso Extremo - Inicio de sesión con una contraseña en el límite de longitud

| Correo | Contraseña | Resultado |
|--------|------------|-----------|
| luis.gomez@gmail.com | 32CaracteresLargos1234#@ | Sesión iniciada correctamente |

### Caso de Prueba #5: Caso Extremo - Inicio de sesión con una contraseña que contiene solo letras minúsculas

| Correo | Contraseña | Resultado |
|--------|------------|-----------|
| maria.lopez@gmail.com | mariaclave | Sesión iniciada correctamente |

### Caso de Prueba #6: Caso Extremo - Inicio de sesión con una contraseña que contiene solo números

| Correo | Contraseña | Resultado |
|--------|------------|-----------|
| carlos.r@gmail.com | 12345678 | Sesión iniciada correctamente |

### Caso de Prueba #7: Caso de Error - Inicio de sesión con contraseña incorrecta

| Correo | Contraseña | Error esperado |
|--------|------------|---------------|
| juan.perez@gmail.com | Incorrecta123 | "Contraseña incorrecta" |

### Caso de Prueba #8: Caso de Error - Inicio de sesión con email no registrado

| Correo | Contraseña | Error esperado |
|--------|------------|---------------|
| usuario.nuevo@gmail.com | NuevaClave@456 | "El correo no está registrado" |

### Caso de Prueba #9: Caso de Error - Inicio de sesión con un email en formato inválido

| Correo | Contraseña | Error esperado |
|--------|------------|---------------|
| incorrecto.com | Prueba2024# | "Formato de correo inválido" |




## Funcionalidad 6: Cambiar contraseña

Permite a los supervisores modificar su contraseña.

### Caso de Prueba #1: Caso Normal - Cambio de contraseña exitoso con credenciales correctas

| Correo | Contraseña Anterior | Nueva Contraseña | Resultado |
|--------|---------------------|------------------|-----------|
| juan.perez@gmail.com | JuanP@123 | JuanP@456 | Contraseña actualizada |

### Caso de Prueba #2: Caso Normal - Cambio de contraseña con una clave fuerte

| Correo | Contraseña Anterior | Nueva Contraseña | Resultado |
|--------|---------------------|------------------|-----------|
| maria.lopez@gmail.com | Maria2024# | MariaFuerte2024! | Contraseña actualizada |

### Caso de Prueba #3: Caso Normal - Cambio de contraseña seguido de un inicio de sesión exitoso con la nueva clave

| Correo | Contraseña | Resultado |
|--------|------------|-----------|
| juan.perez@gmail.com | JuanP@456 | Sesión iniciada correctamente |

### Caso de Prueba #4: Caso Extremo - Cambio de contraseña con la más larga permitida

| Correo | Contraseña Anterior | Nueva Contraseña | Resultado |
|--------|---------------------|------------------|-----------|
| luis.gomez@gmail.com | Luis2023 | 32CaracteresLargos1234#@ | Contraseña actualizada |

### Caso de Prueba #5: Caso Extremo - Cambio de contraseña utilizando exclusivamente caracteres especiales

| Correo | Contraseña Anterior | Nueva Contraseña | Resultado |
|--------|---------------------|------------------|-----------|
| maria.lopez@gmail.com | Maria2024# | @#$%^&*()_+ | Contraseña actualizada |

### Caso de Prueba #6: Caso Extremo - Cambio de contraseña con caracteres especiales y números

| Correo | Contraseña Anterior | Nueva Contraseña | Resultado |
|--------|---------------------|------------------|-----------|
| carlos.r@gmail.com | Carlos2024# | C@rlos1234! | Contraseña actualizada |

### Caso de Prueba #7: Caso de Error - Intento de cambio de contraseña con la clave anterior incorrecta

| Correo | Contraseña Anterior | Nueva Contraseña | Error esperado |
|--------|---------------------|------------------|---------------|
| juan.perez@gmail.com | Incorrecta123 | JuanP@456 | "Contraseña anterior incorrecta" |

### Caso de Prueba #8: Caso de Error - Intento de cambio de contraseña con claves no coincidentes

| Correo | Contraseña Anterior | Nueva Contraseña | Confirmación | Error esperado |
|--------|---------------------|------------------|--------------|---------------|
| luis.gomez@gmail.com | Luis2023 | LuisNuevo2024 | LuisDiferente2024 | "Las contraseñas no coinciden" |

### Caso de Prueba #9: Caso de Error - Intento de cambio de contraseña sin estar autenticado

| Correo | Contraseña Anterior | Nueva Contraseña | Error esperado |
|--------|---------------------|------------------|---------------|
| None | None | NuevaClave@2025 | "Usuario no autenticado" |






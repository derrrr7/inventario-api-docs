# Documentacion de API 
# Proyecto API RESTful - Documentación para Derwin Viera

Este proyecto implementa una API RESTful de Inventario documentada automáticamente con Swagger (drf-yasg).

## Documentación de la API
* **URL de Documentación Interactiva:** http://127.0.0.1:8000/swagger/

### Vista General de Endpoints
Se muestra la lista completa de endpoints generados a partir del ViewSet:

![Vista principal de la interfaz Swagger UI](docs/swagger_main.png) 

### Esquemas y Descripciones
Detalle del esquema de respuesta (código 201), incluyendo los metadatos de documentación (descripciones, tipos y restricciones de los campos):

![Esquema de respuesta 201 Created con descripciones](docs/esquema_201.png)

### Prueba de Navegabilidad
Prueba de ejecución del método POST que resultó en un código 201 Created, demostrando que la API funciona desde la documentación:

![Captura de la prueba de ejecución del método POST](docs/prueba_post.png)
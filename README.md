# 202314_experimento1_E13
Este experimento es desarollado por el equipo 13 de Arquitecturas Ágiles

# Microservicios:
Para el despliegue del experimento se debe ingresar a cada carpeta y subir los microservicios en los siguientes puertos.

1. Gestor de Ofertas:
   Se debe publicar en el puerto: falsk run - p 6901
2. Gestror Recurtos TI
   Se debe publicar en el puerto: falsk run - p 5901  
4. Motor de Emparejamiento 1:
   Se debe publicar en el puerto: falsk run - p 7901
5. Motor de Emparejamiento 2:
   Se debe publicar en el puerto: falsk run - p 7902
8. Motor de Emparejamiento 3:
   Se debe publicar en el puerto: falsk run - p 7903
9. Validador:
    Se debe publicar en el puerto: falsk run - p 8901
10. Cola de Validacion:
    Se debe activar el servidor redis-server
12. Notificador
    Conectarse a la cola de validación: celery -A notificador worker -l info -Q colaValidacion

# Ejecutar Experimento
Para la ejecución del experimento se debe hacer un request POST al endpoint de gestor ofertas http://localhost:6901/oferta enviandole un json con las siguientes variables:

   "descripcion" 
    "habilidad"
    "calificacionRequerida"
    "perfil"

Ejemplo:
<img width="856" alt="image" src="https://github.com/orsolarte4221/202314_experimento1_E13/assets/123704723/27263842-516c-4dcc-b48a-bbf2439734fb">

Ejemplo Respuesta:
Se devuelve la oferta como confirmación de que el registro en la base de datos ha sido exitoso.

Si el motor emparejamiento encuentra un recurso que se ajuste a la oferta, "idRecursoTI" tendrá un valor numérico, de lo contrario sera un valor Nulo.

<img width="697" alt="image" src="https://github.com/orsolarte4221/202314_experimento1_E13/assets/123704723/c48ed02b-ce25-4836-8ece-541f1b93b002">




   

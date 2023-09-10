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

   

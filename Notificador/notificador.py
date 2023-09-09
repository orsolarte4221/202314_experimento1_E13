from celery import Celery

celery_app= Celery(__name__, broker='redis://localhost:6379/0')

@celery_app.task(name='notificar')
# Funcion registrar log recibe los parámetros y los guarda en un archivo separado por comas (csv)
def notificar_csv(idOferta, falloHabilidad, falloPerfil, falloCalificacion, idRecursoTI, idMotor,statusMotor):
    with open('notificador.csv', 'a+') as file:
        file.write(f'{idOferta},{falloHabilidad},{falloPerfil},{falloCalificacion},{idRecursoTI},{idMotor},{statusMotor}\n')
    return True
   


    

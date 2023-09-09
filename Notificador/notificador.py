from celery import Celery
import datetime

celery_app= Celery(__name__, broker='redis://localhost:6379/0')

@celery_app.task(name='notificar')
# Funcion registrar log recibe los parámetros y los guarda en un archivo separado por comas (csv)
def notificar_csv(idEjecucionValidador,fallaIntroducida,idOferta, idRecursoTI, idMotor, statusMotor):
    # Obtener la fecha y hora actual en GMT-5
    fecha_hora_actual = datetime.datetime.now()
    
    # Crear una cadena con los nombres de las columnas
    nombres_columnas = "Fecha_Hora,IdOferta,IdRecursoTI,IdMotor,StatusMotor"

    # Verificar si el archivo ya existe, si no, crearlo e incluir los nombres de las columnas
    with open('notificador.csv', 'a+') as file:
        if file.tell() == 0:
            file.write(nombres_columnas + '\n')
        
        # Registrar los datos en el archivo CSV
        file.write(f'{idEjecucionValidador},{fecha_hora_actual},{fallaIntroducida},{idOferta},{idRecursoTI},{idMotor},{statusMotor}\n')
    
    return True
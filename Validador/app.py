from Validador import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import requests
from celery import Celery

#Integracion con la cola de mensajes
celery_app= Celery(__name__, broker='redis://localhost:6379/0')
@celery_app.task(name='notificar')
def notificar_csv(*args):
    pass



app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

class VistaVotacion(Resource):
    def get(self):

        #Lo que le llega en Json por parametro al puerto de ejecucion lo mandará
        #en el request a los motores de emparejamiento
        data = request.get_json()

        #Llamado a Motor Emparejamiento 1
        motor1 = requests.get('http://127.0.0.1:5001/emparejamiento', json=data)

        #Llamado a Motor Emparejamiento 2
        motor2 = requests.get('http://127.0.0.1:5001/emparejamiento', json=data)

        #Llamado a Motor Emparejamiento 3
        motor3 = requests.get('http://127.0.0.1:5001/emparejamiento', json=data)


        #Logica de  Validador

        #Envio de mensaje a la cola del log en formato json
        log = {
            "idOferta" : 2,
            "falloHabilidad" : False,
            "falloPerfil" : False,
            "falloCalificacion" : False,
            "idRecursoTI" : 3,
            "idMotor" : 1,
            "statusMotor" : "Normal",
            "idEjecucionValidador" : 1,
            "fallaIntroducida":False
        }
        #convertir log en una tupla para que vaya a la cola
        args=(
            log("idEjecucionValidador"),
            log("fallaIntroducida"),
            log["idOferta"],
            log["falloHabilidad"],
            log["falloPerfil"],
            log["falloCalificacion"],
            log["idRecursoTI"],
            log["idMotor"],
            log["statusMotor"])
        #enviar a la cola    
        notificar_csv.apply_async(args, queue='colaValidacion')


        #Retornar IdRecursoIT
        return "IdRecursoIT" #content.json()
    
#Suponiendo que este microservicio corre en el puerto 5002, al hacer un llamado a ese puerto
#al endpoint /emparejamiento se ejecutara lo que se encuentra en la vista votacion
api.add_resource(VistaVotacion, '/emparejamiento') 
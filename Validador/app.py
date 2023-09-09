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

contadorEjecucion = 1

class VistaVotacion(Resource):
    def get(self):

        #Lo que le llega en Json por parametro al puerto de ejecucion lo mandará
        #en el request a los motores de emparejamiento
        data = request.get_json()


        #Llamado a Motor Emparejamiento 1
        motor1 = requests.get('http://127.0.0.1:7901/emparejamiento', json=data)

        #Llamado a Motor Emparejamiento 2
        motor2 = requests.get('http://127.0.0.1:7902/emparejamiento', json=data)

        #Llamado a Motor Emparejamiento 3
        motor3 = requests.get('http://127.0.0.1:7903/emparejamiento', json=data)


        #Logica de  Validador
        
        def encontrar_recurso(motor1_id,motor2_id,motor3_id):
            if motor1_id == motor2_id and motor2_id != motor3_id:
                motor1['statusMotor':'Normal']
                motor2['statusMotor':'Normal']
                motor3['statusMotor':'Fallando']
                return motor1_id
            elif motor1_id == motor3_id and motor2_id != motor3_id:
                motor1['statusMotor':'Normal']
                motor2['statusMotor':'Fallando']
                motor3['statusMotor':'Normal']                
                return motor1_id
            else:
                motor1['statusMotor':'Fallando']
                motor2['statusMotor':'Normal']
                motor3['statusMotor':'Normal']    
                return motor2_id
            
        motor1_id = motor1.json()['IdRecurso']
        motor2_id = motor2.json()['IdRecurso']
        motor3_id = motor3.json()['IdRecurso']

        idRecursoIT = encontrar_recurso(motor1_id,motor2_id,motor3_id)

        for motor in [motor1,motor2,motor3]:
           

            #Envio de mensaje a la cola del log en formato json
            log = {
                "idOferta" : data['idOferta'],
                "idRecursoTI" : motor['IdRecurso'],
                "idMotor" : motor["IdentificadorMotor"],
                "statusMotor" : motor['statusMotor'],
                "idEjecucionValidador" : contadorEjecucion,
                "fallaIntroducida":motor['fallaIntroducida']
            }
            #convertir log en una tupla para que vaya a la cola
            args=(
                log("idEjecucionValidador"),
                log("fallaIntroducida"),
                log["idOferta"],
                log["idRecursoTI"],
                log["idMotor"],
                log["statusMotor"])
            #enviar a la cola    
            notificar_csv.apply_async(args, queue='colaValidacion')

        contadorEjecucion+=1

        #Retornar IdRecursoIT
        if idRecursoIT.isnumeric():
            return {"idRecursoIT":idRecursoIT} 
        else:
            return {"message":"No hay recursos disponibles para la oferta"}
    
#Suponiendo que este microservicio corre en el puerto 5002, al hacer un llamado a ese puerto
#al endpoint /emparejamiento se ejecutara lo que se encuentra en la vista votacion
api.add_resource(VistaVotacion, '/emparejamiento') 
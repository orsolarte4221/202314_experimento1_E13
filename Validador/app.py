from Validador import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import requests


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



        #Retornar IdRecursoIT
        return "IdRecursoIT" #content.json()
    
#Suponiendo que este microservicio corre en el puerto 5002, al hacer un llamado a ese puerto
#al endpoint /emparejamiento se ejecutara lo que se encuentra en la vista votacion
api.add_resource(VistaVotacion, '/emparejamiento') 
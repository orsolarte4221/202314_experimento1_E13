from MotorEmparejamiento3 import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import requests
import json
import random
import json

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

class VistaEmparejamiento(Resource):
    def get(self):
        oferta = request.get_json()

        if oferta.status_code == 404:
            return "No existe la oferta", 404
        else:
            habilidad = oferta.json()["habilidad"]
            calificacionRequerida = oferta.json()["calificacionRequerida"]
            perfil = random.randint(1, 4)

            response = requests.get('http://127.0.0.1:5000/recursosTI')

            if response.status_code == 404:
                return "No se encontraron recursos", 404

            recursos_ti = response.json()

            primer_recurso = next((recurso for recurso in recursos_ti if recurso.get("perfil") == perfil and recurso.get("habilidad") == habilidad and recurso.get("calificacionRequerida", 0) <= calificacionRequerida), None)

            if primer_recurso:
                recurso_id = primer_recurso.get("id")
                return {"IdRecurso":recurso_id, "IdentificadorMotor":1}, 200
            else:
                return {"IdRecurso":"No se encontraron recursos para la oferta", "IdentificadorMotor":1}, 404


api.add_resource(VistaEmparejamiento, '/emparejamiento')
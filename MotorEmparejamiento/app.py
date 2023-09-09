from MotorEmparejamiento import create_app
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


# definir la url global

def cargar_configuracion():
    try:
        with open('config.json', 'r') as archivo_config:
            configuracion = json.load(archivo_config)
            return configuracion
    except FileNotFoundError:
        print("El archivo de configuración 'config.json' no se encontró.")
        return None

configuracion = cargar_configuracion()
if configuracion:
    URL_GLOBAL = configuracion.get('url')
else:
    URL_GLOBAL = 'http://127.0.0.1:5000/'


class VistaEmparejamiento1(Resource):
    def get(self, id_oferta):
        oferta = requests.get(URL_GLOBAL + '/oferta/{}'.format(id_oferta))

        if oferta.status_code == 404:
            return "No existe la oferta", 404
        else:
            habilidad = oferta.json()["habilidad"]
            calificacionRequerida = oferta.json()["calificacionRequerida"]
            perfil = oferta.json()["perfil"]

            response = requests.get(URL_GLOBAL + '/recursosTI')

            if response.status_code == 404:
                return "No se encontraron recursos", 404

            recursos_ti = response.json()

            primer_recurso = next((recurso for recurso in recursos_ti if recurso.get("perfil") == perfil and recurso.get("habilidad") == habilidad and recurso.get("calificacionRequerida", 0) <= calificacionRequerida), None)

            if primer_recurso:
                recurso_id = primer_recurso.get("id")
                return {"IdRecurso":recurso_id, "IdentificadorMotor":1}, 200
            else:
                return {"IdRecurso":"No se encontraron recursos para la oferta", "IdentificadorMotor":1}, 404


api.add_resource(VistaEmparejamiento1, '/emparejamiento1')

class VistaEmparejamiento2(Resource):
    def get(self, id_oferta):
        oferta = requests.get(URL_GLOBAL + '/oferta/{}'.format(id_oferta))

        if oferta.status_code == 404:
            return "No existe la oferta", 404
        else:
            habilidad = random.randint(1, 5)
            calificacionRequerida = oferta.json()["calificacionRequerida"]
            perfil = random.randint(1, 4)

            response = requests.get(URL_GLOBAL + '/recursosTI')

            if response.status_code == 404:
                return "No se encontraron recursos", 404

            recursos_ti = response.json()

            primer_recurso = next((recurso for recurso in recursos_ti if recurso.get("perfil") == perfil and recurso.get("habilidad") == habilidad and recurso.get("calificacionRequerida", 0) <= calificacionRequerida), None)

            if primer_recurso:
                recurso_id = primer_recurso.get("id")
                return {"IdRecurso":recurso_id, "IdentificadorMotor":2}, 200
            else:
                return {"IdRecurso":"No se encontraron recursos para la oferta", "IdentificadorMotor":2}, 404


api.add_resource(VistaEmparejamiento2, '/emparejamiento2')


class VistaEmparejamiento3(Resource):
    def get(self, id_oferta):
        oferta = requests.get(URL_GLOBAL + '/oferta/{}'.format(id_oferta))

        if oferta.status_code == 404:
            return "No existe la oferta", 404
        else:
            habilidad = oferta.json()["habilidad"]
            calificacionRequerida = oferta.json()["calificacionRequerida"]
            perfil = random.randint(1, 4)

            response = requests.get(URL_GLOBAL + '/recursosTI')

            if response.status_code == 404:
                return "No se encontraron recursos", 404

            recursos_ti = response.json()

            primer_recurso = next((recurso for recurso in recursos_ti if recurso.get("perfil") == perfil and recurso.get("habilidad") == habilidad and recurso.get("calificacionRequerida", 0) <= calificacionRequerida), None)

            if primer_recurso:
                recurso_id = primer_recurso.get("id")
                return {"IdRecurso":recurso_id, "IdentificadorMotor":3}, 200
            else:
                return {"IdRecurso":"No se encontraron recursos para la oferta", "IdentificadorMotor":3}, 404


api.add_resource(VistaEmparejamiento3, '/emparejamiento3')
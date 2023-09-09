from MotorEmparejamiento1 import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import requests
import json
import random

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

class VistaEmparejamiento(Resource):
    def get(self):
        oferta = request.get_json()
        habilidadRequerida = oferta.json()["habilidad"]
        calificacionRequerida = oferta.json()["calificacionRequerida"]
        perfilRequerido = oferta.json()["perfil"]

        if habilidadRequerida is None or calificacionRequerida is None or perfilRequerido is None:
             return "Error en la solicitud, informacion incompleta", 404
        else:
            response = requests.get('http://127.0.0.1:5000/recursosTI')

            if response.status_code == 404:
                return "No se encontraron recursos", 404

            recursos_ti = response.json()
            recursoEncontrado=False
            fallaIntroducida = False
            
            if not fallaIntroducida:
                #Logica para encontrar recurso adecuado
                for recurso in recursos_ti:
                    perfil = recurso['perfilRecurso']
                    habilidades = recurso['habilidades']
                    if perfil == perfilRequerido:
                        for habilidad in habilidades:
                            if habilidad['nombreHabilidad'] == habilidadRequerida and habilidad['calificacionHabilidad'] == calificacionRequerida:
                                recursoEncontrado = True
                                break
                        
                        if recursoEncontrado:
                            primer_recurso = recurso
                            contadorEjecucion+=1
                            break

            if primer_recurso:
                recurso_id = primer_recurso['id']
                return {"IdRecurso":recurso_id, "IdentificadorMotor":3, "fallaIntroducida": fallaIntroducida}, 200
            else:
                return {"IdRecurso":"No se encontraron recursos para la oferta", "IdentificadorMotor":3}, 404

api.add_resource(VistaEmparejamiento, '/emparejamiento')
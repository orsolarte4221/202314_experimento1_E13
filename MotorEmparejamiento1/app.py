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
        habilidadRequerida = oferta["habilidad"]
        calificacionRequerida = oferta["calificacionRequerida"]
        perfilRequerido = oferta["perfil"]

        if habilidadRequerida is None or calificacionRequerida is None or perfilRequerido is None:
             return "Error en la solicitud, informacion incompleta", 404
        else:
            response = requests.get('http://127.0.0.1:5901/recursoti')

            if response.status_code == 404:
                return "No se encontraron recursos", 404

            recursos_ti = response.json()
            recursoEncontrado=False
            fallaIntroducida = False
            primer_recurso = False
            
            if not fallaIntroducida:
                #Logica para encontrar recurso adecuado
                for recurso in recursos_ti:
                    perfil = recurso['perfilRecurso']['llave']
                    #print({"Perfil":perfil,"PerfilRequerido":perfilRequerido})
                    habilidades = recurso['habilidades']
                    if perfil == perfilRequerido:
                        for habilidad in habilidades:
                            if habilidad['nombreHabilidad']['llave'] == habilidadRequerida and habilidad['calificacionHabilidad'] >= calificacionRequerida:
                                recursoEncontrado = True
                                break
                        
                    if recursoEncontrado:
                        primer_recurso = recurso
                        break

            if primer_recurso:
                print(primer_recurso)
                recurso_id = primer_recurso['id']
                return {"IdRecurso":recurso_id, "IdentificadorMotor":1, "fallaIntroducida": fallaIntroducida}, 200
            else:
                return {"IdRecurso":"No se encontraron recursos para la oferta", "IdentificadorMotor":3, "fallaIntroducida": fallaIntroducida}, 404

api.add_resource(VistaEmparejamiento, '/emparejamiento')
from flaskr import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import requests
from .modelos import db, Oferta, Habilidad, Perfil, RecursoTI, Habilidades

app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()

api = Api(app)


# Ejemplo! Esto puede ser Borrado después
#Para que el ejemplo funcione esto debe estar corriendo en el puerto 5001
class VistaPrincipal(Resource):
    def get(self):
        return request.get_json()

api.add_resource(VistaPrincipal, '/emparejamiento') 

#Acaba el ejemplo para probar Microservicio Votación
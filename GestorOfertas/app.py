from flaskr import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import requests
from .modelos import db, Oferta, Habilidad, Perfil, RecursoTI, Habilidades
from vistas import VistaGestorOfertas

app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()

api = Api(app)


api.add_resource(VistaGestorOfertas, '/oferta') 
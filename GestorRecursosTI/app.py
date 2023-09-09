from flaskr import create_app
from flask_restful import Resource, Api
from flask import Flask, request
from .modelos import *
from .vistas import VistaRecursoTI

app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaRecursoTI, '/recursoti')
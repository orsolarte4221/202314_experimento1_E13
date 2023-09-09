from flaskr import create_app
from flask_restful import Resource, Api
from flask import Flask, request
<<<<<<< HEAD
import requests
from .modelos import db, Oferta, Habilidad, Perfil, RecursoTI, Habilidades
from vistas import VistaGestorOfertas
=======
from .modelos import db, Oferta, Habilidad, Perfil, RecursoTI, Habilidades
>>>>>>> c74ae6ce6253c740b46a773c9e842a92614a83ce

app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()

<<<<<<< HEAD
api = Api(app)


api.add_resource(VistaGestorOfertas, '/oferta') 
=======
api = Api(app)
>>>>>>> c74ae6ce6253c740b46a773c9e842a92614a83ce

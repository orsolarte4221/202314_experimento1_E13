from flask import request
import requests
from .modelos import db, Oferta, OfertaSchema, Perfil, Habilidad
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

oferta_schema = OfertaSchema()

class VistaGestorOfertas(Resource):

    def post(self):
        #Se crea una nueva oferta
        nueva_oferta = Oferta(perfil=request.json["perfil"], habilidad=request.json["habilidad"],  calificacionRequerida=request.json["calificacionRequerida"], descripcion=request.json["descripcion"])
        
    
        oferta = request.get_json()
        #Se asigna un recurso a la oferta llamando al validador
        idRecursoTIAsignado = requests.get('http://127.0.0.1:8901/emparejamiento', oferta)   

        if 'IdRecursoIT' in idRecursoTIAsignado.json():
            nueva_oferta.idRecursoTI=idRecursoTIAsignado.json()['IdRecursoIT']
        else:
            #No se encontro un recureso para la oferta
            print("No se encontro un recureso para la oferta")
            nueva_oferta.idRecursoTI=None

        db.session.add(nueva_oferta)
        db.session.commit()
        return oferta_schema.dump(nueva_oferta)
       
    def get(self, id_oferta):
        oferta = Oferta.query.get_or_404(id_oferta)
        return [oferta_schema.dump(id_oferta)]



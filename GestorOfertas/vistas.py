from flask import request
from .modelos import db, Oferta, OfertaSchema, Perfil, Habilidad
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

oferta_schema = OfertaSchema()

class VistaGestorOfertas(Resource):

    def post(self, id_oferta):
        oferta = Oferta.query.get_or_404(id_oferta)
        
        if "id_oferta" in request.json.keys():
            
            nueva_oferta = Oferta.query.get(request.json["id_oferta"])
            if nueva_oferta is not None:
                oferta.append(nueva_oferta)
                db.session.commit()
            else:
                return 'Oferta Erronea',404
        else: 
            nueva_oferta = Oferta(id=request.json["id"], perfil=request.json["perfil"], habilidades=request.json["habilidades"],  calificacionRequerida=request.json["calificacionRequerida"], descripción=request.json["descripción"], idRecursoTI=request.json["idRecursoTI"])
            oferta.append(nueva_oferta)
        db.session.commit()
        return oferta_schema.dump(nueva_oferta)
       
    def get(self, id_oferta):
        oferta = Oferta.query.get_or_404(id_oferta)
        return [oferta_schema.dump(id_oferta)]



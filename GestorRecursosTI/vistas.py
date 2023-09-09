from flask import request
from .modelos import db, RecursoTI, RecursoTISchema, Perfil, Habilidad
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

recursoTI_schema = RecursoTISchema()


class VistaRecursoTI(Resource):

    def post(self, id_recursoTI):
        recursoTI = RecursoTI.query.get_or_404(id_recursoTI)
        
        if "id_recursoTI" in request.json.keys():
            
            nuevo_recursoTI = RecursoTI.query.get(request.json["id_recurstoTI"])
            if nuevo_recursoTI is not None:
                recursoTI.append(nuevo_recursoTI)
                db.session.commit()
            else:
                return 'RecursoTI Erroneo',404
        else: 
            nuevo_recursoTI = RecursoTI(id=request.json["id"], nombreRecurso=request.json["nombreRecurso"], perfilRecurso=request.json["perfilRecurso"], habilidades=request.json["habilidades"])
            recursoTI.append(nuevo_recursoTI)
        db.session.commit()
        return recursoTI_schema.dump(nuevo_recursoTI)
       
    def get(self, id_recursoTI):
        recursoTI = RecursoTI.query.get_or_404(id_recursoTI)
        return [recursoTI_schema.dump(id_recursoTI)]



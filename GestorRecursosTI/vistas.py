from flask import request
from .modelos import db, RecursoTI, RecursoTISchema, Perfil, Habilidad , Habilidades
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

recursoTI_schema = RecursoTISchema()


class VistaRecursoTI(Resource):
    def post(self):
        # Obtener los datos JSON de la solicitud
        data = request.json

        # Crear un nuevo recurso de TI
        nuevo_recurso = RecursoTI(
            nombreRecurso=data['nombreRecurso'],
            perfilRecurso=data['perfilRecurso']
        )

        # Crear habilidades asociadas al recurso
        for habilidad_data in data['habilidades']:
            nueva_habilidad = Habilidades(
                nombreHabilidad=habilidad_data['nombreHabilidad'],
                calificacionHabilidad=habilidad_data['calificacionHabilidad']
            )
            nuevo_recurso.habilidades.append(nueva_habilidad)

        # Agregar y guardar el nuevo recurso en la base de datos
        db.session.add(nuevo_recurso)
        db.session.commit()
        return nuevo_recurso, 201
       
    def get(self):
        return [recursoTI_schema.dump(RecursoTi) for RecursoTi in RecursoTI.query.all()]   
        



from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
import enum


db = SQLAlchemy()

class Perfil(enum.Enum):
   BACKEND = 1
   FRONTEND = 2
   ARQUITECTO = 3
   PRUEBAS = 4


class Habilidad(enum.Enum):
   PYTHON = 1
   FLASK = 2
   SQL = 3
   ANGULAR = 4
   JAVA = 5

class EnumADiccionario(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {"llave": value.name, "valor": value.value}


class RecursoTI(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombreRecurso = db.Column(db.String(128))
    perfilRecurso = db.Column(db.Enum(Perfil))
    habilidades = db.relationship('Habilidades')
    
class Habilidades(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombreHabilidad = db.Column(db.Enum(Habilidad))
    calificacionHabilidad = db.Column(db.Integer)
    recursoti=db.Column(db.Integer, db.ForeignKey('recursoTI.id'))

class HabilidadesSchema(SQLAlchemyAutoSchema):
    nombreHabilidad = EnumADiccionario(attribute=("nombreHabilidad"))
    class Meta:
        model = Habilidades
        include_relationships = True
        load_instance = True      


class RecursoTISchema(SQLAlchemyAutoSchema):
    perfilRecurso = EnumADiccionario(attribute=("perfilRecurso"))
    habilidades = fields.Nested('HabilidadesSchema', many=True)   

    class Meta:
         model = RecursoTI
         include_relationships = True
         load_instance = True   
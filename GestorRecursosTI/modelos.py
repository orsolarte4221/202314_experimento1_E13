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


class RecursoTI(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombreRecurso = db.Column(db.String(128))
    perfilRecurso = db.Column(db.Enum(Perfil))
    habilidades = db.relationship('Habilidades')


class EnumADiccionario(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {"llave": value.name, "valor": value.value}
    

class RecursoTISchema(SQLAlchemyAutoSchema):
    habilidad = EnumADiccionario(attribute=("habilidad"))
    perfil = EnumADiccionario(attribute=("perfil"))
    class Meta:
         model = RecursoTI
         include_relationships = True
         load_instance = True
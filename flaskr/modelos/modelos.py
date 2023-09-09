from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()

class Habilidad(enum.Enum):
   PYTHON = 1
   FLASK = 2
   SQL = 3
   ANGULAR = 4
   JAVA = 5

class Perfil(enum.Enum):
   BACKEND = 1
   FRONTEND = 2
   ARQUITECTO = 3
   PRUEBAS = 4


class Oferta(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(256))
    habilidad = db.Column(db.Enum(Habilidad))
    calificacionRequerida = db.Column(db.Integer)
    perfil = db.Column(db.Enum(Perfil))
    idRecursoTI = db.Column(db.Integer, nullable=True)
    

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
    

class Status(enum.Enum):
    FALLANDO = 1
    NORMAL = 2

class Log():
    idOferta: int
    falloHabilidad:bool
    falloPerfil:bool
    falloCalificacion:bool
    idRecursoTI:int
    idMotor:int
    statusMotor:Status  
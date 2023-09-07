from flaskr import create_app
from .modelos import db, Oferta, Habilidad, Perfil

app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()

miPrimerOferta = Oferta(descripcion="Desarrollador Python", habilidad=Habilidad.PYTHON, calificacionRequerida=3, perfil=Perfil.BACKEND)
db.session.add(miPrimerOferta)
db.session.commit()
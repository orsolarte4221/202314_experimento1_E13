from flaskr import create_app
from .modelos import db, Oferta, Habilidad, Perfil, RecursoTI, Habilidades

app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()

miPrimerOferta = Oferta(descripcion="Desarrollador Python", habilidad=Habilidad.PYTHON, calificacionRequerida=3, perfil=Perfil.BACKEND)
db.session.add(miPrimerOferta)
db.session.commit()

recursoTi1 = RecursoTI(nombreRecurso="Gustavo", perfilRecurso=Perfil.BACKEND)
recursoTi1.habilidades.append(Habilidades(nombreHabilidad=Habilidad.PYTHON, calificacionHabilidad=3))
recursoTi1.habilidades.append(Habilidades(nombreHabilidad=Habilidad.JAVA, calificacionHabilidad=2))

db.session.add(recursoTi1)
db.session.commit()

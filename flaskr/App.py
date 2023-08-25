from flaskr import create_app
from .modelos import db, Cancion
from .modelos import db, Album
from .modelos import db, Medios

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#Prueba
with app.app_context():
    c=Cancion(titulo='Bajan',minutos=2, segundos=25, interprete='Pescado Rabioso')
    db.session.add(c)
    db.session.commit()
    print(Cancion.query.all())

    al=Album(titulo='Artaud', año=1973, descripcion='Luis Alberto Spinetta', medio='DISCO')
    db.session.add(al)
    db.session.commit()
    print(Album.query.all())


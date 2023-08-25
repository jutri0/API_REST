from flaskr import create_app
from .modelos import db, Cancion
from .modelos import db, Album
from .modelos import db, Medios
from .modelos import db, Usuario

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#Prueba
with app.app_context():
    u=Usuario(nombre_usuario='Juan',contrasena='1234')
    c=Cancion(titulo='Bajan', minutos=5, segundos=45, interprete='Spinetta')
    al=Album(titulo='Artaud', año=1973, descripcion='After Pescado Rabioso', medio='DISCO')
    u.albumes.append(al)
    al.canciones.append(c)
    db.session.add(u)
    db.session.add(c)
    db.session.commit()
    print(Album.query.all())
    print(Album.query.all()[0].canciones)
    print(Cancion.query.all())
    db.session.delete(al)
    print(Album.query.all())
    print(Cancion.query.all())



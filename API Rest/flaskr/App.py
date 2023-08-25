from flaskr import create_app
from .modelos import db, Usuario, Album, Medios
from .modelos import AlbumSchema

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#Prueba
with app.app_context():
    Album_Schema = AlbumSchema()
    al = Album(titulo='Artaud', anio=1973, descripcion='After Pescado Rabioso', medio=Medios.DISCO)
    db.session.add(al)
    db.session.commit()
    print([Album_Schema.dumps(album) for album in Album.query.all()])





from flaskr import create_app
from .modelos import db, Cancion

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#Prueba
with app.app_context():
    c=Cancion(titulo='Puentes Amarillos',minutos=2, segundos=25, interprete='Pescado Rabioso')
    db.session.add(c)
    db.session.commit()
    print(Cancion.query.all())
from flaskr import create_app
from .modelos import db, Cancion, Usuario, Album, Medios
from flask_restful import Api, Resource
from .vistas import VistaCanciones, VistaCancion

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaCanciones,'/canciones')
api.add_resource(VistaCanciones,'/canciones/<init:id_cancion>')

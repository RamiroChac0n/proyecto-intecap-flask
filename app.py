
from flask import Flask
from src.common.utils import db, api, ma, jwt
from src.routes.routes import General_Routes


def crear_aplicacion():
    app = Flask(__name__)




    app.config.from_object("configuracion.Configuracion")



    db.init_app(app)
    api.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    #iniciar las rutas
    with app.app_context():
        General_Routes(api)

    return app

app = crear_aplicacion()
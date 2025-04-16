from flask import Flask, redirect, request
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os
from importlib import import_module




db = SQLAlchemy()
login_manager = LoginManager()


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)



def register_blueprints(app):
    if not app.config['DEBUG']:
        @app.before_request
        def before_request():
            if request.scheme != 'https':
                return redirect(request.url.replace('http://', 'https://'))


    # Rutas de la apliación a añadir en blueprints
    rutas_blueprints = ['usuarios', 'home']
    for module_name in (rutas_blueprints):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)



def configure_database(app):
    try:
        with app.app_context():
            db.create_all()
    
    except Exception as e:
        print('> Error: DBMS Exception: ' + str(e) )

        # fallback to SQLite
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')

        print('> Fallback to SQLite ')
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()





# Creamos la apliación Flask, configuramos y registramos las extensiones, blueprints y la base de datos
def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    
    return app
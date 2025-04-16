import os, random, string

#  Obtención de variables de entorno del fichero config.env
from dotenv import load_dotenv

load_dotenv('config.env')
#  ------------------------------------------------


# WARNING: Don't run with debug turned on in production!
DEBUG = (os.getenv('DEBUG', 'False') == 'True')




class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))    # Directorio base de la aplicación

    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static')

    # Set up the App SECRET_KEY
    SECRET_KEY  = os.getenv('SECRET_KEY', None)

    if not SECRET_KEY:
        SECRET_KEY = ''.join(random.choice( string.ascii_lowercase  ) for i in range( 32 ))    

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB_ENGINE   = os.getenv('DB_ENGINE'   , None)
    DB_USERNAME = os.getenv('DB_USERNAME' , None)
    DB_PASS     = os.getenv('DB_PASS'     , None)
    DB_HOST     = os.getenv('DB_HOST'     , None)
    DB_PORT     = os.getenv('DB_PORT'     , None)
    DB_NAME     = os.getenv('DB_NAME'     , None)

    USE_SQLITE  = True 

    # try to set up a Relational DBMS
    if DB_ENGINE and DB_NAME and DB_USERNAME:
        try:
            # Relational DBMS: PSQL, MySql
            SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
                DB_ENGINE,
                DB_USERNAME,
                DB_PASS,
                DB_HOST,
                DB_PORT,
                DB_NAME   ) 

            USE_SQLITE = False

        except Exception as e:
            print('> Error: DBMS Exception: ' + str(e) )
            print('> Fallback to SQLite ')    

    if USE_SQLITE:
        SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
        
        if not SQLALCHEMY_DATABASE_URI:
            # This will create a file in <app> FOLDER
            SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3') 



# Creamos configuración para el entorno de PRODUCCIÓN, Config + DEBUG + SEGURIDAD
class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600


# Creamos configuración para el entorno de DESARROLLO, Config + DEBUG
class DebugConfig(Config):
    DEBUG = True



# Diccionario con las posibles configuraciones
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
    }
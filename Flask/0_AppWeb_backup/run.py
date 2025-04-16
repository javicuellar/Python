from flask_migrate import Migrate
from flask_minify  import Minify

from app.config import config_dict, DEBUG
from app import create_app, db




# Coniguración de la aplicación
get_config_mode = 'Debug' if DEBUG else 'Production'

try:
    # Cargamos la configuración de la aplicación
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')


app = create_app(app_config)
Migrate(app, db)


if not DEBUG:
    Minify(app=app, html=True, js=False, cssless=False)
    
if DEBUG:
    app.logger.info('DEBUG            = ' + str(DEBUG)             )
    app.logger.info('Page Compression = ' + 'FALSE' if DEBUG else 'TRUE' )
    app.logger.info('DBMS             = ' + app_config.SQLALCHEMY_DATABASE_URI)
    app.logger.info('ASSETS_ROOT      = ' + app_config.ASSETS_ROOT )





if __name__ == "__main__":
    if DEBUG:
        # Pruebas en PC local
        app.run(port=5015)
    else:
        # Producción en NAS Synology
        # En el navegador -> http://javicu.synology.me:5010/login  o  http://192.168.1.41:5010/login
        # app.run(host="192.168.1.41", port=5010, debug=True)
        # no poner como host "javicu.synology.me", ni localhost, no han funcionado

        # Conexión segura https para el NAS
        app.run(ssl_context=('cert.pem', 'privkey.pem'),host="192.168.1.41", port=5010)

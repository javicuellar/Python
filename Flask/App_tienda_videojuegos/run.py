# import sys
# sys.path.insert(0, '/var/www/html/tienda_videojuegos')

from aplicacion.app import app as application


if __name__ == "__main__":
    application.run(port=5004)

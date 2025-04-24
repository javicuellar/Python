import sys
sys.path.insert(0, '/var/www/html/tienda_videojuegos')
activate_this = '/home/ubuntu/venv/flask/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from aplicacion.app import app as application

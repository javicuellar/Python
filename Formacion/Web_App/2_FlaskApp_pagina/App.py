#  Creando una Página Principal

from flask import Flask
from flask import render_template   # Importar de directorio templates -> index.html



app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


#  No sale bonito porque faltan estas referencias de index.html
# <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">
# <link href="http://getbootstrap.com/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet"


@app.route("/showSignUp")
def showSignUp():
    return "Bienvenido a SignUp."



if __name__ == "__main__":
    app.run()                   # En el navegador -> http://localhost:5000/  o  http://127.0.0.1:5000
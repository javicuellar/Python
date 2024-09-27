from flask import Flask


app = Flask(__name__)


@app.route("/")
def main():
    return "Bienvenido."



if __name__ == "__main__":
    app.run()                   # En el navegador -> http://localhost:5000/  o  http://127.0.0.1:5000
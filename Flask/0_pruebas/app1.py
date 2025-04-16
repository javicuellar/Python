from flask import Flask
from flask import request, render_template, redirect, url_for
from flask import session
from flask import make_response
from blueprints.auth import auth_bp
from blueprints.user import user_bp
from blueprints.admin import admin_bp



app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '¡Hola, Mundo!'


# Rutas con parámetros -> falta el tipo de la variable, por defecto es string.
@app.route('/usuario/<nombre>')
def mostrar_usuario(nombre):
    return f'Hola, {nombre}!'

# Rutas con parámetros -> Tipos de variables: string (por defecto), int, float, path, uuid.
@app.route('/post/<int:id>')
def mostrar_post(id):
    return f'Este es el post con ID: {id}'



# Métodos HTTP:  GET (obtener datos), POST (enviar datos), PUT (actualizar datos), DELETE (eliminar datos).
# from flask import request
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Procesar datos del formulario
        return 'Datos del formulario recibidos'
    else:
        # Mostrar formulario de login
        return 'Formulario de login'

@app.route('/buscar') 
def buscar(): 
    termino = request.args.get('q') 
    if termino: 
        return f'Resultados para: {termino}' 
    else: 
        return 'Introduce un término de búsqueda'


# Uso de jinja2 para renderizar plantillas HTML, con variables y estructuras de control.
# from flask import render_template
@app.route('/perfil')
def perfil_usuario():
    usuario = {'nombre': 'Juan Pérez', 'email': 'juan@ejemplo.com'}
    return render_template('perfil.html', usuario=usuario)


# formularios: etiqueta, métodos GET y POST, Campos de entrada (, <textarea>, ). Botón de envío (, ).
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        # Procesar los datos (guardar en base de datos, etc.)
        return redirect(url_for('registro_exito', nombre=nombre))
    return render_template('registro.html')

@app.route('/registro/exito/<nombre>')
def registro_exito(nombre):
    return f'¡Registro exitoso, {nombre}!'



# Manejo de sesiones
# from flask import session, redirect, url_for
@app.route('/login_usuario', methods=['POST'])
def login_usuario():
    # ... Autenticación del usuario ...
    session['usuario_id'] = usuario.id
    session['nombre_usuario'] = usuario.nombre
    return redirect(url_for('pagina_protegida'))

@app.route('/logout')
def logout():
    session.pop('usuario_id', None)
    session.pop('nombre_usuario', None)
    return redirect(url_for('inicio'))

@app.route('/protegida')
def pagina_protegida():
    if 'usuario_id' in session:
        return f'Bienvenido, {session["nombre_usuario"]}!'
    return redirect(url_for('login'))


# Trabajando con cookies
# from flask import make_response
@app.route('/establecer_cookie')
def establecer_cookie():
    respuesta = make_response("Cookie establecida")
    respuesta.set_cookie('mi_cookie', 'valor_cookie', max_age=3600)
    return respuesta

@app.route('/obtener_cookie')
def obtener_cookie():
    valor = request.cookies.get('mi_cookie')
    return f'El valor de la cookie es: {valor}'


# Ejemplo uso blueprints (modulo de ejemplo en carpeta blueprints)
# from blueprints.auth import auth_bp

# app = Flask(__name__)
# app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)





if __name__ == '__main__':
    app.run(debug=True)
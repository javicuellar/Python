#      Aplicación Web creada por la IA Aria en python, Flask y SQULite
#
#      Instalación de paquetes necesarios
#
#  $ pip install Flask    Flask-SQLAlchemy    Flask-Login

#  A partir de la aplicación creada, voy a incorporar la CRUD_APP (cambiando MYSQL por SQLite)

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user



app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'


db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)



class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)



# @app.before_request
# def before_request():
#     if request.scheme != 'https':
#         return redirect(request.url.replace('http://', 'https://'))


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        usuario = Usuario.query.filter_by(username=username, password=password).first()
        if usuario:
            login_user(usuario)
            return redirect(url_for('usuarios'))
            # return redirect(url_for('estudiantes'))
        else:
            flash('Credenciales incorrectas.')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        nuevo_usuario = Usuario(username=username, password=password)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Usuario registrado exitosamente. Puedes iniciar sesión.')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/usuarios')
@login_required
def usuarios():
    usuarios = Usuario.query.all()
    return render_template('users.html', usuarios=usuarios)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_user(id):
    usuario = Usuario.query.get_or_404(id)
    if request.method == 'POST':
        usuario.username = request.form['username']
        usuario.password = request.form['password']
        db.session.commit()
        flash('Usuario actualizado exitosamente.')
        return redirect(url_for('usuarios'))
    return render_template('edit_user.html', usuario=usuario)


@app.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_user(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    flash('Usuario eliminado exitosamente.')
    return redirect(url_for('usuarios'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))



# ------------------------------------------------------------------------------------

#  Tratamiento Estudiantes = CRUD

class Estudiantes(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)



@app.route('/estudiantes')
def estudiantes():
    estudiantes = Estudiantes.query.all()
    return render_template('estudiantes.html', estudiantes=estudiantes)


@app.route('/estudiantes/alta', methods = ['POST'])
def estudiantes_alta():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        nuevo_estudiante = Estudiantes(name=name, email=email, phone=phone)
        db.session.add(nuevo_estudiante)
        db.session.commit()
        flash("Data Inserted Successfully")
        return redirect(url_for('estudiantes'))

@app.route('/estudiantes/borrar/<string:id_data>', methods = ['GET'])
def estudiantes_borrar(id_data):
    estudiante = Estudiantes.query.get_or_404(id_data)
    db.session.delete(estudiante)
    db.session.commit()
    flash("Record Has Been Deleted Successfully")
    return redirect(url_for('estudiantes'))

@app.route('/estudiantes/actualizar', methods= ['POST', 'GET'])
def estudiantes_actualizar():
    if request.method == 'POST':
        id_data = request.form['id']
        estudiante = Estudiantes.query.get_or_404(id_data) 
        estudiante.name = request.form['name']
        estudiante.email = request.form['email']
        estudiante.phone = request.form['phone']
        db.session.commit()
        # print(f"Registro actualizado: {estudiante.name}, {estudiante.email}, {estudiante.phone}")
        flash("Data Updated Successfully")
        return redirect(url_for('estudiantes'))



# ------------------------------------------------------------------------------------

#  Tratamiento Usuarios = CRUD

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(15), nullable=False)


# template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# template_dir = os.path.join(template_dir, 'src', 'templates')
# app = Flask(__name__, template_folder = template_dir)


#Rutas de la aplicación
@app.route('/users')
def users_home():
    myresult = Users.query.all()
    
    # cursor = db.database.cursor()
    # cursor.execute("SELECT * FROM users")
    # myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    # columnNames = [column[0] for column in cursor.description]
    columnNames = ['id', 'username', 'name', 'password']
    
    for record in myresult:
        print(record)
        insertObject.append(dict(zip(columnNames, (record.id, record.username, record.name, record.password))))
    # cursor.close()
    return render_template('index.html', data=insertObject)


#Ruta para guardar usuarios en la bdd
@app.route('/users/user', methods=['POST'])
def users_addUser():
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']

    if username and name and password:
        nuevo_user = Users(username=username, name=name, password=password)
        db.session.add(nuevo_user)
        db.session.commit()
        # flash("Data Inserted Successfully")
    return redirect(url_for('users_home'))

@app.route('/users/delete/<string:id>')
def users_delete(id):
    usuario = Users.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    # flash("Record Has Been Deleted Successfully")
    return redirect(url_for('users_home'))

@app.route('/users/edit/<string:id>', methods=['POST'])
def users_edit(id):
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']

    if username and name and password:
        usuario = Users.query.get_or_404(id) 
        usuario.username = username
        usuario.name = name
        usuario.password = password
        db.session.commit()
        # flash("Data Updated Successfully")
    return redirect(url_for('users_home'))







if __name__ == '__main__':
    with app.app_context():
        db.create_all()         # Crea la base de datos

    # En el navegador -> http://javicu.synology.me:5010/login  o  http://192.168.1.41:5010/login
    # app.run(host="192.168.1.41", port=5010, debug=True)
    # no poner como host "javicu.synology.me", ni localhost, no han funcionado

    # Conexión segura https
    # app.run(ssl_context=('cert.pem', 'privkey.pem'),host="192.168.1.41", port=5010, debug=True)
    app.run(debug=True, port=5010)
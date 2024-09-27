#      Aplicación Web creada por la IA Aria en python, Flask y SQULite
#
#      Instalación de paquetes necesarios
#
#  $ pip install Flask    Flask-SQLAlchemy    Flask-Login

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



@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        usuario = Usuario.query.filter_by(username=username, password=password).first()
        if usuario:
            login_user(usuario)
            return redirect(url_for('usuarios'))
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





if __name__ == '__main__':
    with app.app_context():
        db.create_all()         # Crea la base de datos
    app.run(debug=True)         # En el navegador -> http://localhost:5000/login  o  http://127.0.0.1:5000/login
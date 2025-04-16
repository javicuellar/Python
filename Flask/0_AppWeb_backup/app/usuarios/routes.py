from flask import Blueprint
from flask import render_template, redirect, request, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user

from app import db, login_manager
from app.usuarios.models import Usuarios
from app.usuarios.forms import LoginForm, RegistroForm
from app.usuarios.util import comprobar_password





blueprint = Blueprint('usuarios_blueprint', __name__, url_prefix='')


# Redirige a la ruta de login por defecto
@blueprint.route('/')
def route_default():
    return redirect(url_for('usuarios_blueprint.login'))


# Login & Registration en la aplciación
@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if 'login' in request.form:
        usuario = request.form['usuario']
        password = request.form['password']
        
        user = Usuarios.query.filter_by(usuario=usuario).first()
        if user and comprobar_password(password, user.password):
            login_user(user)
            print('user login: ', user, " -> vuelvo al login")
            # porque va al login otra vez?
            return redirect(url_for('usuarios_blueprint.login'))

        # Si el usuario o pws no esta bien 
        return render_template('usuarios/login.html', 
                               msg='Datos introducidos incorrectos',
                               form=login_form)

    if not current_user.is_authenticated:
        print("No hay usuario autenticado")
        return render_template('usuarios/login.html',
                               form=login_form)

    return redirect(url_for('usuarios_blueprint.usuarios'))
    # return redirect(url_for('home_blueprint.home'))



# Función que valida y da de alta un nuevo usuario en la base de datos
def valida_alta_usuario(usuario, password, email):
    valido=False
    # Comprobar si el usuario existe
    user = Usuarios.query.filter_by(usuario=usuario).first()
    print("Usuario leido", user)    
    if user:
        mensaje = 'Usuario ya registrado'
        print("Usuario ya registrado")
    else:
        # Revisar si el email existe
        user = Usuarios.query.filter_by(email=email).first()
        print("Usuario leido por mail ", user)  
        if user:
            mensaje = 'Email ya registrado'
            print("Email ya registrado")
        else:        
            # Usuario validado, crear el usuario
            user = Usuarios(usuario=usuario, password=password, email=email)
            db.session.add(user)
            db.session.commit()
            mensaje = 'Usuario creado correctamente'
            valido=True
    return mensaje, valido


@blueprint.route('/registro', methods=['GET', 'POST'])
def registro():
    crear_cuenta_form = RegistroForm(request.form)
    if 'registro' in request.form:
        usuario = request.form['usuario']
        email = request.form['email']
        password = request.form['password']

        mensaje, valido = valida_alta_usuario(usuario, password, email)
        
        return render_template('usuarios/registro.html', 
                            msg=mensaje, 
                            success=valido, 
                            form=crear_cuenta_form)
    else:
        return render_template('usuarios/registro.html', form=crear_cuenta_form)



@blueprint.route('/alta_usuario', methods=['GET', 'POST'])
def alta_usuario():
    crear_cuenta_form = RegistroForm(request.form)
    if current_user.is_authenticated:
        usuario = request.form['usuario']
        email = request.form['email']
        password = request.form['password']
        print ("usuario: ", usuario, " email: ", email, "password: ", password)

        mensaje, valido = valida_alta_usuario(usuario, password, email)

        usuarios = Usuarios.query.all()
            
        if valido:
            return render_template('usuarios/usuarios.html', segment='usuarios', usuarios=usuarios, msg=mensaje, form=crear_cuenta_form)
        else:
            return render_template('usuarios/usuarios.html', segment='usuarios', msg=mensaje, usuarios=usuarios, form=crear_cuenta_form)



@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('usuarios_blueprint.login'))



# Errors
@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404


@blueprint.errorhandler(405)
def not_found_error(error):
    return render_template('home/page-405.html'), 405


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('home/page-500.html'), 500





#  no se usa, pero se deja por si acaso
@blueprint.route('/usuarios')
@login_required
def usuarios(mensaje=None):
    crear_cuenta_form = RegistroForm(request.form)
    usuarios = Usuarios.query.all()
    return render_template('usuarios/usuarios.html', segment='usuarios', usuarios=usuarios, msg=mensaje, form=crear_cuenta_form)



@blueprint.route('/usuario/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_usuario(id):
    usuario = Usuarios.query.get_or_404(id)
    if request.method == 'POST':
        usuario.usuario = request.form['usuario']
        usuario.email = request.form['email']
        usuario.password = request.form['password']
        db.session.commit()
        flash('Usuario actualizado exitosamente.')
        # return redirect(url_for('home_blueprint.home'))
        return redirect(url_for('usuarios_blueprint.usuarios'))
    print("edit_user, GET ", usuario)
    # return render_template('home/home.html', usuario=usuario)
    # return render_template('usuarios/usuarios.html', usuario=usuario)
    return redirect(url_for('usuarios_blueprint.usuarios'))


@blueprint.route('/usuario/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def baja_usuario(id):
    print("delete_usuario, id: ", id)
    usuario = Usuarios.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    flash('Usuario eliminado exitosamente.')
    # return redirect(url_for('home_blueprint.home'))
    return redirect(url_for('usuarios_blueprint.usuarios'))
from flask import Flask, Blueprint, render_template, request



# Creamos un blueprint para la sección de usuarios
user_bp = Blueprint('user', __name__, url_prefix='/users')

# Definimos una vista dentro del blueprint
@user_bp.route('/')
def user_index():
    return render_template('users/index.html')

@user_bp.route('/profile')
def user_profile():
    return render_template('users/profile.html')

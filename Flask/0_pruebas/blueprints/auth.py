from flask import Blueprint, render_template, request, redirect, url_for




auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # ... lógica de login ...
    return render_template('auth/login.html')


@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    # ... lógica de registro ...
    return render_template('auth/registro.html')

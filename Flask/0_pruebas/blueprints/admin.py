from flask import Flask, Blueprint, render_template, request




# Creamos un blueprint para la sección de administradores
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
def admin_index():
    return 'Página principal de administradores'
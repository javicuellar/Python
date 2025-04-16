from flask import Blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
from app.usuarios.models import Usuarios




blueprint = Blueprint('home_blueprint', __name__, url_prefix='')


@blueprint.route('/home')
@login_required
def home():
    print("home, recuperamos usuarios")
    usuarios = Usuarios.query.all()
    return render_template('home/home.html', segment='index', usuarios=usuarios)


@blueprint.route('/<template>')
@login_required
def route_template(template):
    try:
        if not template.endswith('.html'):
            template += '.html'
        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404
    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):
    try:
        segment = request.path.split('/')[-1]
        if segment == '':
            segment = 'index'
        return segment
    except:
        return None

from flask_login import UserMixin
from app import db, login_manager

from app.usuarios.util import hash_password




class Usuarios(db.Model, UserMixin):
    id       = db.Column(db.Integer, primary_key=True)
    usuario  = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.LargeBinary)
    email    = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_password(value)  # codificamos contraseña en bytes (no string)

            setattr(self, property, value)

    def __repr__(self):
        return str(self.usuario)


@login_manager.user_loader
def user_loader(id):
    return Usuarios.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    usuario = request.form.get('usuario')
    user = Usuarios.query.filter_by(usuario=usuario).first()
    return user if user else None

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired





# Definimoss Form de login
class LoginForm(FlaskForm):
    usuario = StringField('Usuario',
                         id='usuario_login',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])



# Definimoss Form de Registro
class RegistroForm(FlaskForm):
    usuario = StringField('Usuario',
                         id='usuario_nuevo',
                         validators=[DataRequired()])
    email = StringField('Email',
                      id='email_nuevo',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='pwd_nuevo',
                             validators=[DataRequired()])

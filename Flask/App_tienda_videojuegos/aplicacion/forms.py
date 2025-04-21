from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DecimalField,IntegerField,TextAreaField,SelectField,PasswordField, HiddenField, IntegerField
from wtforms.fields import EmailField
from flask_wtf.file import FileField
from wtforms.validators import DataRequired, NumberRange


class formCategoria(FlaskForm):                      
	nombre=StringField("Nombre:",validators=[DataRequired("Tienes que introducir el dato")])
	submit = SubmitField('Enviar')


class formArticulo(FlaskForm):                      
	nombre=StringField("Nombre:",validators=[DataRequired("Tienes que introducir el dato")])
	precio=DecimalField("Precio:",default=0,validators=[DataRequired("Tienes que introducir el dato")])
	iva=IntegerField("IVA:",default=21,validators=[DataRequired("Tienes que introducir el dato")])
	descripcion= TextAreaField("Descripción:")
	photo = FileField('Selecciona imagen:')
	stock=IntegerField("Stock:",default=1,validators=[DataRequired("Tienes que introducir el dato")])
	CategoriaId=SelectField("Categoría:",coerce=int)
	submit = SubmitField('Enviar')

class formSINO(FlaskForm):      
	si = SubmitField('Si') 
	no = SubmitField('No') 

class LoginForm(FlaskForm):
	username = StringField('Login', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Entrar')

class formUsuario(FlaskForm):
	username = StringField('Login', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	nombre = StringField('Nombre completo')
	email = EmailField('Email')
	submit = SubmitField('Aceptar')	

class formChangePassword(FlaskForm):
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Aceptar')	

class formCarrito(FlaskForm):
	id = HiddenField()
	cantidad = IntegerField('Cantidad',default=1,validators=[NumberRange(min=1,message="Debe ser un número positivo"),DataRequired("Tienes que introducir el dato")])
	submit = SubmitField('Aceptar')	
from flask import Flask, render_template,redirect,url_for,request,abort,session,make_response
from flask_login import LoginManager,login_user,logout_user,login_required,current_user
# from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from app import config
from app.forms import LoginForm,formUsuario,formChangePassword, formContacto, formSINO


app = Flask(__name__)
app.config.from_object(config)

Bootstrap(app)	
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

from app.models import Usuarios, Contactos, Etiquetas




@login_manager.user_loader
def load_user(user_id):
    return Usuarios.query.get(int(user_id))


@app.route('/login', methods=['get', 'post'])
def login():
	# Control de permisos
	if current_user.is_authenticated:
		return redirect(url_for("contactos"))

	form = LoginForm()
	if form.validate_on_submit():
		user=Usuarios.query.filter_by(username=form.username.data).first()
		if user!=None and user.verify_password(form.password.data):
			login_user(user)
			next = request.args.get('next')
			return redirect(next or url_for('contactos'))
		form.username.errors.append("Usuario o contraseña incorrectas.")
	return render_template('login.html', form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route("/registro",methods=["get","post"])
def registro():
	# Control de permisos
	if current_user.is_authenticated:
		return redirect(url_for("contactos"))

	form=formUsuario()
	if form.validate_on_submit():
		existe_usuario=Usuarios.query.filter_by(username=form.username.data).first()
		if existe_usuario==None:
			user=Usuarios()
			form.populate_obj(user)
			user.admin=False
			db.session.add(user)
			db.session.commit()
			return redirect(url_for("contactos"))
		form.username.errors.append("Nombre de usuario ya existe.")
	return render_template("usuarios_new.html",form=form)



@app.route('/')
@app.route('/contactos/<id>')
def contactos(id='0'):
	etiqueta = Etiquetas.query.get(id)
	etiquetas = Etiquetas.query.all()
	
	if id == '0':
		contactos = Contactos.query.all()
	else:
		contactos = Contactos.query.filter_by(EtiquetaId=id)
	return render_template("inicio.html",contactos=contactos, etiquetas=etiquetas, etiqueta=etiqueta)



@app.route('/contactos/new', methods=["get","post"])
@login_required
def contactos_new():
	# Control de permisos
	if not current_user.is_admin():
		abort(404)

	form = formContacto()
	etiquetas = [(c.id, c.nombre) for c in Etiquetas.query.all()[1:]]
	form.EtiquetaId.choices = etiquetas

	if form.validate_on_submit():
		cont = Contactos()
		form.populate_obj(cont)
		db.session.add(cont)
		db.session.commit()
		return redirect(url_for("contactos"))
	else:
		return render_template("Contactos_new.html",form=form)


@app.route('/contactos/<id>/edit', methods=["get","post"])
@login_required
def contactos_edit(id):
	# Control de permisos
	if not current_user.is_admin():
		abort(404)

	cont = Contactos.query.get(id)
	if cont is None:
		abort(404)

	form= formContacto(obj=cont)
	etiquetas = [(c.id, c.nombre) for c in Etiquetas.query.all()[1:]]
	form.EtiquetaId.choices = etiquetas
	
	if form.validate_on_submit():
		#Borramos la imagen anterior si hemos subido una nueva
		form.populate_obj(cont)
		db.session.commit()
		return redirect(url_for("contactos"))
	return render_template("contactos_new.html",form=form)



@app.route('/contactos/<id>/delete', methods=["get","post"])
@login_required
def contactos_delete(id):
		# Control de permisos
	if not current_user.is_admin():
		abort(404)

	cont = Contactos.query.get(id)
	if cont is None:
		abort(404)

	form = formSINO()
	if form.validate_on_submit():
		if form.si.data:
			db.session.delete(cont)
			db.session.commit()
		return redirect(url_for("contactos"))
	return render_template("contactos_delete.html",form=form,cont=cont)

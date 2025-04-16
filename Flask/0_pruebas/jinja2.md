# Plantillas Jinja2

* ¿Qué son las Plantillas?

    - Separación de la lógica de presentación del código Python.
    - Jinja2 como motor de plantillas predeterminado en Flask.

* Creando Plantillas:

    - La carpeta templates.
    - Archivos HTML con sintaxis Jinja2.
    - Variables en las Plantillas:

            perfil.html

            <h1>Bienvenido, {{ usuario.nombre }}</h1>
            <p>Tu correo electrónico es: {{ usuario.email }}</p>

            app.py
            
            from flask import render_template

            @app.route('/perfil')
            def perfil_usuario():
                usuario = {'nombre': 'Juan Pérez', 'email': 'juan@ejemplo.com'}
                return render_template('perfil.html', usuario=usuario)

 * Estructuras de Control:

   * {% if condicion %}, {% elif condicion %}, {% else %}, {% endif %}.
   * {% for item in lista %}, {% endfor %}.
 
 * Filtros:
 
   * Modificar la salida de las variables (ej: {{ nombre|upper }}).
   * Filtros comunes: upper, lower, capitalize, length, default.
 
 * Herencia de Plantillas:
 
   * Crear una plantilla base (base.html) con la estructura común.
   * Extender la plantilla base en otras plantillas ({% extends 'base.html' %}).
   * Bloques ({% block contenido %}, {% endblock %}).


-------------------------------------
## Jinja2 en Flask: Un ejemplo completo con base.html, extensiones y bloques

Este ejemplo muestra una aplicación Flask que utiliza Jinja2 para renderizar plantillas.  Incluye una plantilla base (`base.html`), plantillas que heredan de la base usando bloques, y la integración de una extensión de Jinja2.

**1. Estructura del proyecto:**

```
my_app/
├── app.py
└── templates/
    ├── base.html
    ├── index.html
    └── about.html
```

**2. app.py:**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='Mundo')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
```

**3. templates/base.html:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Mi Aplicación Flask</h1>
        <nav>
            <a href='/'>Inicio</a>
            <a href='/about'>Acerca de</a>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <p>&copy; 2023 Mi Aplicación</p>
    </footer>
</body>
</html>
```

**4. templates/index.html:**

```html
{% extends 'base.html' %}

{% block title %}Inicio{% endblock %}

{% block content %}
    <p>¡Hola, {{ name }}!</p>
{% endblock %}
```

**5. templates/about.html:**

```html
{% extends 'base.html' %}

{% block title %}Acerca de{% endblock %}

{% block content %}
    <p>Esta es la página Acerca de.</p>
{% endblock %}
```

**Explicación:**

*   `base.html` define la estructura básica de la página, incluyendo el encabezado, el pie de página y bloques para el título y el contenido principal (`title` y `content`).
*   `index.html` y `about.html` heredan de `base.html` usando `{% extends 'base.html' %}`.  Los bloques se rellenan con contenido específico usando `{% block ... %}{% endblock %}`.
*   La variable `name` se pasa desde la vista (`app.py`) a la plantilla usando `render_template('index.html', name='Mundo')`.

**Para ejecutar la aplicación:**

1.  Guarda los archivos como se muestra en la estructura del proyecto.
2.  Asegúrate de tener Flask instalado (`pip install Flask`).
3.  Ejecuta `app.py` desde tu terminal.
4.  Abre tu navegador y visita `http://127.0.0.1:5000/` y `http://127.0.0.1:5000/about`.

Este ejemplo proporciona una base sólida para construir aplicaciones web más complejas con Flask y Jinja2. Puedes añadir más extensiones, filtros y tests de Jinja2 según sea necesario.
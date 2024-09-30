FROM python:latest

LABEL Maintainer="Prueba docker python HTTPS"

# Con Python no hace falta instalar estos paquetes
# RUN apt-get update && apt-get upgrade -y && apt-get install -y python3-pip  && apt-get clean && rm -rf /var/lib/apt/lists/*
#	&& apt-get install -y python3-venv \

# Copiamos la aplicación al directorio /usr/src del contenedor
COPY . /usr/src

# Activamos como directorio de trabajo /usr/src
WORKDIR /usr/src

# Instalamos las dependencias necesarias para la aplicación: Flask    Flask-SQLAlchemy    Flask-Login
RUN pip install -r requirements.txt

# EXPOSE 5010

# Ejecutamos la aplicación 
CMD [ "python3", "webapp.py"]




#  $ docker build -t prueba/python_https:1 .
#  $ docker run -d -p 5010:5010 --name python_webapp prueba/python_https:1 .			# sin --netrower usa bridge, crea una nueva red interna   NO USAR
#  $ docker run -d --name python_webapp_https --network host prueba/python_https:1 .	# con --network host usa la misma IP						USAR

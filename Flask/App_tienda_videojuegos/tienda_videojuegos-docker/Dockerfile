FROM ubuntu:16.04
MAINTAINER José Domingo Muñoz
RUN apt-get update -y && apt-get install -y \
        apache2 \
        libapache2-mod-wsgi-py3 \
        python3-pip \
        && apt-get clean && rm -rf /var/lib/apt/lists/*
ADD /tienda_videojuegos /var/www/html/tienda_videojuegos
RUN chown www-data:www-data -R /var/www/html/tienda_videojuegos
RUN pip3 install -r /var/www/html/tienda_videojuegos/requirements.txt
ADD 000-default.conf /etc/apache2/sites-available/
ADD app.wsgi /var/www/html/tienda_videojuegos
RUN service apache2 restart
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
EXPOSE 80
WORKDIR /var/www/html/tienda_videojuegos
COPY ./run.sh /
ENTRYPOINT ["/run.sh"]

#    Instalar previamente pysftp
#  pip install pysftp

import pysftp

# Dirección o IP del servidor SFTP.
host = "ftp.mi-sitio.com"

# Usuario y contraseña.
username = "mi-usuario"
password = "mi-clave-123"

# Realizar la conexión.
with pysftp.Connection(host, username=username, password=password) as sftp:
    # Cambiar el directorio a la carpeta remota donde se quiere
    # subir el archivo.
    with sftp.cd("/home/public_html"):
        # Subir el archivo local hola.txt al servidor.
        sftp.put("hola.txt")
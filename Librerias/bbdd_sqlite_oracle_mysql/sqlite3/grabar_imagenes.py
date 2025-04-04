#   Script generado por la IA Aria de Opera

# Las imágenes se pueden guardar como BLOBs (Binary Large Objects), que son ideales para almacenar datos binarios como imágenes.
#
# Pasos para almacenar imágenes en SQLite
# Conectar a la base de datos:
#    1) necesitas establecer una conexión con tu base de datos SQLite.
#        Crear una tabla: Debes crear una tabla que tenga una columna para almacenar las imágenes como BLOB.
#    2) Insertar la imagen: Puedes leer la imagen en modo binario y luego insertarla en la tabla.
#    3) Recuperar la imagen: Para mostrar la imagen, puedes recuperarla de la base de datos y guardarla en un archivo
#       o mostrarla directamente.

import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('bbdd_fotos.db')
cursor = conn.cursor()

# Crear una tabla para almacenar imágenes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS imagenes (id INTEGER PRIMARY KEY, nombre TEXT, imagen BLOB)
               ''')

# Función para insertar una imagen
def insertar_imagen(nombre, ruta_imagen):
    with open(ruta_imagen, 'rb') as file:
        blob = file.read()
        cursor.execute('INSERT INTO imagenes (nombre, imagen) VALUES (?, ?)', (nombre, blob))
        conn.commit()

# Función para recuperar una imagen
def recuperar_imagen(id):
    cursor.execute('SELECT nombre, imagen FROM imagenes WHERE id = ?', (id,))
    row = cursor.fetchone()
    if row:
        nombre, imagen = row
        with open(f'recuperada_{nombre}.jpg', 'wb') as file:
            file.write(imagen)


# Ejemplo de uso
insertar_imagen('mi_imagen', '//NAS\\invitados\logo_google.png')
recuperar_imagen(1)

# Cerrar la conexión
conn.close()
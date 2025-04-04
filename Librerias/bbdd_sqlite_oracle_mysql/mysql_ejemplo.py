import mysql.connector
from mysql_claves import *



# Datos de conexión a la base de datos
config = {
  'user': USUARIIO_MYSQL,
  'password': PASSWROD_MYSQL,
  'host': HOST,
  'database': 'prueba',
  'port': PUERTO,
}


# Conexión a la base de datos
try:
  connection = mysql.connector.connect(**config)
  cursor = connection.cursor()

  # Crear la tabla
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
      id INT AUTO_INCREMENT PRIMARY KEY,
      nombre VARCHAR(255) NOT NULL,
      email VARCHAR(255) UNIQUE NOT NULL,
      contraseña VARCHAR(255) NOT NULL
    )
  """)

  # Confirmar la creación de la tabla
  connection.commit()

  print("Tabla creada correctamente")

  # Cerrar la conexión
  cursor.close()
  connection.close()

except mysql.connector.Error as error:
  print(f"Error al conectar a la base de datos: {error}")

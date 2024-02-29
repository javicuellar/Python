# ------------------------------------------------------------------------------------------------
#    LIBRERIA os: Tratamiento ficheros, directorios, borrado
# ------------------------------------------------------------------------------------------------

#    Ejemplo lista de archvios, tamaño, fecha acceso
#
# recogido de:  http://python-para-impacientes.blogspot.com.es/2015/09/explorando-directorios-con-listdir-walk.html
import os
from datetime import datetime

ruta_app = os.getcwd()              # obtiene ruta del script 
contenido = os.listdir(ruta_app)    # obtiene lista con archivos/dir 

total = 0
archivos = 0
formato = '%d-%m-%y %H:%M:%S'       # establece formato de fecha-hora
linea = '-' * 60                    # escribe 60 veces '-'

for elemento in contenido:
    archivo = ruta_app + os.sep + elemento
    
    # verifica que el archivo no es ejecutable -> not os.access(archivo, os.X_OK)
    #    os.F_OK para comprobar que es posible acceder a un archivo,
    #    os.R_OK para saber si el archivo se puede leer y
    #    os.W_OK para conocer si adem�s se permite la escritura.
    if  os.access(archivo, os.X_OK) and os.path.isfile(archivo):
        archivos += 1
        estado = os.stat(archivo)       # obtiene estado del archivo
        tamano = estado.st_size         # obtiene de estado el tamano 
        
        # Obtiene del estado fechas de último acceso/modificación
        # Como los valores de las fechas-horas vienen expresados
        # en segundos se convierten a tipo datetime. 
        ult_acceso = datetime.fromtimestamp(estado.st_atime)
        modificado = datetime.fromtimestamp(estado.st_mtime)
        
        # Se aplica el formato establecido de fecha y hora
        ult_acceso = ult_acceso.strftime(formato)
        modificado = modificado.strftime(formato)
        
        # Se acumulan tamanos y se muestra info de cada archivo
        total += tamano
        print(linea)
        print('archivo      :', elemento)
        print('modificado   :', modificado)        
        print('Último acceso:', ult_acceso)
        print('tamano (Kb)  :', round(tamano/1024, 1))

print(linea)
print('Núm. archivos:', archivos)
print('Total (kb)   :', round(total/1024, 1))

# -------------------------------------------------------------------------------------------------------------------------
#    Por cierto, aunque hemos utilizado os.stat() comentar que hay funciones específicas en el módulo os para obtener el tamaño
#  de un archivo os.path.getsize() y las fechas de último acceso os.path.getatime() y de última modificación os.path.getmtime(). 

# Para finalizar, los métodos de la clase stat son los siguientes (dependiendo del sistema algunos no estarán disponibles): 
# st_size: tamano en bytes.
# st_mode: tipo de archivo y bits de permisos.
# st_ino: número de inodo.
# st_dev: identificador del dispositivo.
# st_uid: identificador del usuario propietario.
# st_gid: identificador del grupo propietario.
# st_atime: fecha-hora del último acceso (en segundos).
# st_mtime: fecha-hora de la última modificación (en segundos).
# st_ctime: fecha-hora ultimo cambio (unix) o creación (win).
# st_atime_ns, st_mtime_ns y st_ctime_ns (idem. expresado en nanoseg).
# st_blocks: número de bloques de 512 bytes asignados.
# st_blksize: tamano de bloque preferido por sistema.
# st_rdev: tipo de dispositivo si un dispositivo inode.
# st_flags: banderas definidas por usuario.
# st_gen: Número fichero generado.
# st_birthtime: tiempo de creación del archivo.
# st_rsize: tamano real del archivo.
# st_creator: creador del archivo.
# st_type: tipo de archivo.
# st_file_attributes: atributos.
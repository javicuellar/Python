# ------------------------------------------------------------------------------------------------
#    LIBRERIA os: Tratamiento ficheros, directorios, borrado
# ------------------------------------------------------------------------------------------------
import os
from datetime import datetime

ruta_app = os.getcwd()
total = 0
num_archivos = 0
formato = '%d-%m-%y %H:%M:%S'
linea = '-' * 60

for ruta, directorios, archivos in os.walk(ruta_app, topdown=True):
    print('\nruta       :', ruta) 
    for elemento in archivos:
        num_archivos += 1
        archivo = ruta + os.sep + elemento
        estado = os.stat(archivo)
        tamano = estado.st_size
        ult_acceso = datetime.fromtimestamp(estado.st_atime)
        modificado = datetime.fromtimestamp(estado.st_mtime)
        ult_acceso = ult_acceso.strftime(formato)
        modificado = modificado.strftime(formato)
        total += tamano
        print(linea)
        print('archivo      :', elemento)
        print('modificado   :', modificado)        
        print('último acceso:', ult_acceso)
        print('tamano (Kb)  :', round(tamano/1024, 1))

print(linea)
print('Num. archivos:', num_archivos)
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
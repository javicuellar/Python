# ------------------------------------------------------------------------------------------------
#    LIBRERIA os: Tratamiento ficheros, directorios, borrado
# ------------------------------------------------------------------------------------------------

#  Obtener iterador con las entradas de un directorio: scandir()

#  Para concluir, la función os.scandir() devuelve un iterador basado en la clase DirEntry
# que contiene información relacionada con las entradas (archivos y directorios) del directorio
# indicado (path). La información no sigue ningún tipo de orden predeterminado y no se incluyen,
# si existen, las entradas '.' y '..'. 

import os
from datetime import datetime

os.scandir(path='.')

#      La clase DirEntry cuenta con métodos que permiten acceder a información relativa a cada entrada: 
#   name: nombre del archivo o directorio leído.
#   path: ruta completa del archivo o directorio leído.
#   inode(): devuelve número de inodo de la entrada.
#   is_dir(*, follow_symlinks=True): devuelve True si es directorio
#   is_file(*, follow_symlinks=True): devuelve True si es archivo
#   is_symlink(): devuelve True si es un enlace simbólico.
#   stat(*, follow_symlinks=True): devuelve estado de la entrada

#      La función os.scandir() se propone en Python 3.5 (PEP0471) como alternativa a os.listdir() al
#  mejorar la velocidad de acceso al sistema de ficheros por realizar menos llamadas a os.stat().
#  Además, dependiendo del tipo de sistema y del tamano de los archivos la velocidad con os.walk()
#  puede ser más rápida de 2 a 20 veces. 

import os
from datetime import datetime

ruta_app = os.getcwd() 
total = 0
archivos = 0
formato = '%d-%m-%y %H:%M:%S'
linea = '-' * 40

contenido = os.scandir(ruta_app)
for elemento in contenido:
    if os.access(elemento.path, os.X_OK) and elemento.is_file():
        archivos += 1
        estado = elemento.stat()        
        tamano = estado.st_size
        ult_acceso = datetime.fromtimestamp(estado.st_atime)
        modificado = datetime.fromtimestamp(estado.st_mtime)
        ult_acceso = ult_acceso.strftime(formato)
        modificado = modificado.strftime(formato)
        total += tamano
        print(linea)
        print('archivo      :', elemento.name)
        print('permisos     :', estado.st_mode)
        print('modificado   :', modificado)        
        print('Último acceso:', ult_acceso)
        print('tamaño (Kb)  :', round(tamano/1024, 1))

print(linea)
print('Núm. archivos:', archivos)
print('Total (kb)   :', round(total/1024, 1))
# ------------------------------------------------------------------------------------------------
#    LIBRERIA os: Tratamiento ficheros, directorios, borrado
# ------------------------------------------------------------------------------------------------
#  Borrar todos los ficheros y subdirectorios de un directorio
# Delete everything reachable from the directory named in 'top',
# assuming there are no symbolic links.
# CAUTION:  This is dangerous!  For example, if top == '/', it
# could delete all your disk files.
import os

top = 'direcotorio_a_borrar'

for root, dirs, files in os.walk(top, topdown=False):
   for name in files:
       print("borramos fichero: ", name)
       os.remove(os.path.join(root, name))
   for name in dirs:
       print("borramos directorio: ", name)
       os.rmdir(os.path.join(root, name))


# -------------------------------------------------------------------------------------------------
from os import walk			# Recorremos todo el árbol de archivos

for (path, directorios, archivos) in walk("."):
    print("patch: ", path)
    print("directorios: ", directorios)
    print("archivos: ", archivos)

# -------------------------------------------------------------------------------------------------
#    Mayor control con os.walk() - python-2.2 y python-3.x
#  Se pueden obtener sólo los archivos de forma más compacta:
from os import walk

def ls(ruta = '.'):
    return next(walk(ruta))[2]

print("\nUsando os.walk y next")
print("Ficheros en el directorio por defecto, ruta actual:\n", ls())


# O se puede tener mayor control si se quiere, obteniendo dos listas (directorios y archivos)
def ls(ruta = '.'):
    dir, subdirs, archivos = next(walk(ruta))
    print("Actual: ", dir)
    print("Subdirectorios: ", subdirs)
    print("Archivos: ", archivos)
    return archivos

print("\nSegunda forma Usando os.walk y next")
print("Ficheros en el directorio por defecto, ruta actual:\n", ls())

# Y si también se quiere obtener los archivos de todos los subdirectorios, permite iterar de la
#  siguiente forma:
from os import walk, getcwd

def ls(ruta = getcwd()):
    listaarchivos = []
    for (_, _, archivos) in walk(ruta):
        listaarchivos.extend(archivos)
    return listaarchivos

print("\nTercera forma Usando os.walk y next")
print("Ficheros en el directorio por defecto, ruta actual:\n", ls())
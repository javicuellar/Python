# ------------------------------------------------------------------------------------------------
#    LIBRERIA os: Tratamiento ficheros, directorios, borrado
# ------------------------------------------------------------------------------------------------

#   Mayor eficiencia con os.scandir() - python-3.5
#
#  Devuelve un iterador a objetos que mantienen las propiedades de los archivos, haciéndolo más eficiente
# (por ejemplo, no necesita realizar una llamada al sistema adicional para ver si un objeto es un archivo
# o un directorio).
from os import scandir, getcwd

def ls(ruta = getcwd()):    # toma por defecto la ruta actual = getcwd
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

print("Ficheros en el directorio por defecto, ruta actual:\n", ls())


# -------------------------------------------------------------------------------------------------
# O si se quiere obtener la ruta absoluta de cada archivo:
from os import scandir, getcwd
from os.path import abspath

def ls(ruta = getcwd()):
    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]

print("\nLo mismo pero con ruta absoluta.")
print("Ficheros en el directorio por defecto, ruta actual:\n", ls())

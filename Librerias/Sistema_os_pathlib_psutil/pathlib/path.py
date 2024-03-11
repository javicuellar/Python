# ------------------------------------------------------------------------------------------------
#    LIBRERIA pathlb: Tratamiento ficheros, directorios, borrado
# ------------------------------------------------------------------------------------------------

#    Con la libreráa pathlib y su clase principal Path - python-3.4
#
#   Ofrece mayor nivel de consistencia entre los diferentes sistemas operativos, sin la necesidad de
#  referenciar directamente a os, evitando también muchas llamadas al sistema.
from pathlib import Path

def ls(ruta = Path.cwd()):
    return [arch.name for arch in Path(ruta).iterdir() if arch.is_file()]

print("Usando pahtlib - path")
print("Ficheros en el directorio por defecto, ruta actual:\n", ls())
# ------------------------------------------------------------------------------------------------
#    LIBRERIA os: Tratamiento ficheros, directorios, borrado
# ------------------------------------------------------------------------------------------------
#  Leer carpetas y archivos en python
from os import listdir

for cosa in listdir("."):   # entrada el path del directorio deseado
    print("Leído listdir: ", cosa)				# imprime una lista con archivos y directorios


from os.path import isfile, join

mi_path = "."
solo_archivos = [							# lista por "compresión"
    cosa for cosa in listdir(mi_path)		# listdir devuelve una lista
    if isfile(join(mi_path, cosa))]			# solo nos quedamos con los archivos
                                            # join junta el patch con el nombre de archivo
for archivo in solo_archivos:
    print("Léido llistdir tipo fichero: ", archivo)
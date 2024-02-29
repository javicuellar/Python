# ------------------------------------------------------------------------------------------------
#    LIBRERIA os: Tratamiento ficheros, directorios, borrado
# ------------------------------------------------------------------------------------------------

# Listar el tamaño en bytes de cada archivo de un path
import os
from os.path import join, getsize

directorio = 'd:\python\Librerias\os'
for root, dirs, files in os.walk(directorio):
   print(root, "consume", sum(getsize(join(root, name)) for name in files), "bytes in", len(files), "non-directory files")
   
   if 'CVS' in dirs:
       print("Hay CVS, lo borramos")
       dirs.remove('CVS')   # don't visit CVS directories

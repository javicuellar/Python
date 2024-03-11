# ------------------------------------------------------------------------------------------------
#    LIBRERIA os: Tratamiento ficheros, directorios, borrado
# ------------------------------------------------------------------------------------------------

#  Lista con el nombre de los archivos de una determinada extensión en un directorio
import os

#Variable para la ruta al directorio
path = 'd:/python/Librerias'
 
#Lista vacia para incluir los ficheros
lstFiles = []
 
#Lista con todos los ficheros del directorio:
lstDir = os.walk(path)      # os.walk()  Lista directorios y ficheros

#Crea una lista de los ficheros jpg que existen en el directorio y los incluye a la lista.
for root, dirs, files in lstDir:
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if(extension == ".py"):
            lstFiles.append(nombreFichero+extension)
            #print (nombreFichero+extension)

print("\nListado ficheros python (*.py)")         
print(lstFiles)            
print('LISTADO FINALIZADO')
print("longitud de la lista = ", len(lstFiles))

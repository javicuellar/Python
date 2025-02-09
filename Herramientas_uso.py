###################################################################################################
#  Para usar las Herramientas python de la carpeta Herramientas importar la librería
#     
#    - La carpeta Python\Herramientas contiene los scripts en "local" (mantenimiento)
#    - Se sincroniza con la carpeta siguiente, que es la que se recupera automáticamente 
#        C:\Users\javic\AppData\Local\Programs\Python\Python311\Lib\Herramientas
#
###################################################################################################

#  Para usarlo, simplemente importar la librería (ya está en el path)
from Herramientas.variables import USUARIO, PASSWORD, etc. 



###################################################################################################

#  Sino estuviera en el path, hay que acceder a la carpeta Herramientas
import sys, os

# Para Windows añadimos path a librerías python, para añadir librerías mías de Herramientas
if os.name == 'nt':
    sys.path.append(os.path.join(os.path.dirname(__file__), '\\Python'))
    DIRECTORIO = 'D:\\'
else:
    DIRECTORIO = '/video'


from Herramientas.variables import USUARIO, PASSWORD, etc. 
#   Ejemplos funciones en módulos
from Ejemplos import sumar as s, restar as r
s.suma(5,3)
r.resta(5,3)

#  listas y n�meros aleatorios, randint
from Ejemplos import guerrabarcos

#  ordenar listas numeros (solo orden los n�meros impares (utiliza ITERADORES)
from Ejemplos import Orden_impar

#  Ejemplo conversor millas, pies y pulgadas
from Ejemplos import conversor_millas_metros


# encontrar el mayor de la lista  (uso lambda)
from Ejemplos import mayor
from Ejemplos import funcion_calculo_marca
from Ejemplos import funcion_bucle_cubico
from Ejemplos import funcion_recursiva
from Ejemplos import pos_medio
# Kata de ejemplo para invertir una lista de númreos
from Ejemplos import funcion_invertir_lista

# Kata Growth of a Population, crecimiento población
from Ejemplos import poblacion

# kata extract file name usando RE 'Regular expresions'
from Ejemplos import Expresiones_regulares_extrae


#   Ejemplos con ficheros
from Ficheros import file_csv_escribir
# graba regristros con numeros y textos en ficheros (hasta 100.000.000 de reg.)
from Ficheros import file_csv_leer
from Ficheros import escribir	


#   Ejemplos de programas con sentencias SQL de manejo BD SQLite
#   - De la carpeta bbdd_SQLite importamos (ejecutamos) script ejemplosSQLite
from bbdd_SQLite import ejemplosSQLite


#   Lectura de directorios y ficheros y busqueda de ficheros (no funciona)
from modulo_os import prueba3


#   Pruebas de módulos con lectura de webs
from leerweb import prueba_urllib


#   Ejemplos de manejo de fechas
import Tiempos.fechass
# Vamos a usar de forma simple un prototipo de marcador de records, de manera
# que las puntuaciones en un juego puedan guardarse y conservarse de forma
# permanente. Para eso vamos a usar un tipo de base de datos llamado sqlite3.
# La interacción la hemos implementado en el archivo 'records.py' (mira su
# código). Importamos también el módulo de Python 'datetime' para trabajar
# con las funciones de hora y fecha.

import records, datetime


# Una vez importados los módulos, creamos la variable (el objeto) que contendrá
# la tabla de puntuaciones. La llamaremos simplemente 'tabla' y es una instancia
# de la clase 'Records', definida como hemos dicho en el archivo 'records.py'
tabla = records.Records()

# Bien. Vamos a hacer un bucle de manera que se muestren las puntuaciones
# almacenadas. Pediremos una nueva puntuación y cuando el usaurio la haya
# introducido se insertará en la base de datos de puntuaciones, de manera que
# en la próxima iteración se mostrará. Si el usaurio simplemente pulsa 'enter'
# el programa terminará.


while True:    
    # Primero, escribamos en pantalla una cabezera 'aparente'
    print ()
    print ("---------------------------------------------------------")
    print ("Lista de Puntuaciones")
    print ("---------------------------------------------------------")
    print ()
    
    # Ahora usamos la tabla para obtener el listado de puntuaciones. Para ello
    # sólo hay que invocar la función 'listado' de la tabla:
    puntuaciones = tabla.listado()
    
    # 'puntuaciones' tiene ahora el listado deseado. Para recorrerlo usaremos
    # un bucle 'for'; si la tabla está vacía no se hará nada. En el bucle,
    # la variable que representa cada uno de los elementos de la lista la
    # llamaremos 'registro':
    for registro in puntuaciones:
        
        # Como puedes ver en el código de 'records.py', cada registro de la tabla
        # de puntuaciones tiene tres campos; el primero es el nombre del jugador...
        nombre = registro[0]
        
        # ... el segundo son los puntos que obtuvo al jugar...
        puntos = registro[1]
        
        # ... y el tercero es el momento en el que lo hizo. En la tabla se almacena
        # como un número entero muy grande; es el número de segundos que han
        # transcurrido respecto de una determinada fecha que el sistema usa como
        # referencia. En el módulo 'datetime' que hemos importado al principio
        # tenemos la función 'datetime.fromtimestamp()' que convierte tal número
        # en un objeto que Python interpreta como una fecha. Vamos a almacenarlo
        # en una variable, digamos 'fecha':
        fecha = datetime.datetime.fromtimestamp(registro[2])
        
        # Los objetos de este tipo poseen un método muy útil, 'strftime()', que
        # permite mostrar la fecha con una gran flexibilidad. ¿Cómo? Pasándole
        # a la función como parámetro un cadena de texto; allí donde Python
        # encuentre el código especial '%d' lo sustituirá por el día, '%m' por el
        # més, '%y' por el año, '%H' por la hora, '%M' por los minutos y '%S' por
        # los segundos:
        textofecha = fecha.strftime('%d/%m/%y a las %H:%M')
        
        # Después de la línea anterior, fecha contendrá una expresión del estilo
        # de '25/12/2010 a las 23:15' (los valores concretos, claro, variarán
        # según sea el día en el que se guardó la puntuación).
        # Una vez conseguidos todos los datos, toca mostratlos. ¡Nada más fácil!
        print (puntos, 'puntos, conseguidos por', nombre, 'el', textofecha)
    
    # Terminado el bucle 'for', se han mostrado todas las puntuaciones. Ponemos
    # una línea y un poco de espacio.
    print ("---------------------------------------------------------")
    print ()
    
    # Es el turno de pedir al usuario que introduzca una nueva puntuación.
    nombre = input("Introduce nombre (pulsa 'enter' para terminar): ")
    
    # Si se pulsa 'enter' para terminar, hay que salir del bucle 'while'
    if nombre =='':
        break
    
    # Ahora toca introducir los puntos...
    puntos = input('Introduce puntos: ')
    
    # Ya tenemos todos los datos. Para introducirlos en la tabla y que así queden
    # queden guardados, vamos a usar el método 'guardarPuntos()' del objeto
    # 'tabla'. Los dos parámetros que hay que pasarle son el nombre del jugador
    # y los puntos que ha obtenido, ya que el propio objeto calcula el día
    # y la hora en que se ha producido.
    tabla.guardarPuntos(nombre, puntos)
import sqlite3, time, os

# La clase Records implementa un marcador muy sencillo para almacenar los
# puntos que han conseguido los jugadores sin que se pierdan al salir del programa.
# La clave es usar una base de datos. Python soporta muchas de ellas, pero la
# más sencilla (e incorporada en el propio lenguaje) es la conocida por sqlite3.
# En el código que incluímos a continuación se usan los comandos propios de este
# tipo de bases de datos (en el lenguaje denominado SQL) para realizar tareas
# sencillas. La ventaja de hacerlo así es que los programas que usen este módulo
# no necesitarán usarlos; bastará que usen las funciones más intuitivas que
# definimos aquí.


class Records:
    def __init__(self):
        # Lo primero es mirar si la base de datos existe ya. En tal caso se puede
        # usar pero, en caso contrario, hay que crearla. Esto, por supuesto,
        # ocurrirá la primera vez que se ejecute el programa.
        # Para ver si existe un archivo, lo más fácil es utilizar el módulo os
        # de python y su función path.exists
        if not os.path.exists('puntos.db'):
            
            # Vale. Si hemos llegado aquí es que la base no existe y hay que
            # crearla. Para ello usaremos la variable baseDatos y tendremos que
            # decirle a Python que va a ser una base de datos sqlite3, es decir,
            # 'conectarla'. El nombre del archivo que crearemos en el disco
            # duro puede ser el que queramos. Vamos a llamarlo 'puntos.db':
            self.baseDatos=sqlite3.connect('puntos.db')
            
            # Una vez creado y conectado el archivo, hemos de decirle qué tipo
            # de datos contiene. Las bases de datos están formadas 'tablas' y en
            # éstas hay 'registros'. Cada registro puede tener todos los datos que
            # queramos, pero hay que decidirlo al crear la tabla. En nuestro caso
            # nos basta con tener una tabla que llamaremos 'records' y cada uno
            # de los registros tendrá almacenados el nombre del jugador, los puntos
            # que ha sacado y el momento en el que lo ha hecho (lo que se conoce
            # comno 'campos' de los registros o de la base). Las bases sqlite3
            # pueden manejar tipos divdersos; aquí vamos a hacerlo sencillo y
            # vamos a usar cadenas de texto para el nombre y enteros para los
            # puntos y la fecha.
            # Para ejecutar instrucciones en en lenguaje SQL de las bases de datos
            # usaremos el comando de Python execute; la cadena de texto que le
            # pasemos como argumento será la tarea que se realice. En SQL las
            # tablas se crean escribiendo 'create table' segudi del nombre de la
            # tabla y de los nombres de los tipos de campo de los registros con
            # sus respectivos tipos:
            self.baseDatos.execute('''create table records
                        (nombre text, puntos int, fecha int)''')
        else:
            # En el caso de que sí que exista la base de datos no hace falta
            # crearla, basta simplemente conectar con ella:
            self.baseDatos=sqlite3.connect('puntos.db')
            
        # Con la base de datos ya en memoria, para poder manipularla necesitamos
        # un objeto conocido como 'cursor'. Es sobre él sobre quien se realizan
        # las consultas o las modificaciones. Lo vamos a almacenar en otra
        # propiedad, 'cursor'
        self.cursor=self.baseDatos.cursor()

    def __del__(self):
        # Éste es un método especial de Python. Igual que cuando se crea un
        # objeto se invoca automáticamente la función __init__ (conocida como
        # 'constructor'), cuando un objeto se elimina se invoca automáticamente
        # la función __del__ si existe (por eso se le suele conocer como
        # 'destructor'). Así éste es el lugar perfecto para poner el código que
        # deseamos que se ejecute cuando termine la vida del objeto. Con bases
        # de datos, aquí se suele llamar a la función close para cerrar la
        # conexión con el archivo del disco duro que contiene la base.
        self.baseDatos.close()

    def listado(self):
        # Esta función se encargará de devolver la lista de puntuaciones
        # almacenada. Con 'execute' hemos de pasarle al cursor de la base de
        # datos una cadena de texto con las instrucciones necesarias. En lenguaje
        # SQL, para seleccionar registros se usa 'select' seguido de la condición
        # que han de cumplir los registros que queremos (o de * si los queremos
        # todos); luego se escribe 'from' y el nombre de la tabla de donde
        # tomamos los datos e incluso se puede ordenar los resultados con
        # la instrucción 'order'. Observa que para que salgan de mayor puntuación
        # a menor, añadimos 'desc' detrás:
        self.cursor.execute('select * from records order by puntos desc')
        
        # Después de ejecutar la línea anterior, el cursor de la base de datos
        # contendrá todos los registros de la tabla 'records' ordenados de mayor
        # a menor según el campo 'puntos'.
        return self.cursor

    def guardarPuntos(self, nombre, puntos):
        # El objetivo de esta función es insertar en la base de datos un nuevo
        # registro que consiste en el nombre del jugador, los puntos que ha
        # obtenido y la fecha y hora en las que lo ha hecho. Los dos primeros
        # son los parámetros de la función, así que hay que calcular lo último.
        # Conseguimos saber el momento actual con la función time() del módulo
        # time. El resultado es un número entero muy grande que no es si no el
        # número de segundos que han transcurrido desde una determinada fecha
        # fija de referencia. Éste es el valor que almacenaremos en la base de
        # datos, ya que Python tiene métodos para hacer la conversión inversa.
        fecha = time.time()
        
        # En lenguaje SQL, para insertar registros en una tabla se escribe
        # 'insert into' seguido del nombre de la tabla. Además, para indicar
        # los valores que se van a insertar, hay que añadir 'values' y, entre
        # paréntesis, los valores en cuestión (el nombre, los puntos y la fecha).
        self.cursor.execute('''insert into records
                    values (\'%s\',\'%s\',\'%s\')''' % (nombre,puntos,fecha))
                    
        # Finalmente, para que el cambio tenga lugar de forma efectiva, se usa
        # el comando 'commit' (se hace así por si se produce un error o alguna
        # otra modificación y garantizar que la base no quede corrupta).
        self.baseDatos.commit()
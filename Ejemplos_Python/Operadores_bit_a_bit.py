================================================================================================
Operaciones bit a bit
================================================================================================
Operaciones b�sicas bit a bit
print 5 >> 4  # Right Shift			# devuelve 0
print 5 << 1  # Left Shift			# 10
print 8 & 5   # Bitwise AND			# 0
print 9 | 4   # Bitwise OR			# 13
print 12 ^ 42 # Bitwise XOR			# 38
print ~88     # Bitwise NOT			# -89
---------------------------------------------------------------------------------------------
N�meros en base 2   (nuestros n�meros est�n en base 10)  (n�meros binarios comienzan por 0b)
print 0b1,    		#1
print 0b10,   		#2
print 0b11,   		#3
print 0b100,  		#4
print 0b101,  		#5
print 0b110,  		#6
print 0b111   		#7
print "******"
print 0b1 + 0b11	# 4
print 0b11 * 0b11	# 11
one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight= 0b1000 
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100
---------------------------------------------------------------------------------------------
print bin(1)
for x in range(2,6):
    print bin(x)			# 0b1    0b10   0b11    0b100   0b101
---------------------------------------------------------------------------------------------
print int("1",2)			# int pasa un entero a entero
print int("10",2)			# pero admite un segundo par�metro para indicar la base
print int("111",2)			# convirtiendo una ceadena de binarios (base 2) a enteros
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int('11001001',2)
---------------------------------------------------------------------------------------------
# Left Bit Shift (<<)  
0b000001 << 2 == 0b000100 (1 << 2 = 4)
0b000101 << 3 == 0b101000 (5 << 3 = 40)       

# Right Bit Shift (>>)
0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
0b0000010 >> 2 == 0b000000 (2 >> 2 = 0) 
---------------------------------------------------------------------------------------------
shift_right = 0b1100
shift_left = 0b1
shift_right = shift_right >> 2		# 0b11
shift_left = shift_left << 2		# 0b100
---------------------------------------------------------------------------------------------
print bin(0b1110 & 0b101)     # 0b100  operador AND compara numeros binarios 0&*=0, 1&1=1
print bin(0b1110|0b101)		  # 0b1111 operador OR compara numeros binarios 0|0=0, 1|*=1
print bin(0b1110 ^ 0b101) 	  # 0b1011  o uno o otro
---------------------------------------------------------------------------------------------
print ~1		# -2	operador NOT 
print ~2		# -3
print ~3		# -4
print ~42		# -43
print ~123		# -124
---------------------------------------------------------------------------------------------
def check_bit4(input):    
    c = 0b1000				# funci�n que indica si el cuarto bit est� activo (es 1)
    suma = input & c
    if suma > 0:
        return 'on'
    else:
        return 'off'
print check_bit4(0b10000)
---------------------------------------------------------------------------------------------
a = 0b10111011
b = 0b100
mask = a | b				# activa el tercer bit a 1 de el numero binario a
print bin(mask)
---------------------------------------------------------------------------------------------
a = 0b11101110
b = 0b11111111				# cambia los 1 por ceros y los ceros por unos
print bin(a ^ b)	# 0b10001


================================================================================================
INTRODUCCI�N A CLASES (ORIENTADO A OBJETOS)
================================================================================================
class Fruit(object):
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous
    def description(self):
        print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)
    def is_edible(self):
        if not self.poisonous:
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)
lemon.description()		# I'm a yellow lemon and I taste sour.
lemon.is_edible()		# Yep! I'm edible.
------------------------------------------------------------------------------------------------
class Animal(object):
    pass   				# despu�s se rellena, se deja vac�o
------------------------------------------------------------------------------------------------
class Animal(object):
    def __init__(self):
        pass			# se deja la inicializaci�n vac�a para despu�s
------------------------------------------------------------------------------------------------
class Animal(object):
	is_alive = True  		# Variable interna de la clase Animal
    def __init__(self, name, age,is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry
zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)
print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry
------------------------------------------------------------------------------------------------
class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):		# hereda las variables y m�todos de Customer
    """For customers of the repeat variety."""
    def display_order_history(self):
        print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()
------------------------------------------------------------------------------------------------
class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
class Triangle(Shape):
    def __init__(self,side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
------------------------------------------------------------------------------------------------
class Employee(object):
    def __init__(self, name):
        self.name = name
    def greet(self, other):
        print "Hello, %s" % other.name
class CEO(Employee):						# se hereda el metodo greet pero se puede CAMBIAR
    def greet(self, other):
        print "Get back to work, %s!" % other.name
ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)     		# Hello, Emily
ceo.greet(emp)			# Get back to work, Steve!
------------------------------------------------------------------------------------------------
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00
class PartTimeEmployee(Employee): 		# nueva clase en la que los empleados cobran 12.00 por hora
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
------------------------------------------------------------------------------------------------
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
    def full_time_wage(self, hours):     # se utiliza SUPER para recuperar el metodo de la clase padre
        return super(PartTimeEmployee, self).calculate_wage(hours)
        
milton = PartTimeEmployee('Javi')
print milton.full_time_wage(10)
------------------------------------------------------------------------------------------------
class Triangle(object):
    number_of_sides = 3
    def __init__(self,angle1,angle2,angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False

class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle

my_triangle = Triangle(90,30,60)
print my_triangle.number_of_sides
print my_triangle.check_angles()
------------------------------------------------------------------------------------------------
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        return 'This is a %s %s with %s MPG.' % (self.color,self.model,str(self.mpg))
    def drive_car(self):
        self.condition = 'used'

class ElectricCar(Car):
    def __init__(self, model, color, mpg,battery_type):
        self.model = model
        self.color = color
        self.mpg   = mpg
        self.battery_type = battery_type
    def drive_car(self):
        self.condition = 'like new'
    
my_car = ElectricCar("DeLorean", "silver", 88,'molten salt')
print my_car.condition
my_car.drive_car()
print my_car.condition
------------------------------------------------------------------------------------------------
class Point3D(object):
    def __init__(self,x,y,z):		# m�todo para iniicializar el objeto de la clase
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):				# m�todo para representar el objeto de la clase (IMPRIMIR)
        return '(%d, %d, %d)' % (self.x, self.y, self.z)

my_point = Point3D(1,2,3)
print my_point						# (1, 2, 3)
------------------------------------------------------------------------------------------------
class Reversa:	# Ejemplo de clase como iterador (Iterador para recorrer una secuencia marcha atr�s)
	def __init__(self, datos):
        self.datos = datos
        self.indice = len(datos)
     def __iter__(self):		# para ser iterador tiene que tener este m�todo
        return self
     def next(self):			# para ser iterador tiene que tener este m�todo
        if self.indice == 0:
			raise StopIteration		# PARA salir del bucle iterativo
        self.indice = self.indice - 1
        return self.datos[self.indice]

for letra in Reversa('spam'):
     print letra

------------------------------------------------------------------------------------------------
Generador de listas
------------------------------------------------------------------------------------------------
my_list = [i**2 for i in range(1,11)] 	# Generates a list of squares of the numbers 1 - 10
------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------
LIBRER�A os: Tratamiento ficheros, directorios, borrado
------------------------------------------------------------------------------------------------
# Borrar todos los ficheros y subdirectorios de un directorio
# Delete everything reachable from the directory named in 'top',
# assuming there are no symbolic links.
# CAUTION:  This is dangerous!  For example, if top == '/', it
# could delete all your disk files.
import os
for root, dirs, files in os.walk(top, topdown=False):
   for name in files:
       os.remove(os.path.join(root, name))
   for name in dirs:
       os.rmdir(os.path.join(root, name))

Leer carpetas y archivos en python
-------------------------------------
from os import listdir

for cosa in listdir("."):   # entrada el path del directorio deseado
    print cosa				# imprime una lista con archivos y directorios
----------------------------------------------------------------------------------
from os import listdir
from os.path import isfile, join

mi_path = "."
solo_archivos = [							# lista por "compresi�n"
    cosa for cosa in listdir(mi_path)		# listdir devuelve una lista
    if isfile(join(mi_path, f))]			# solo nos quedamos con los archivos
for archivo in solo_archivos:				# join cunta el patch con el nombre de archivo
    print archivo
----------------------------------------------------------------------------------
from os import walk			# Recorremos todo el �rbol de archivos

for (path, ficheros, archivos) in walk("."):
    print path
    print ficheros	# �directorios?
    print archivos
----------------------------------------------------------------------------------
lista_arq = ls(ruta)   # no especificar ruta para tomar el directorio actual
----------------------------------------------------------------------------------
# 1) Mayor eficiencia con os.scandir() - python-3.5
# Devuelve un iterador a objetos que mantienen las propiedades de los archivos, haci�ndolo m�s eficiente
# (por ejemplo, no necesita realizar una llamada al sistema adicional para ver si un objeto es un archivo
# o un directorio).
from os import scandir, getcwd

def ls(ruta = getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]
# O si se quiere obtener la ruta absoluta de cada archivo:
from os import scandir, getcwd
form os.path import abspath

def ls(ruta = getcwd()):
    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]
----------------------------------------------------------------------------------
# 2) Con la librer�a pathlib y su clase principal Path - python-3.4
# Ofrece mayor nivel de consistencia entre los diferentes sistemas operativos, sin la necesidad de
# referenciar directamente a os, evitando tambi�n muchas llamadas al sistema.
from pathlib import Path

def ls(ruta = Path.cwd()):
    return [arch.name for arch in Path(ruta).iterdir() if arch.is_file()]
----------------------------------------------------------------------------------
# Mayor control con os.walk() - python-2.2 y python-3.x
# Se pueden obtener s�lo los archivos de forma m�s compacta:
from os import walk

def ls(ruta = '.'):
    return next(walk(ruta))[2]
# O se puede tener mayor control si se quiere, obteniendo dos listas (directorios y archivos)
from os import walk

def ls(ruta = '.'):
    dir, subdirs, archivos = next(walk(ruta))
    print("Actual: ", dir)
    print("Subdirectorios: ", subdirs)
    print("Archivos: ", archivos)
    return archivos
# Y si tambi�n se quiere obtener los archivos de todos los subdirectorios, permite iterar de la
#  siguiente forma:
from os import walk, getcwd

def ls(ruta = getcwd()):
    listaarchivos = []
    for (_, _, archivos) in walk(ruta):
        listaarchivos.extend(archivos)
    return listaarchivos

----------------------------------------------------------------------------------	
#Lista con el nombre de los archivos de una determinada extensi�n en un directorio

import os
#Variable para la ruta al directorio
path = '/home/zeito/'
 
#Lista vacia para incluir los ficheros
lstFiles = []
 
#Lista con todos los ficheros del directorio:
lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros
 
#Crea una lista de los ficheros jpg que existen en el directorio y los incluye a la lista.
for root, dirs, files in lstDir:
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if(extension == ".jpg"):
            lstFiles.append(nombreFichero+extension)
            #print (nombreFichero+extension)
             
print(lstFiles)            
print ('LISTADO FINALIZADO')
print "longitud de la lista = ", len(lstFiles)

Ejemplo lista de archvios, tama�o, fecha acceso
----------------------------------------------------------------------------------
# recogido de:  http://python-para-impacientes.blogspot.com.es/2015/09/explorando-directorios-con-listdir-walk.html
import os
from datetime import datetime

ruta_app = os.getcwd()  # obtiene ruta del script 
contenido = os.listdir(ruta_app)  # obtiene lista con archivos/dir 
total = 0
archivos = 0
formato = '%d-%m-%y %H:%M:%S'  # establece formato de fecha-hora
linea = '-' * 40

for elemento in contenido:
    archivo = ruta_app + os.sep + elemento
    if not os.access(archivo, os.X_OK) and os.path.isfile(archivo):
        archivos += 1
        estado = os.stat(archivo)  # obtiene estado del archivo
        tamano = estado.st_size  # obtiene de estado el tamano 
        
        # Obtiene del estado fechas de �ltimo acceso/modificaci�n
        # Como los valores de las fechas-horas vienen expresados
        # en segundos se convierten a tipo datetime. 
        
        ult_acceso = datetime.fromtimestamp(estado.st_atime)
        modificado = datetime.fromtimestamp(estado.st_mtime)
        
        # Se aplica el formato establecido de fecha y hora
        
        ult_acceso = ult_acceso.strftime(formato)
        modificado = modificado.strftime(formato)
        
        # Se acumulan tamanos y se muestra info de cada archivo
        
        total += tamano
        print(linea)
        print('archivo      :', elemento)
        print('modificado   :', modificado)        
        print('�ltimo acceso:', ult_acceso)
        print('tamano (Kb)  :', round(tamano/1024, 1))

print(linea)
print('N�m. archivos:', archivos)
print('Total (kb)   :', round(total/1024, 1))

''' Con if not os.access(archivo, os.X_OK) se verifica que el archivo no es ejecutable. El resto de modos que se pueden utilizar con os.access() son: 
os.F_OK para comprobar que es posible acceder a un archivo,
os.R_OK para saber si el archivo se puede leer y
os.W_OK para conocer si adem�s se permite la escritura.

Con la funci�n os.path.isfile(archivo) se comprueba si el elemento es un archivo. 

Por cierto, aunque hemos utilizado os.stat() comentar que hay funciones espec�ficas en el m�dulo os para obtener el tamano de un archivo os.path.getsize() y las fechas de �ltimo acceso os.path.getatime() y de �ltima modificaci�n os.path.getmtime(). 

Para finalizar, los m�todos de la clase stat son los siguientes (dependiendo del sistema algunos no estar�n disponibles): 
st_size: tamano en bytes.
st_mode: tipo de archivo y bits de permisos.
st_ino: n�mero de inodo.
st_dev: identificador del dispositivo.
st_uid: identificador del usuario propietario.
st_gid: identificador del grupo propietario.
st_atime: fecha-hora del �ltimo acceso (en segundos).
st_mtime: fecha-hora de la �ltima modificaci�n (en segundos).
st_ctime: fecha-hora ultimo cambio (unix) o creaci�n (win).
st_atime_ns, st_mtime_ns y st_ctime_ns (idem. expresado en nanoseg).
st_blocks: n�mero de bloques de 512 bytes asignados.
st_blksize: tamano de bloque preferido por sistema.
st_rdev: tipo de dispositivo si un dispositivo inode.
st_flags: banderas definidas por usuario.
st_gen: N�mero fichero generado.
st_birthtime: tiempo de creaci�n del archivo.
st_rsize: tamano real del archivo.
st_creator: creador del archivo.
st_type: tipo de archivo.
st_file_attributes: atributos.
'''

# Otra forma con Walk
import os
from datetime import datetime

ruta_app = os.getcwd()
total = 0
num_archivos = 0
formato = '%d-%m-%y %H:%M:%S'
linea = '-' * 60

for ruta, directorios, archivos in os.walk(ruta_app, topdown=True):
    print('\nruta       :', ruta) 
    for elemento in archivos:
        num_archivos += 1
        archivo = ruta + os.sep + elemento
        estado = os.stat(archivo)
        tamano = estado.st_size
        ult_acceso = datetime.fromtimestamp(estado.st_atime)
        modificado = datetime.fromtimestamp(estado.st_mtime)
        ult_acceso = ult_acceso.strftime(formato)
        modificado = modificado.strftime(formato)
        total += tamano
        print(linea)
        print('archivo      :', elemento)
        print('modificado   :', modificado)        
        print('�ltimo acceso:', ult_acceso)
        print('tamano (Kb)  :', round(tamano/1024, 1))

print(linea)
print('N�m. archivos:', num_archivos)
print('Total (kb)   :', round(total/1024, 1))

# Obtener iterador con las entradas de un directorio: scandir()

''' Para concluir, la funci�n os.scandir() devuelve un iterador basado en la clase DirEntry
que contiene informaci�n relacionada con las entradas (archivos y directorios) del directorio
indicado (path). La informaci�n no sigue ning�n tipo de orden predeterminado y no se incluyen,
si existen, las entradas '.' y '..'. 

os.scandir(path='.')
La clase DirEntry cuenta con m�todos que permiten acceder a informaci�n relativa a cada entrada: 

name: nombre del archivo o directorio le�do.
path: ruta completa del archivo o directorio le�do.
inode(): devuelve n�mero de inodo de la entrada.
is_dir(*, follow_symlinks=True): devuelve True si es directorio
is_file(*, follow_symlinks=True): devuelve True si es archivo
is_symlink(): devuelve True si es un enlace simb�lico.
stat(*, follow_symlinks=True): devuelve estado de la entrada

La funci�n os.scandir() se propone en Python 3.5 (PEP0471) como alternativa a os.listdir() al
mejorar la velocidad de acceso al sistema de ficheros por realizar menos llamadas a os.stat().
Adem�s, dependiendo del tipo de sistema y del tamano de los archivos la velocidad con os.walk()
puede ser m�s r�pida de 2 a 20 veces. 
'''

import os
from datetime import datetime

ruta_app = os.getcwd() 
total = 0
archivos = 0
formato = '%d-%m-%y %H:%M:%S'
linea = '-' * 40

contenido = os.scandir(ruta_app)
for elemento in contenido:
    if not os.access(elemento.path, os.X_OK) and elemento.is_file():
        archivos += 1
        estado = elemento.stat()        
        tamano = estado.st_size
        ult_acceso = datetime.fromtimestamp(estado.st_atime)
        modificado = datetime.fromtimestamp(estado.st_mtime)
        ult_acceso = ult_acceso.strftime(formato)
        modificado = modificado.strftime(formato)
        total += tamano
        print(linea)
        print('archivo      :', elemento.name)
        print('permisos     :', estado.st_mode)
        print('modificado   :', modificado)        
        print('�ltimo acceso:', ult_acceso)
        print('tamano (Kb)  :', round(tamano/1024, 1))

print(linea)
print('N�m. archivos:', archivos)
print('Total (kb)   :', round(total/1024, 1))

--------------------------------------------------------------------------------------------
# Listar el tama�o en bytes de cada archivo de un path
--------------------------------------------------------------------------------------------
import os
from os.path import join, getsize

for root, dirs, files in os.walk('python/Lib/email'):
   print root, "consumes",
   print sum(getsize(join(root, name)) for name in files),
   print "bytes in", len(files), "non-directory files"
   if 'CVS' in dirs:
       dirs.remove('CVS')  # don't visit CVS directories

--------------------------------------------------------------------------------------------
import os, glob, sys

print os.name               # posix   (unix)
print os.getuid()			# 3360    (usuario)
print os.getcwd()			# /home/run2359  (dir. actual)
print sys.version_info		# sys.version_info(major=2, minor=7, micro=3, releaselevel='final', serial=0)

print glob.glob('*.*')		# ['script.py']  (lista con los archivos en directorio)

path = "/home/run2359"
 
for (path, dirs, files) in os.walk(path):
    print("----")			# ----
    print(path)				# /home/run2359
    print(dirs)				# []
    print(files)			# ['script.py']

===========================================================================================================	
El m�dulo pickle
-----------------
Las cadenas pueden facilmente escribirse y leerse de un archivo. Los n�meros toman algo m�s de esfuerzo, 
ya que el m�todo read() s�lo devuelve cadenas, que tendr�n que ser pasadas a una funci�n como int(), que 
toma una cadena como '123' y devuelve su valor num�rico 123. Sin embargo, cuando quer�s grabar tipos de datos
m�s complejos como listas, diccionarios, o instancias de clases, las cosas se ponen m�s complicadas.

En lugar de tener a los usuarios constantemente escribiendo y debugueando c�digo para grabar tipos de datos
complicados, Python provee un m�dulo est�ndar llamado pickle. Este es un asombroso m�dulo que puede tomar casi
cualquier objeto Python (�incluso algunas formas de c�digo Python!), y convertirlo a una representaci�n de
cadena; este proceso se llama picklear. Reconstruir los objetos desde la representaci�n en cadena se llama
despicklear. Entre que se picklea y se despicklea, la cadena que representa al objeto puede almacenarse en un
archivo, o enviarse a una m�quina distante por una conexi�n de red.

Si ten�s un objeto x, y un objeto archivo f que fue abierto para escritura, la manera m�s simple de picklear
el objeto toma una sola linea de c�digo: '''

pickle.dump(x, f)

# Para despicklear el objeto, si f es un objeto archivo que fue abierto para lectura: 

x = pickle.load(f)

'''(Hay otras variantes de esto, usadas al picklear muchos objetos o cuando no quer�s escribir los datos
pickleados a un archivo; consult� la documentaci�n completa para pickle en la Referencia de la Biblioteca
de Python.)

pickle es la manera est�ndar de hacer que los objetos Python puedan almacenarse y reusarse por otros
programas o por una futura invocaci�n al mismo programa; el t�rmino t�cnico de esto es un objeto persistente.
Ya que pickle es tan ampliamente usado, muchos autores que escriben extensiones de Python toman el cuidado
de asegurarse que los nuevos tipos de datos, como matrices, puedan ser adecuadamente pickleados y
despickleados.
===========================================================================================================
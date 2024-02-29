------------------------------------------------------------------------------------------------
Generador de listas por iteradores
------------------------------------------------------------------------------------------------
Lista = [i**2 for i in range(1,11)] 	# Genera una lista con los cuadrados de los números del 1-10

------------------------------------------------------------------------------------------------
CONSTRUYENDO LISTAS con for in y if
------------------------------------------------------------------------------------------------
evens_to_50 = [i for i in range(51) if i % 2 == 0]            # pares menoes 50
print evens_to_50

doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]    # dobles diivisibles 3
print doubles_by_3

even_squares = [x**2 for x in range(1,12) if x % 2 == 0]      # cuadrados de pares
print even_squares
---------------------------------------------------------------------------------------------
c = ['C' for x in range(5) if x < 3]
print c      # devuelve ['C', 'C', 'C']
---------------------------------------------------------------------------------------------
cubes_by_four = [x**3 for x in range(1,11)   # cubos de num. entre 1 y 10 divisibles entre 4
    if x**3 % 4 == 0]
print cubes_by_four
---------------------------------------------------------------------------------------------
COGIENDO TROZOS DE LISTAS
-------------------------
l = [i ** 2 for i in range(1, 11)]
print l         # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print l[2:9:1]  # [9, 16, 25, 36, 49, 64, 81]   del 2 incluido(empieza en 0) al 9 excluido
print l[2:9:2]	#[9, 25, 49, 81] del 2 al 9 pero de dos en dos
---------------------------------------------------------------------------------------------
my_list = range(1, 11) 	# Lista de numbers 1 - 10
print my_list[::2]     	# saca los numeros impares (desde el principio, cada dos)
print my_list[::9]		# saca el primero y 9 números después, el último
---------------------------------------------------------------------------------------------
my_list = range(1, 11) 		# lista del 1 al 10
backwards = my_list[::-1] 	# lista invertida, del 10 al 1
print backwards
---------------------------------------------------------------------------------------------
to_one_hundred = range(101)					# lista de 1 a 100
backwards_by_tens = to_one_hundred[::-10]	# lista invertida de 100 a 10 (de 10 en 10)
print backwards_by_tens
---------------------------------------------------------------------------------------------
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)
---------------------------------------------------------------------------------------------
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)
---------------------------------------------------------------------------------------------
threes_and_fives = [x for x in range(1,16) 
                if x % 3 == 0 or x % 5 == 0]
print threes_and_fives				# [3, 5, 6, 9, 10, 12, 15]
---------------------------------------------------------------------------------------------
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-1]
print message   			# IX XaXmX XtXhXeX XsXeXcXrXeXtX XmXeXsXsXaXgXeX!
message = message[::2]
print message				# I am the secret message!
---------------------------------------------------------------------------------------------
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x:x != 'X' ,garbled)
print message				# I am another secret message!

------------------------------------------------------------------------------------------------
Diccionarios
------------------------------------------------------------------------------------------------
my_dict = { 'nombre':'Javi',
            'edad':25,
            'sexo':'V'}

print my_dict.items()     	# displaya claves y valores
print my_dict.keys()		# displaya claves
print my_dict.values()		# displaya valores

for key in my_dict:
    print key, my_dict[key]

================================================================================================
Ejemplo Loops (flujos) en listas
================================================================================================
count = 0
if count < 5:
    print "Hello, I am an if statement and count is", count
while count < 9:
    print "Hello, I am a while and count is", count
    count += 1
--------------------------------------------------------------------
loop_condition = True
while loop_condition:
    print "I am a loop"
    loop_condition = False
--------------------------------------------------------------------
num = 1
while num <11:  # Fill in the condition
    # Print num squared (al cuadrado)
    print num ** 2
    # Increment num (make sure to do this!)
    num += 1
--------------------------------------------------------------------
choice = raw_input('Enjoying the course? (y/n)')
while choice != 'y' and choice !='n':  
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")	
--------------------------------------------------------------------
count = 0
while True:
    print count
    count += 1
    if count >= 10:
        break
--------------------------------------------------------------------
import random
print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"
count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break         # Al salir con break no se ejecuta el else
    count += 1
else:
    print "You win!"  # si sale por count >=3 se ejecuta el else
--------------------------------------------------------------------
from random import randint
# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
guesses_left = 3
# Start your game!
while guesses_left > 0:
    guess = int(raw_input('Your guess: '))
    if guess == random_number:
        print 'You win!'
        break
    else:
        guesses_left -= 1
else:
    print 'You lose.'
--------------------------------------------------------------------
print "Counting..."
for i in range(20):       # bucle for
    print i
--------------------------------------------------------------------
hobbies = []
# Add your code below!
for i in range(3):
    hobbi = raw_input('Hobbi: ')
    hobbies.append(hobbi)
print hobbies
--------------------------------------------------------------------
thing = "spam!"
for c in thing:			#bucle for para recorrer un string.
    print c
word = "eggs!"
# Your code here!
for a in word:
    print a
--------------------------------------------------------------------
phrase = "A bird in the hand..."
# Add your for loop
for char in phrase:
    if char == 'A' or char == 'a':
        print 'X',      #ponemos , para sacar en la misma linea
    else:
        print char,     #ponemos , para sacar en la misma linea
#Don't delete this print statement!
print
--------------------------------------------------------------------
numbers  = [7, 9, 12, 54, 99]
print "This list contains: "
for num in numbers:
    print num
# Add your loop below!
for num in numbers:
    print num ** 2,
print
--------------------------------------------------------------------
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}
for key in d:
    # Your code here!
    print key,			# imprime clave, un espacio ","
    print d[key]		# imprime valor
--------------------------------------------------------------------
choices = ['pizza', 'pasta', 'salad', 'nachos']
print 'Your choices are:'
for index, item in enumerate(choices):
    print index + 1, item	# index toma el valor del lugar en la lista
--------------------------------------------------------------------
MULTIPLES LISTAS
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):    # zip trata varias listas
    # Add your code here!           # bucle recorre la lista mas corta
    if a > b:						# puede tratar más de dos listas
        print a
    else:
        print b
--------------------------------------------------------------------
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']
print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'

================================================================================================
Funciones
================================================================================================
def is_even(x):        # is_even = es divisible entre 2
    if x % 2 == 0:
        return True
    else:
        return False
--------------------------------------------------------------------------------
def factorial(x):     # funcion recursiva
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x * factorial(x-1)
--------------------------------------------------------------------------------
def is_prime(x):       	# primo si es positivo mayor que uno y 
    if x < 2:			# no divisible más que por el o por 1
        return False
    else:
        for n in range(2,x-1):
            if x % n == 0:
                return False
                break
        else:
            return True
for a in range (8):		# prueba de los 8 primeros números
    print a, is_prime(a)
--------------------------------------------------------------------------------
def reverse(text):      # funcion recursiva para dar la vuelta a un texto
    if len(text) == 1:
        return text
    else:
        return reverse(text[1:len(text)]) + text[0]    
--------------------------------------------------------------------------------
def anti_vowel(text):    # funcion que elimina las vocales del texto
    retorno = ''
    for letra in text:
        if not letra in 'aeiouAEIOU':
            retorno += letra
    return retorno
--------------------------------------------------------------------------------
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
def scrabble_score(word):       # calcula puntos de la palabra
    puntos = 0
    if word == '':
        return 0
    else:
        for a in word.lower():
            puntos += score[a]
    return puntos
--------------------------------------------------------------------------------
def censor(text,word):       # funcion que sustituye word por asteriscos
    if not word in text:
        return text
    else:
        a = "*" * len(word)
        return a.join(text.split(word))
print censor('this hack is wack hack', "hack")
--------------------------------------------------------------------------------
def count(sequence,item):	# cuenta las veces que aparece item en la lista sequence
    return sequence.count(item)     

lista = [1,2,1,1]
lista1 =[['a','a'],['a'],['a','b'],['a','b']]
i = ['a','b']
print count(lista,1)
print count(lista1,i)
--------------------------------------------------------------------------------
def purify(lista):    # devuelve los numeros pares de una lista
    salida = []
    for a in lista:
        if a % 2 == 0:
            salida.append(a)
    return salida

print purify([1,2,3,4,5])
--------------------------------------------------------------------------------
def remove_duplicates(lista):
    salida = []
    for a in lista:
        if not a in salida:
            salida.append(a)
    return salida
    
print remove_duplicates([1,1,2,2])
--------------------------------------------------------------------------------
def median(lista):
    l = sorted(lista)
    if len(l) % 2 != 0:
        return l[int(len(l) / 2)]
    else:
        m = int(len(l) / 2)
        return (l[m - 1] + l[m]) / 2.0

lis1 = [4,5,5,4]
lis2 = [1,3,6,7,12]
print median(lis1)
print median(lis2)
------------------------------------------------------------------------------------

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return variance / len(scores)

def grades_std_deviation(var):
    return var ** 0.5

print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
variance = grades_variance(grades)
print variance
print grades_std_deviation(variance)


================================================================================================
Funciones con Dicicionarios
================================================================================================
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)
    
def get_average(student):
    homework = average(student['homework'])
    quizzes = average(student['quizzes'])
    tests = average(student['tests'])
    return int(0.1 * homework + 0.3 * quizzes + 0.6 * tests)
    
def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return int(average(results))

estudiantes = [alice, lloyd, tyler]
print get_class_average(estudiantes)
print get_letter_grade(get_class_average(estudiantes))

================================================================================================
Operaciones bit a bit
================================================================================================
Operaciones básicas bit a bit
print 5 >> 4  # Right Shift			# devuelve 0
print 5 << 1  # Left Shift			# 10
print 8 & 5   # Bitwise AND			# 0
print 9 | 4   # Bitwise OR			# 13
print 12 ^ 42 # Bitwise XOR			# 38
print ~88     # Bitwise NOT			# -89
---------------------------------------------------------------------------------------------
Números en base 2   (nuestros números están en base 10)  (números binarios comienzan por 0b)
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
print int("10",2)			# pero admite un segundo parámetro para indicar la base
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
    c = 0b1000				# función que indica si el cuarto bit está activo (es 1)
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
INTRODUCCIÓN A CLASES (ORIENTADO A OBJETOS)
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
    pass   				# después se rellena, se deja vacío
------------------------------------------------------------------------------------------------
class Animal(object):
    def __init__(self):
        pass			# se deja la inicialización vacía para después
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

class ReturningCustomer(Customer):		# hereda las variables y métodos de Customer
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
    def __init__(self,x,y,z):		# método para iniicializar el objeto de la clase
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):				# método para representar el objeto de la clase (IMPRIMIR)
        return '(%d, %d, %d)' % (self.x, self.y, self.z)

my_point = Point3D(1,2,3)
print my_point						# (1, 2, 3)
------------------------------------------------------------------------------------------------
class Reversa:	# Ejemplo de clase como iterador (Iterador para recorrer una secuencia marcha atrás)
	def __init__(self, datos):
        self.datos = datos
        self.indice = len(datos)
     def __iter__(self):		# para ser iterador tiene que tener este método
        return self
     def next(self):			# para ser iterador tiene que tener este método
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
LIBRERÍA os: Tratamiento ficheros, directorios, borrado
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
solo_archivos = [							# lista por "compresión"
    cosa for cosa in listdir(mi_path)		# listdir devuelve una lista
    if isfile(join(mi_path, f))]			# solo nos quedamos con los archivos
for archivo in solo_archivos:				# join cunta el patch con el nombre de archivo
    print archivo
----------------------------------------------------------------------------------
from os import walk			# Recorremos todo el árbol de archivos

for (path, ficheros, archivos) in walk("."):
    print path
    print ficheros	# ¿directorios?
    print archivos
----------------------------------------------------------------------------------
lista_arq = ls(ruta)   # no especificar ruta para tomar el directorio actual
----------------------------------------------------------------------------------
# 1) Mayor eficiencia con os.scandir() - python-3.5
# Devuelve un iterador a objetos que mantienen las propiedades de los archivos, haciéndolo más eficiente
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
# 2) Con la librería pathlib y su clase principal Path - python-3.4
# Ofrece mayor nivel de consistencia entre los diferentes sistemas operativos, sin la necesidad de
# referenciar directamente a os, evitando también muchas llamadas al sistema.
from pathlib import Path

def ls(ruta = Path.cwd()):
    return [arch.name for arch in Path(ruta).iterdir() if arch.is_file()]
----------------------------------------------------------------------------------
# Mayor control con os.walk() - python-2.2 y python-3.x
# Se pueden obtener sólo los archivos de forma más compacta:
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
# Y si también se quiere obtener los archivos de todos los subdirectorios, permite iterar de la
#  siguiente forma:
from os import walk, getcwd

def ls(ruta = getcwd()):
    listaarchivos = []
    for (_, _, archivos) in walk(ruta):
        listaarchivos.extend(archivos)
    return listaarchivos

----------------------------------------------------------------------------------	
#Lista con el nombre de los archivos de una determinada extensión en un directorio

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

Ejemplo lista de archvios, tamaño, fecha acceso
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
        
        # Obtiene del estado fechas de último acceso/modificación
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
        print('último acceso:', ult_acceso)
        print('tamano (Kb)  :', round(tamano/1024, 1))

print(linea)
print('Núm. archivos:', archivos)
print('Total (kb)   :', round(total/1024, 1))

''' Con if not os.access(archivo, os.X_OK) se verifica que el archivo no es ejecutable. El resto de modos que se pueden utilizar con os.access() son: 
os.F_OK para comprobar que es posible acceder a un archivo,
os.R_OK para saber si el archivo se puede leer y
os.W_OK para conocer si además se permite la escritura.

Con la función os.path.isfile(archivo) se comprueba si el elemento es un archivo. 

Por cierto, aunque hemos utilizado os.stat() comentar que hay funciones específicas en el módulo os para obtener el tamano de un archivo os.path.getsize() y las fechas de último acceso os.path.getatime() y de última modificación os.path.getmtime(). 

Para finalizar, los métodos de la clase stat son los siguientes (dependiendo del sistema algunos no estarán disponibles): 
st_size: tamano en bytes.
st_mode: tipo de archivo y bits de permisos.
st_ino: número de inodo.
st_dev: identificador del dispositivo.
st_uid: identificador del usuario propietario.
st_gid: identificador del grupo propietario.
st_atime: fecha-hora del último acceso (en segundos).
st_mtime: fecha-hora de la última modificación (en segundos).
st_ctime: fecha-hora ultimo cambio (unix) o creación (win).
st_atime_ns, st_mtime_ns y st_ctime_ns (idem. expresado en nanoseg).
st_blocks: número de bloques de 512 bytes asignados.
st_blksize: tamano de bloque preferido por sistema.
st_rdev: tipo de dispositivo si un dispositivo inode.
st_flags: banderas definidas por usuario.
st_gen: Número fichero generado.
st_birthtime: tiempo de creación del archivo.
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
        print('último acceso:', ult_acceso)
        print('tamano (Kb)  :', round(tamano/1024, 1))

print(linea)
print('Núm. archivos:', num_archivos)
print('Total (kb)   :', round(total/1024, 1))

# Obtener iterador con las entradas de un directorio: scandir()

''' Para concluir, la función os.scandir() devuelve un iterador basado en la clase DirEntry
que contiene información relacionada con las entradas (archivos y directorios) del directorio
indicado (path). La información no sigue ningún tipo de orden predeterminado y no se incluyen,
si existen, las entradas '.' y '..'. 

os.scandir(path='.')
La clase DirEntry cuenta con métodos que permiten acceder a información relativa a cada entrada: 

name: nombre del archivo o directorio leído.
path: ruta completa del archivo o directorio leído.
inode(): devuelve número de inodo de la entrada.
is_dir(*, follow_symlinks=True): devuelve True si es directorio
is_file(*, follow_symlinks=True): devuelve True si es archivo
is_symlink(): devuelve True si es un enlace simbólico.
stat(*, follow_symlinks=True): devuelve estado de la entrada

La función os.scandir() se propone en Python 3.5 (PEP0471) como alternativa a os.listdir() al
mejorar la velocidad de acceso al sistema de ficheros por realizar menos llamadas a os.stat().
Además, dependiendo del tipo de sistema y del tamano de los archivos la velocidad con os.walk()
puede ser más rápida de 2 a 20 veces. 
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
        print('último acceso:', ult_acceso)
        print('tamano (Kb)  :', round(tamano/1024, 1))

print(linea)
print('Núm. archivos:', archivos)
print('Total (kb)   :', round(total/1024, 1))

--------------------------------------------------------------------------------------------
# Listar el tamaño en bytes de cada archivo de un path
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
El módulo pickle
-----------------
Las cadenas pueden facilmente escribirse y leerse de un archivo. Los números toman algo más de esfuerzo, 
ya que el método read() sólo devuelve cadenas, que tendrán que ser pasadas a una función como int(), que 
toma una cadena como '123' y devuelve su valor numérico 123. Sin embargo, cuando querés grabar tipos de datos
más complejos como listas, diccionarios, o instancias de clases, las cosas se ponen más complicadas.

En lugar de tener a los usuarios constantemente escribiendo y debugueando código para grabar tipos de datos
complicados, Python provee un módulo estándar llamado pickle. Este es un asombroso módulo que puede tomar casi
cualquier objeto Python (¡incluso algunas formas de código Python!), y convertirlo a una representación de
cadena; este proceso se llama picklear. Reconstruir los objetos desde la representación en cadena se llama
despicklear. Entre que se picklea y se despicklea, la cadena que representa al objeto puede almacenarse en un
archivo, o enviarse a una máquina distante por una conexión de red.

Si tenés un objeto x, y un objeto archivo f que fue abierto para escritura, la manera más simple de picklear
el objeto toma una sola linea de código: '''

pickle.dump(x, f)

# Para despicklear el objeto, si f es un objeto archivo que fue abierto para lectura: 

x = pickle.load(f)

'''(Hay otras variantes de esto, usadas al picklear muchos objetos o cuando no querés escribir los datos
pickleados a un archivo; consultá la documentación completa para pickle en la Referencia de la Biblioteca
de Python.)

pickle es la manera estándar de hacer que los objetos Python puedan almacenarse y reusarse por otros
programas o por una futura invocación al mismo programa; el término técnico de esto es un objeto persistente.
Ya que pickle es tan ampliamente usado, muchos autores que escriben extensiones de Python toman el cuidado
de asegurarse que los nuevos tipos de datos, como matrices, puedan ser adecuadamente pickleados y
despickleados.
===========================================================================================================
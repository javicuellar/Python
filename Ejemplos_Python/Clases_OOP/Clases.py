# ================================================================================================
#    INTRODUCCION A CLASES (ORIENTADO A OBJETOS)
# ================================================================================================
class Fruit(object):
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous
    def description(self):
        print("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))
    def is_edible(self):
        if not self.poisonous:
            print("Yep! I'm edible.")
        else:
            print("Don't eat me! I am super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)
lemon.description()		# I'm a yellow lemon and I taste sour.
lemon.is_edible()		# Yep! I'm edible.

# ------------------------------------------------------------------------------------------------
class Animal(object):
    pass   				# después se rellena, se deja vacío

# ------------------------------------------------------------------------------------------------
class Animal(object):
    def __init__(self):
        pass			# se deja la inicialización vacía para después

#------------------------------------------------------------------------------------------------
class Animal(object):
    is_alive = True  		# Variable interna de la clase Animal
    def __init__(self, name, age,is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print(zebra.name, zebra.age, zebra.is_hungry)
print(giraffe.name, giraffe.age, giraffe.is_hungry)
print(panda.name, panda.age, panda.is_hungry)

# ------------------------------------------------------------------------------------------------
class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print("I'm a string that stands in for the contents of your shopping cart!")

class ReturningCustomer(Customer):		# hereda las variables y métodos de Customer
    """For customers of the repeat variety."""
    def display_order_history(self):
        print("I'm a string that stands in for your order history!")

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

# ------------------------------------------------------------------------------------------------
class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
class Triangle(Shape):
    def __init__(self,side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

# ------------------------------------------------------------------------------------------------
class Employee(object):
    def __init__(self, name):
        self.name = name
    def greet(self, other):
        print("Hello, %s" % other.name)
class CEO(Employee):						# se hereda el metodo greet pero se puede CAMBIAR
    def greet(self, other):
        print("Get back to work, %s!" % other.name)

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)     		    # Hello, Emily
ceo.greet(emp)			    # Get back to work, Steve!

# ------------------------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------------------------
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
print(milton.full_time_wage(10))

# ------------------------------------------------------------------------------------------------
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
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())

# ------------------------------------------------------------------------------------------------
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
print(my_car.condition)
my_car.drive_car()
print(my_car.condition)

# ------------------------------------------------------------------------------------------------
class Point3D(object):
    def __init__(self,x,y,z):		# m�todo para iniicializar el objeto de la clase
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):				# m�todo para representar el objeto de la clase (IMPRIMIR)
        return '(%d, %d, %d)' % (self.x, self.y, self.z)

my_point = Point3D(1,2,3)
print(my_point)						# (1, 2, 3)

# ------------------------------------------------------------------------------------------------
class Reversa:	        # Ejemplo de clase como iterador (Iterador para recorrer una secuencia marcha atrás)
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
     print(letra)
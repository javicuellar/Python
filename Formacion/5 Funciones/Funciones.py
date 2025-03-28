# ================================================================================================
#    Funciones
# ================================================================================================
# is_even = es divisible entre 2
def is_even(x=1):           # si x no viene informado toma por defecto el valor 1
    if x % 2 == 0:
        return True
    else:
        return False

# --------------------------------------------------------------------------------
def factorial(x):           # funcion recursiva
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x * factorial(x-1)   # Llama recursivamente hasta que x es menor que 2

# --------------------------------------------------------------------------------
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

for a in range (8):		# prueba de los 8 primeros n�meros
    print(a, is_prime(a))

# --------------------------------------------------------------------------------
def reverse(text):      # funcion recursiva para dar la vuelta a un texto
    if len(text) == 1:
        return text
    else:
        return reverse(text[1:len(text)]) + text[0]

# --------------------------------------------------------------------------------
def anti_vowel(text):    # funcion que elimina las vocales del texto
    retorno = ''
    for letra in text:
        if not letra in 'aeiouAEIOU':
            retorno += letra
    return retorno

# --------------------------------------------------------------------------------
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

# --------------------------------------------------------------------------------
def censor(text,word):       # funcion que sustituye word por asteriscos
    if not word in text:
        return text
    else:
        a = "*" * len(word)
        return a.join(text.split(word))

print(censor('this hack is wack hack', "hack"))

# --------------------------------------------------------------------------------
def count(sequence,item):	# cuenta las veces que aparece item en la lista sequence
    return sequence.count(item)     

lista = [1,2,1,1]
lista1 = [['a','a'],['a'],['a','b'],['a','b']]
i = ['a','b']

print(count(lista, 1))
print(count(lista1, i))

# --------------------------------------------------------------------------------
def purify(lista):    # devuelve los numeros pares de una lista
    salida = []
    for a in lista:
        if a % 2 == 0:
            salida.append(a)
    return salida

print(purify([1,2,3,4,5]))

# --------------------------------------------------------------------------------
def remove_duplicates(lista):
    salida = []
    for a in lista:
        if not a in salida:
            salida.append(a)
    return salida
    
print(remove_duplicates([1,1,2,2]))

# --------------------------------------------------------------------------------
def median(lista):
    l = sorted(lista)
    if len(l) % 2 != 0:
        return l[int(len(l) / 2)]
    else:
        m = int(len(l) / 2)
        return (l[m - 1] + l[m]) / 2.0

lis1 = [4,5,5,4]
lis2 = [1,3,6,7,12]
print(median(lis1))
print(median(lis2))

# ------------------------------------------------------------------------------------
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print(grade)

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
print(grades_sum(grades))
print(grades_average(grades))

variance = grades_variance(grades)
print(variance)
print(grades_std_deviation(variance))
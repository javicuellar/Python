# ================================================================================================
#    Ejemplo Loops (flujos) en listas - FOR
# ================================================================================================

print("Counting...")
for i in range(20):       # bucle for
    print(i)

# --------------------------------------------------------------------
hobbies = []
# Add your code below!
for i in range(3):
    hobbi = input('Hobbi: ')
    hobbies.append(hobbi)
print(hobbies)

# --------------------------------------------------------------------
thing = "spam!"
for c in thing:			# bucle for para recorrer un string.
    print(c)

word = "eggs!"
# Your code here!
for a in word:
    print(a)

# --------------------------------------------------------------------
phrase = "A bird in the hand..."
# Add your for loop
for char in phrase:
    if char == 'A' or char == 'a':
        print('X'),      #ponemos , para sacar en la misma linea
    else:
        print(char),     #ponemos , para sacar en la misma linea
#Don't delete this print statement!
print()

# --------------------------------------------------------------------
numbers  = [7, 9, 12, 54, 99]
print("This list contains: ")
for num in numbers:
    print(num)
# Add your loop below!
for num in numbers:
    print(num ** 2,)
print()

# --------------------------------------------------------------------
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}
for key in d:
    # Your code here!
    print(key,)			# imprime clave, un espacio ","
    print(d[key])		# imprime valor

# --------------------------------------------------------------------
choices = ['pizza', 'pasta', 'salad', 'nachos']
print('Your choices are:')
for index, item in enumerate(choices):
    print(index + 1, item)  	# index toma el valor del lugar en la lista

# --------------------------------------------------------------------
# MULTIPLES LISTAS
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):    # zip trata varias listas
    # Add your code here!           # bucle recorre la lista mas corta
    if a > b:						# puede tratar m�s de dos listas
        print(a)
    else:
        print(b)

# --------------------------------------------------------------------
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']
print('You have...')
for f in fruits:
    if f == 'tomato':
        print('A tomato is not a fruit!')       # (It actually is.)
        break
    print ('A', f)
else:
    print('A fine selection of fruits!')
# ================================================================================================
#    Ejemplo Loops (flujos) en listas
# ================================================================================================
count = 0
if count < 5:
    print("Hello, I am an if statement and count is", count)
while count < 9:
    print("Hello, I am a while and count is", count)
    count += 1

# --------------------------------------------------------------------
loop_condition = True
while loop_condition:
    print("I am a loop")
    loop_condition = False

# --------------------------------------------------------------------
num = 1
while num <11:  # Fill in the condition
    # Print num squared (al cuadrado)
    print(num ** 2)
    # Increment num (make sure to do this!)
    num += 1

# --------------------------------------------------------------------
choice = input('Enjoying the course? (y/n)')
while choice != 'y' and choice !='n':  
    choice = input("Sorry, I didn't catch that. Enter again: ")

# --------------------------------------------------------------------
count = 0
while True:
    print(count)
    count += 1
    if count >= 10:
        break

# --------------------------------------------------------------------
import random
print("Lucky Numbers! 3 numbers will be generated.")
print("If one of them is a '5', you lose!")

count = 0
while count < 3:
    num = random.randint(1, 6)
    print(num)
    if num == 5:
        print("Sorry, you lose!")
        break           # Al salir con break no se ejecuta el else
    else:
        print("You win!")       # si sale por count >=3 se ejecuta el else
    count += 1

# --------------------------------------------------------------------
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
guesses_left = 3

# Start your game!
while guesses_left > 0:
    guess = int(input('Your guess: '))
    if guess == random_number:
        print('You win!')
        break
    else:
        guesses_left -= 1
else:
    print('You lose.')
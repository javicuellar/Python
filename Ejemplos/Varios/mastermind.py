#   Módulo que permite elegir números aleatoriamente
import random

# Conjunto de símbolos válidos en el código a descubrir.
digitos = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

codigo = ''
for i in range(4):
	while True:
		cifra = random.choice(digitos)
		# no se permiten cifras repetidas
		if cifra not in codigo:
			codigo += cifra
			break

# Iniciamos la interacción con el usuario
print ('Bienvenido/a al Masterind!')
print ('Tienes que adivinar un número de 4 cifras distintas')

# Iniciamos el número de intentos y la propuesta del jugador
propuesta = ''
intento = 0

while codigo != propuesta:
	propuesta = input('Introduce la propuesta: ')
	
	# inicializamos el número de aciertos y coincidencias e incrementamos el número de intentos.
	acierto, coincidencia = 0, 0
	intento += 1
	
	# recorremos las cifras de la propuesta y verificamos con el código
	for i in range(4):
		if propuesta[i] == codigo[i]:
			acierto += 1
		elif propuesta[i] in codigo:
			coincidencia += 1
	
	print ('Has tenido ', acierto, ' aciertos y ', coincidencia, ' coincidencias.')

print ('Felicidades!, adivinaste el código en ', intento, ' intentos.')

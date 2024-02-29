# Ficheros: apertura, lectura, escritura (input/output)
# -----------------------------------------------------
from time import time	#importamos la función time para capturar tiempos


f = open("d:\\python\\Ficheros\\output.txt", "w")  				# w para escribir, r+ para 
# f = open("C:\\Users\\u526101\\Downloads\\output.txt", "w")  		# fichero en c: por limitación en disco d:

a = 1000    
b = 1

tiempo_inicial = time() 		# medimos la hora de inicio.

for item in range(b,a+b):
	cadena = str(item).zfill(9)						# rellenar zeros por la izquierda a una cadena.
	texto = ('Javi ' + str(item)).ljust(50, " ")	# rellena espacios a la izquierda
	reg = cadena + texto + texto +'-'
	f.write(reg + "\n")								# se utiliza '\n' para saltar a la siguiente línea

tiempo_final = time() 
tiempo_ejecucion = tiempo_final - tiempo_inicial

numeroconpuntos =  "{:,}".format(a).replace(',','.')   # formatea numero con puntos decimales.

print ('El tiempo de ejecucion de escribir : ', numeroconpuntos, 'registros fue:',tiempo_ejecucion) 	#En segundos
	
f.close()

# para grabar 100.000.000 de registros de 110 caracteres de longitud (10,4 GB -- 11.200.000.000 bytes) tarda 7,5 minutos.
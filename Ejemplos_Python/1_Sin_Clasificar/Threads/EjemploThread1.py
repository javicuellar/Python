from threading import Thread
from time import sleep

def espera(n):		# función que espera n segundos y luego muestra mensaje
 sleep(n)
 print ("Espero %s segundos." % n)


subproceso1 = Thread(target=espera, args=(1,))	# crea subproceso
subproceso2 = Thread(target=espera, args=(2,))	# crea subproceso

subproceso1.start()				# comienza el subproceso 1
subproceso2.start()				# comienza el subproceso 2


print ("Yo espero menos.")		# es lo primero que se ejecuta, con subproceso en marcha
subproceso1.join()				# detiene ejecución hasta fin del subproceso
# join sirve para sincronizar la ejecución y esperar a su finalización
# En caso contrario, simplemente tendremos 2 procesos ejecutándose a la vez
print ("Final proceso.")

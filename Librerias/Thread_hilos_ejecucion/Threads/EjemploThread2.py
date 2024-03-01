from threading import Thread
from time import sleep
from random import choice

def espera(n):
	sleep(n)

subproceso = Thread(target=espera, args=(5,))
subproceso.start()
# isAlive nos dice si el subproceso continúa ejecutándose o ya ha acabado

while(subproceso.isAlive()): 
	print ("Esperando...")
	sleep(1)

print ("He llegado.")

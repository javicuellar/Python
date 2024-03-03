import numpy as np


#  - Lectura fichero texto
puntos = np.genfromtxt(fname= 'bbva2inv.txt', delimiter=';')
print(puntos)
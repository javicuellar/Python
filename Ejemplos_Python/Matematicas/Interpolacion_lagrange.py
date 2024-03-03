# Interpolacion polinomica de Lagrange  (código base de Abraham Teran)

import numpy as np

puntos = np.genfromtxt(fname= 'bbva2inv.csv', delimiter=';')


def obtenerpuntos():
    results = []
    cantPoints = len(puntos)
    points = np.arange(cantPoints*2,dtype=float)
    lfun = np.arange((cantPoints)**2,dtype=float)
    points.shape = (2, cantPoints)
    lfun.shape = (cantPoints,cantPoints)\

    for i in range(cantPoints):
        points[0,i] = float(i + 1)
        points[1,i] = puntos[i]
	    
    print (points)
    unkoPoint = float(cantPoints + 1)
	
    for i in range(len(points[0])):
        for j in range(len(lfun)):
            if i == j:  lfun[i,j] = 1
            else:  lfun[i,j] = (unkoPoint-points[0,j])/(points[0,i]-points[0,j])\

    for i in range(len(points[1])):
        results.append(prod(lfun[i])*points[1,i])\

    res = sum(results)
    print ("Resultado: 'y' para x =",unkoPoint," :>",res)

def prod(A):
    a = 1
    for i in range(len(A)):
        a = a*A[i]
    return a

def main():
    cantPoints = int(input("Ingrese cantidad de puntos conocidos > "))

    if cantPoints < 2:
        print ("CANTIDAD DE PUNTOS CONOCIDOS >= 2")
        main()\

    results = []
    points = np.arange(cantPoints*2,dtype=float)
    lfun = np.arange((cantPoints)**2,dtype=float)
    points.shape = (2,cantPoints)
    lfun.shape = (cantPoints,cantPoints)\

    for i in range(cantPoints):
        print ("x",i,",y",i)
        x = float(input("Ingrese 'x' > "))
        y = float(input("Ingrese 'y' > "))
        points[0,i] = x
        points[1,i] = y\
	    
    print (points)
    unkoPoint = float(input("Ingrese 'x' de punto desconocido > "))\
	
    for i in range(len(points[0])):
        for j in range(len(lfun)):
            if i == j:  lfun[i,j] = 1
            else:  lfun[i,j] = (unkoPoint-points[0,j])/(points[0,i]-points[0,j])\

    for i in range(len(points[1])):
        results.append(prod(lfun[i])*points[1,i])\

    res = sum(results)
    print ("Resultado: 'y' para x =",unkoPoint," :>",res)

# main()
obtenerpuntos()
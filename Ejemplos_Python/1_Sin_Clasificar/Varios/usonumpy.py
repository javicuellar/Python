# -*- coding: utf-8 -*-

import numpy as np

#Creamos una matriz
a=np.array([0,1,2,3,4,5])

print ('Presenta la matriz')
print (a)
print ('Dimension de la matriz')
print (a.ndim)
#Vemos sus dimesion

print ('Forma de la matriz')
print (a.shape)
#Vemos su forma, el número de renglones y columnas

print ('Multiplica cada entrada por 2')
print (a*2)
#Multiplicamos cada entrada por 2

print ('Eleva a la potencia 2 cada entrada')
print (a**2)
#Elevamos a la segunda potencia cada entrada

print ('Cambiando la forma del la matriz')
print (a.reshape((3,2)))
print ('Se imprime cada uno de sus elementos')
print (a[0],a[1],a[2])
a[0]=5
print ('Se cambia la primera entrada a[0]=5')
print (a)

#Creamos una nueva matriz para de más dimensiones
b=np.array([[0,1,2],[3,4,5]])
print ('Se presenta b')
print (b)
print ('La forma de b')
print (b.shape)
print ('Se multiplica cada entrada por 3')
print (b*3)
print ('Se eleva cada entrada al cuadrado')
print (b**2)

#Se eliminan el vector y la matriz
del(a,b)


#Creacion de matrices especiales
a=np.zeros((3,4))
print ('Se presenta la matriz nula de 3X4')
print (a)

b=np.ones((2,2))
print ('Se presenta la matriz de unos')
print (b)

#Se creo la matriz con un valor igual para todas las entradas
c=np.full((3,3),3.5)
print ('Se presenta la matriz con valores iguales en todas las entradas')
print (c)


#Matriz identidad
d=np.eye(5)

print ('Se presenta la matriz identida de dimension 5')
print (d)


#Matriz con valores aleatorios
e=np.random.random((6,6))
print ('Se preseta la matri con valores aleatorios en cada entrada')
print (e)

#Eliminamos las matrices
del(a,b,c,d,e)

#Algunos detalles con los valores de las matrices y asignaciones
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print ('Se presenta la nueva matriz a')
print (a)
print ('Se presenta el valor de sus colnas')
print (a[:,2])

#Se presentan las dos primeras filas
print ('Se presentan las dos primeras filas')
print (a[:2,:])

#Creamos una nueva matriz con las primeras 4 entradas de a
b=a[:2,:2]
print ('Sub matriz de a')
print (b)
print ('modificamos el valor de b y modifica el de a')
b[0][0]=65
print (b)
print ('Modifica a')
print (a)

#esto tiene que ver con la asignación de memoria y de valores por python
del(a,b)

#Operaciones matematicas
a=np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=np.float64)
b=np.array([[1,0,1],[2,6,1],[1,1,1]], dtype=np.float64)

#Suma de matrices
print (a+b)
print (np.add(a,b))

#Resta de matrices
print (a-b)
print (np.subtract(a,b))

#Multiplicacion
print (a*b)
print (np.multiply(a,b))

#division
print (b/a)
print (np.divide(b,a))

#Raiz cuadrada
print (np.sqrt(a))

#Producto interno de vectores y de vectores con matrices
c=np.array([1,0,1])

print ('Produto interno por (1,0,1)')
print (a.dot(c))
print ('Producto punto de matrices')
print (a.dot(b))

print ('Valores de b')
print (b)
print ('eleccion de valores mayores a 1')
print (b[b>1])
print (b>1)

print ('Generamos otra matriz con un elemento NAN')
c=np.array([1,2,np.NAN,3,4])
print ('Presentamos su valor')
print (c)
print ('Identificamos los valores que son NAN')
print (np.isnan(c))
print ('Elegimos los valores que no son NAN')
print (c[~np.isnan(c)])

import numpy as np


#  Creamos una array
a = np.array([0,1,2,3,4,5])
print ("Array: ", a)
print ('Dimension de la matriz: ', a.ndim)
print ('Tamaño del array: ', a.shape)

print ('\nMultiplica cada entrada por 2.\n', a*2)
print ('\nEleva a la potencia 2 cada entrada\n', a**2)

print ('Redimensionamos la matriz a (3,2):\n', a.reshape((3,2)))

print ('\nSe imprime cada uno de sus elementos ', a[0],a[1],a[2])

#  Asignación de valores
a[0]= 5
print ('Se cambia la primera entrada a[0]=5, a[0]= ', a)

#  Creamos una nueva matriz para de más dimensiones
b = np.array([[0,1,2],[3,4,5]])
print ('Matriz b:\n', b)
print ('Tamaño de b\n ', b.shape)
print ('Se multiplica cada entrada por 3\n', b*3)
print ('Se eleva cada entrada al cuadrado\n', b**2)

#   Se eliminan el vector y la matriz
del(a,b)


#   Creacion de matrices especiales
a = np.zeros((3,4))
print ('Se presenta la matriz nula de 3X4\n', a)

b = np.ones((2,2))
print ('Se presenta la matriz de unos\n', b)

#   Se creo la matriz con un valor igual para todas las entradas
c = np.full((3,3),3.5)
print ('Se presenta la matriz con valores iguales en todas las entradas\n', c)

#   Matriz identidad
d = np.eye(5)
print("Matriz identidad dimension 5\n", d)

#   Matriz con valores aleatorios
e = np.random.random((6,6))
print ('Se preseta la matri con valores aleatorios en cada entrada\n', e)

#   Eliminamos las matrices
del(a,b,c,d,e)

#   Algunos detalles con los valores de las matrices y asignaciones
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print ('Se presenta la nueva matriz a\n', a)
print ('Se presenta el valor de sus columnas\n', a[:,2])
print ('Se presentan las dos primeras filas\n ', a[:2,:])

#   Creamos una nueva matriz con las primeras 4 entradas de a
b = a[:2,:2]
print ('Sub matriz de a\n', b)
b[0][0] = 65
print ('modificamos el valor de b (b[0][0] = 65) y modifica el de a', b)
print ('Modifica a, al ser b una sub matriz de a\n', a)

#   esto tiene que ver con la asignación de memoria y de valores por python
del(a,b)

#   Operaciones matematicas
a = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=np.float64)
b = np.array([[1,0,1],[2,6,1],[1,1,1]], dtype=np.float64)

#   Suma de matrices
print ("Matriz a + b\n", a + b)
print ("También se puede realizar con mp.add\n", np.add(a,b))

#   Resta de matrices
print ("Resta a - b\n", a - b)
print ("O también con np.subtract\n", np.subtract(a,b))

#   Multiplicacion
print ("Multiplicación a * b\n", a * b)
print ("Otra forma coon np.multiply\n", np.multiply(a,b))

#   division
print ("División b entre a\n", b / a)
print ("O con np.divide\n", np.divide(b,a))

#   Raiz cuadrada
print ("Raíz cuadrada de a\n", np.sqrt(a))


#   Producto interno de vectores y de vectores con matrices
c = np.array([1,0,1])

print ('Produto interno por (1,0,1)\n', a.dot(c))
print ('Producto punto de matrices, a x b, a.dot(b)', a.dot(b))

print ('Valores de b\n', b)

#   Selección valores
print ('Selección valores mayores a 1\n', b[b > 1])
print ("O también directamente b>1\n", b>1)


print ('Generamos otra matriz con un elemento NAN')
c = np.array([1, 2, np.NAN, 3, 4])
print ('Presentamos su valor\n', c)
print ('Identificamos los valores que son NAN\n', np.isnan(c))
print ('Elegimos los valores que no son NAN', c[~np.isnan(c)])
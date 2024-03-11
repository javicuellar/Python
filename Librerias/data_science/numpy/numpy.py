import numpy as np                      # Información www.numpy.org
import statistics as ss


# Array de una dimensión a partir de una lista de enteros
# Una dimensión se crea un "vector"
enteros = [1,3,5,7,9]
array = np.array(enteros)
print("Lista de enteros a array numpy -> ", array, "\n")

# Si tiene dos dimensiones se crea una "matriz"
enteros2D = [[1,3,5,7,9], [2,4,6,8,10]]
array2D = np.array(enteros2D)
print("Lista de enteros2D a array numpy -> ", array2D, "\n")

# np.empty  crea un array de las dimensión indicada ("vacío", tendrá lo que esté en memoria)
print("Array Empty (tiene lo que haya en memoria) -> ", np.empty(3), "\n")

# crea una array de n dimensiones, parámetro, con ceros.
arrayvacio4 = np.zeros(3)
print("Array Zeros(3) -> ", arrayvacio4, "\n")

# crea una array de n dimensiones (3), con unos
arrayUnos = np.ones(3)
print("Array ones(3) -> ", arrayUnos, "\n")

# np.full(n,m) crea una matriz (una "referencia" a la matriz) de n tamaño (dimensión si va en tupla)
# conteniendo el valor m.
print("np.full(4,2) -> ", np.full(4,2))
print("LLena matriz con 2 de 4 dimensiones np.full(4,2) -> \n", np.full(4,2), "\n")

# np.identity(n)  crea una matriz identidad
print("Matriz identidad (1 diagonal) np.identity(3) -> \n", np.identity(3), "\n") 
print("Crea y devuelve una referencia a un array de una dimensión cuyos elementos son la \n    \
secuencia desde inicio hasta fin tomando valores cada salto. np.arange(inicio, fin, salto)     \
np.arange(1, 100, 2) \n", np.arange(1,100,2), "\n")      # salto de 2 en 2, impares

# np.linspace(inicio, fin, n)    crea y devuleve referencia a un array de n elementos equidistantes
# entre el inicio y el fin.
print("np.linspace(1, 100, 10) \n", np.linspace(1, 100, 10))

# Números aleatorios
# crear lista aleatoria -> np.random.random(n)   array de 10 elementos (entre 0 y 1, tipo float)
print("np.random(10) \n", np.random.random(10))
#  podemos generar aleatorios cumpliendo una distribución:
#       - Poisson           -> poisson
#       - Normal            -> normal
#       - Binomial          -> binomial
#       - Chi Cuadrado      -> chisquare
#       - Hipergeométrica   -> hypergeometric

# crea una lista de valores aleatorios con la distribución normal
listaNormal = np.random.normal(50,1,100)     # distribución Normal con media 50, desv. tipica 1.
print("Lista 100 valores, distribución Normal \n", listaNormal)
print("La media de la lista Normal anterior es -> ", ss.mean(listaNormal))

#  Podemos poner una semailla, da igual el número, hace que si ejecuto otra vez salgan los mismos valores
np.random.seed(0)         # utiliza como semilla este valor, fija el resultado de random

#  Usamos randint(inicio, fin) para que genere numeros aleatorios entre el intervalo, inicio, fin
for i in range(1,4):        # con la semilla estableces las mismas condiciones iniciales
    print(np.random.randint(1,10))      # el resultado es que si ejejutamos varias veces


identidad = np.identity(3)   # podemos poner (3, int), sino por defecto toma float64
print("Matriz identidada \n", identidad)
print("identidad.ndim ", identidad.ndim)        # devuelve el rango, num. dimensiones
print("identidad.shape ", identidad.shape)      # devuelve tupla con num. elementos de cada dimensión
print("identidad.size ", identidad.size)        # devuelve el número de elementos del array
print("identidad.dtype ", identidad.dtype)      # devuelve el tipo de dato del array
print("\n")

# acdeso a los elementos..
identidad = np.identity(3,int)      # fila identidad (unos en la diagonal), de tipo entero
print("Matriz identidada(3, int) \n", identidad)
print("identidad.dtype ", identidad.dtype)
print("identidad[0,0] -> ", identidad[0,0])     # primer elemento de la primera fila, primera columna
print("identidad[0,1] -> ", identidad[0,1])       
print("identidad[1,0] -> ", identidad[1,0])    
print("identidad[1,1] -> ", identidad[1,1])    

# Podemos sacar los mínimos, máximos, media, etc.
print("Máximo matriz identidad: ", identidad.max())
print("Mínimo matriz identidad: ", identidad.min())

# Entre los corchetes puedo utilizar [:, 0:2] ->  todas las filas, columnas desde 0, 2 elementos
#                                             ->  para dos dimensiones, fila = 1 dimensión
#                                                                       oolumna = 2 dimensión
print("identidad[:, :2], todas 1 dimen, 2 dimen solo el primer elemento\n", identidad[:,:2])
print("\n")

#  También se pueden poner condiciones, coger los valores que sean 1, o mayores que 4
print("Cogemos los valores de identidad que sean 1 de identidad")
print(identidad[identidad==1])   
print("\n")

#  Multiplicar matrices con   matriz1.dot(matriz2)
print("Matriz identidad por sigo misma = \n", identidad.dot(identidad))
print("\n")

#  Calcular matriz transpuesta ->  matriz.T  
print("La matriz transpuesta de Identidad es: \n", identidad.T)
print("\n")

#   np.exp(matriz)  -->  crea matriz de dimensión de la de entrada elevando num. e a los 
#  valores que contiene la matriz de entrada.
print("Exp eleva el número e a el dato del array de entrada")
print("Array de entrada para exp -> \n", array2D)
print("Resultado de np.exp(array2D) -> \n", np.exp(array2D))

#  Tambien tenemos otras funciones como:
#   np.log(matriz)      -> Devuelve matriz con el logaritmo natural de cada elemento
#   np.sqrt(matriz)     -> Devuelve matriz con la raíz cuadarada de cada elemento

#   Generador de listas por iteradores
# ------------------------------------------------------------------------------------------------

# Genera una lista con los cuadrados de los números del 1-10
Lista = [i**2 for i in range(1,11)]

#   Construyendo listas con for in y if
# ------------------------------------------------------------------------------------------------
# pares menoes 50
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50)

# dobles diivisibles 3
doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]
print(doubles_by_3)

 # cuadrados de pares
even_squares = [x**2 for x in range(1,12) if x % 2 == 0]
print(even_squares)

#  devuelve C cuando los números del rango 0 al 4 sean menores que 3
c = ['C' for x in range(5) if x < 3]
print c      # devuelve ['C', 'C', 'C']

# cubos de num. entre 1 y 10 divisibles entre 4
cubes_by_four = [x**3 for x in range(1,11) if x**3 % 4 == 0]
print(cubes_by_four)
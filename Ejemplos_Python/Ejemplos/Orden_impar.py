#   Ordenar lista de impares: si la lista esta vacía, devuelve vacía. Los pares se quedan
# como están y los impares hay que ordenarlos.

# Ej.- 
#    (sort_array([5, 3, 2, 8, 1, 4])) #, [1, 3, 2, 8, 5, 4])
#    (sort_array([5, 3, 1, 8, 0]))    #, [1, 3, 5, 8, 0])
#    (sort_array([]))                 #,[])

# modo manual
def sort_array(s):
	li = [] 
	if s == []:
		return s
	for e in s:
		if e%2 != 0:
			li.append(e)
	li.sort()
	salida = []
	for e in s:
		if e%2 != 0:
			salida.append(li[0])
			del li[0]
		else:
			salida.append(e)
	return salida


# UTILIZANDO LOS RECURSOS PYTHON
def ordena_array(arr):
  impares = sorted((x for x in arr if x%2 != 0), reverse=True)
  print ('impares: ', impares)
  return [x if x%2==0 else impares.pop() for x in arr]

  
print(sort_array([5, 3, 2, 8, 1, 4])) 		#, [1, 3, 2, 8, 5, 4])
print(sort_array([5, 3, 1, 8, 0]))    		#, [1, 3, 5, 8, 0])
print(sort_array([]))                 		#,[])
print(ordena_array([5, 3, 2, 8, 1, 4]))
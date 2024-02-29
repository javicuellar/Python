def gimme(input_array):
	if input_array[0] == input_array[1]: # and input_array[1] == input_array[2]:
		return 1
	lista = [x  for x in input_array  if x <= max(input_array) and x > min(input_array)]
	return input_array.index(lista[0])
		
print (gimme([2, 2, 1]))  	# 0
print (gimme([5, 5, 5]))	# 1

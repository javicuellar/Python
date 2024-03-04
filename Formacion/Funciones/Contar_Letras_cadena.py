def freq_seq(s, sep):
	lista = ''
	for car in s:
		lista += str(s.count(car))
		lista += sep
	return lista[:len(lista)-1]
		
print (freq_seq('hello world', '-'))   # '1-1-3-3-2-1-1-2-1-3-1')
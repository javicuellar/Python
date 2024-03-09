""" Un programa sencillo, para calcular cuadrados de numeros """

def main():
	print ('Calculo de cuadros de numeros')
	n1 = int(input('Entre numero 1: '))
	n2 = int(input('Entre numero 2: '))
	
	for x in range(n1,n2):
		print (' -> depurando: x -> ', x, ' n1 -> ', n1, ' n2 -> ', n2)
		print ('cuadrado de ', x, ' = ', x ** x)
	
	print ('Hasta luego lucas.')

main()

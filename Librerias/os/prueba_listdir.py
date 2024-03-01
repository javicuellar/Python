import os

ruta = u'c:\\'

# PRUEBA CON OS.LISTDIR  (con error de acceso denegado)
def leer_dir_listdir(ruta):
	num_ar, salida = 0, ''
	for file in os.listdir(ruta):
		pathname = os.path.join(ruta, file)
		num_ar += 1
		print (num_ar, '> ', pathname)
		if num_ar == 2:
			salida = os.path.join(ruta, dir)
	return salida

# prueba sacar el directorio con OS.LISTDIR (con displays)
print ('-'*80)
ruta2 = leer_dir_listdir(ruta)

# prueba sacar directorio con ACCESO DENEGADO con OS.LISTDIR (con displays)  --->  ERROR
print ('\n')
print ('-'*80)
ruta2 = leer_dir_listdir(ruta2)
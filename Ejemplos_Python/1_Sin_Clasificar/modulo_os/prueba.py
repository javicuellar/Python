# -*- coding: utf-8 -*-

import os


def leer_dir_walk(ruta):
	salida = ''
	for (path,directorios,archivos) in os.walk(ruta, onerror=control_error):
		if path != ruta:
			print (path, ' -> salimos arriba')
			break
	
		num_ar, num_dir = 0, 0
		for ar in archivos:
			num_ar += 1
			print (num_ar, '> ', path, ' ---> ', ar)

		for dir in directorios:
			num_dir += 1
			print (num_dir, '> ', path, ' dir> ', dir)
			if num_dir == 2:
				salida = os.path.join(path, dir)

	return salida

	
#(n,e) = os.path.splitext(ar)


def control_error(err):
	er = err.strerror
	print ('Clase error: ', type(err))
	print ('Argumentos error: ', err)
	print ('winerror: ', err.winerror)
	print ('strerror: ', err.strerror)
	return er

	
ruta = u'c:\\'

# prueba sacar el directorio con OS.WALK (con displays)
print ('*'*70)
ruta2 = leer_dir_walk(ruta)

# prueba sacar directorio con ACCESO DENEGADO con OS.WALK (con displays)  (ERROR CONTROLADO)
print (ruta2, '\n', '*'*70)
ruta2 = leer_dir_walk(ruta2)



# PRUEBA CON FUNCION LEER_RUTA para exportar a nuestro proyecto
def leer_ruta(ruta):
	er = ''
	archivos, directorios = [], []
	for (path,directorios,archivos) in os.walk(ruta, onerror=control_error):
		break
	print ('  --> ', err.strerror)
	if er == '':
		for i in range(len(directorios)):
			directorios[i] = os.path.join(path, directorios[i])
	return archivos, directorios, er


# prueba obtener archivos, directorios y error con OS.WALK
print ('\n', '>'*70)
files, dirs, erro = leer_ruta(ruta)
	
num_ar, num_dir = 0, 0
for ar in files:
	num_ar += 1
	print (num_ar, '> ', ruta, ' ---> ', ar)

for dir in dirs:
	num_dir += 1
	print (num_dir, '>  dir> ', dir)

# prueba sacar directorio con ACCESO DENEGADO con OS.WALK (con displays)  (ERROR CONTROLADO)
print ('\n')
print ('>'*80)
files, dirs, erro = leer_ruta(ruta2)
print ('Error: ', erro)
	
num_ar, num_dir = 0, 0
for ar in files:
	num_ar += 1
	print (num_ar, '> ', ruta, ' ---> ', ar)

for dir in dirs:
	num_dir += 1
	print (num_dir, '>  dir> ', dir)



# PRUEBA CON OS.LISTDIR  (con error de acceso denegado)
'''
def leer_dir_listdir(ruta):
	num_ar, salida = 0, ''
	for file in os.listdir(ruta):
		pathname = os.path.join(ruta, file)
		num_ar += 1
		print (num_ar, '> ', pathname)
		if num_ar == 2:
			salida = os.path.join(path, dir)
	return salida
	
# prueba sacar el directorio con OS.LISTDIR (con displays)
print ('-'*80)
ruta2 = leer_dir_listdir(ruta)

# prueba sacar directorio con ACCESO DENEGADO con OS.LISTDIR (con displays)  --->  ERROR
print ('\n')
print ('-'*80)
ruta2 = leer_dir_listdir(ruta2)
'''
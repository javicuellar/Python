#    Módulo de gestión de ficheros, trata ficheros tipo excel, formato .csv. 
#		NO UTILIZA EL MODULO CSV
#
#    - AbrirFichero(fichero,modo).- toma dos parámetros, el fichero con todo su path y el modo de apertura.
#    - LeerFichero().- lee una línea del fichero y devuelve la lista (acción,fecha,valor).
#    - CerrarFichero().- cierra el fichero.
#
#	Funciones internas:
#    - FormatearRegistro(cadena).- Devuelve una lista con los campos contenidos en la cadena separ�ndolos por
#			el carácter ";". También realiza la eliminación de caracteres no válidos.




#  Función AbrirFichero, recibe el nombre del fichero con todo el path completo y el modo de apertura.
def AbrirFichero(fichero,modo):
	return open(fichero,modo)

	
#  Función LeerFichero, no tiene parámetros de entrada, devuelve una lista con los valores: acción, fecha y valor.
#		Realiza la lectura de una línea del fichero y la formatea usando la función FormatearRegistro para 
#		eliminar caracteres no válidos y separar campos.
def LeerFichero(fichero):
	return FormatearRegistro(fichero.readline())

	
#  Función FormatearRegistro, recibe un string del que elimina el carácter de fin de línea "\n" y divide el string
#		en los campos que contenga separados por ";" (ficheros de tipo .csv).
def FormatearRegistro(cadena):
	cadena = cadena.replace('\n', '')
	cadena = cadena.replace(',', '.')
	return cadena.split(';')


#  Función CerrarFichero, realiza la operación de cerrar el fichero.
def CerrarFichero(fichero):
	fichero.close()

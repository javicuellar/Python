#  M�dulo de gesti�n de ficheros, trata ficheros tipo excel, formato .csv. 
#		NO UTILIZA EL M�DULO CSV
#
#    - AbrirFichero(fichero,modo).- toma dos par�metros, el fichero con todo su path y el modo de apertura.
#    - LeerFichero().- lee una l�nea del fichero y devuelve la lista (acci�n,fecha,valor).
#    - CerrarFichero().- cierra el fichero.
#
#	Funciones internas:
#    - FormatearRegistro(cadena).- Devuelve una lista con los campos contenidos en la cadena separ�ndolos por
#			el car�cter ";". Tambi�n realiza la eliminaci�n de caracteres no v�lidos.





#  Funci�n AbrirFichero, recibe el nombre del fichero con todo el path completo y el modo de apertura.
def AbrirFichero(fichero,modo):
	return open(fichero,modo)

	
#  Funci�n LeerFichero, no tiene par�metros de entrada, devuelve una lista con los valores: acci�n, fecha y valor.
#		Realiza la lectura de una l�nea del fichero y la formatea usando la funci�n FormatearRegistro para 
#		eliminar caracteres no v�lidos y separar campos.
def LeerFichero(fichero):
	return FormatearRegistro(fichero.readline())

	
#  Funci�n FormatearRegistro, recibe un string del que elimina el car�cter de fin de l�nea "\n" y divide el string
#		en los campos que contenga separados por ";" (ficheros de tipo .csv).
def FormatearRegistro(cadena):
	cadena = cadena.replace('\n', '')
	cadena = cadena.replace(',', '.')
	return cadena.split(';')


#  Funci�n CerrarFichero, realiza la operaci�n de cerrar el fichero.
def CerrarFichero(fichero):
	fichero.close()

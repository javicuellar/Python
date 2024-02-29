#  M�dulo que contiene las funcionalidades del proyecto Mercado
#
#    - GrabarDatosFichero(fichero).- Abre el fichero, formato csv, y lo graba en la tabla Mercado (SQLite)
#    - RecuperarValor(accion).- Devuelve una lista de tuplas(fecha, valor) de los registros accion de la tabla Mercado.
#    - RecuperarValores().- Devuelve un diccionario con clave la acci�n y valores una lista de tuplas(fecha, valor).
#	 - Cerrar().- Cierra BD SQLite, tabla Mercado



import Mercado.fichero as f
#  Este m�dulo agrupa las funciones que se realizan con ficheros, ficheros excel .csv. NO utiliza m�dulo csv
#
#    - AbrirFichero(fichero,modo).- toma dos par�metros, el fichero con todo su path y el modo de apertura.
#    - LeerFichero().- lee una l�nea del fichero y devuelve la lista (acci�n,fecha,valor).
#    - CerrarFichero().- cierra el fichero.


import Mercado.tabla as t
#  Este m�dulo agrupa las funciones que se realizan con tablas, BD SQLite.
#
#    - InsertaRegistro(lista).- inserta en la tabla Mercado la lista (acci�n, fecha, valor).
#    - LeerAccion(accion).- devuelve tupla (fecha,valor) de los registros de la tabla Mercado de la acci�n 
#    - CerrarTabla().- cierra la BD SQLite


import Mercado.analisis as a
#  Este m�dulo agrupa las funciones de an�lisis de datos de los valores
#
#    - AnalizarValores(valores).- Realiza un an�lisis de la cartera enviada como par�metro (tipo diccionario)


import Tiempos.medirtiempos as tiempo
#  Usamos el m�dulo medirtiempos para conocer el rendimiento de los accesos a ficheros y tablas (y an�lisis)
#
#    - Inicio().- Recupera la hora de inicio
#    - Duraci�n(inicio).- Devuelve el tiempo transcurrido en segundos desde el par�metro inicio hasta la hora actual.




#  Funci�n GrabarDatosFichero(fichero).- toma como par�metro un string con el nombre del fichero con
#			la informaci�n acci�n, fecha, valor y lo carga en BD, tabla Mercado.
def GrabarDatosFichero(fichero):
	lectura = 'r'
	fichero = f.AbrirFichero(fichero,lectura)
	leido = f.LeerFichero(fichero)		# El primer registro contiene las cabeceras, pasamos de el

	contador = 0
	horainicio = tiempo.Hora()			# tomamos la hora para contabilizar el tiempo que tarda en grabar los registros
	leidoant = leido
	while leido[0] != '':
		leido = f.LeerFichero(fichero)	# lectura de valores desde fichero [acci�n, fecha, valor]
		if leido[0] != '':
			contador += 1
			leido[1] = tiempo.FormatearFecha(leido[1])
			if (contador % 100) == 0:
				print ('Llevamos ', str (contador), 'registros.')
			if leido[1] != leidoant[1]:		# no grabamos registro si est� duplicado por fecha
				t.InsertaRegistro(leido)	# graba en BD SQLite en tabla Mercado [acci�n, fecha, valor]
				leidoant = leido

	tarda = tiempo.Duracion(horainicio)
	tardaregistro = '%.2f' % (tarda/contador)
	tarda = '%.2f' % tarda
	print ('Hemos tardado: ' + str(tarda) + ' segundos para ' + str(contador) + ' registros. Tarda ' + str(tardaregistro) + ' en grabar un regitro.')
	f.CerrarFichero(fichero)


	
#  Funci�n RecuperarValor(accion).- toma como par�metro un string con el nombre de la acci�n 
#			a recuperar de la BD. Devuelve una lista de tuplas(fecha, valor).
def RecuperarValor(accion):
	return t.LeerAccion(accion)


	
#  Funci�n RecuperarValores().- Accede a la tabla Mercado y devuelve un diccionario con clave la acci�n y 
#			como valores una lista de tuplas(fecha, valor).
def RecuperarValores():
	return t.LeerMercado()


	
#  Funci�n AnalizarValores(valores).- Realiza un an�lisis de la cartera enviada como par�metro (tipo diccionario)
def AnalizarValores(valores):
	a.Analisis(valores)



#  Funci�n CerrarTabla().- cierra la BD SQLite
def Cerrar():
	t.CerrarTabla()

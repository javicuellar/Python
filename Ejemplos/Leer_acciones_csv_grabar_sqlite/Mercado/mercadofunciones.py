#   Módulo que contiene las funcionalidades del proyecto Mercado
#    - GrabarDatosFichero(fichero).- Abre el fichero, formato csv, y lo graba en la tabla Mercado (SQLite)
#    - RecuperarValor(accion).- Devuelve una lista de tuplas(fecha, valor) de los registros accion de la tabla Mercado.
#    - RecuperarValores().- Devuelve un diccionario con clave la acción y valores una lista de tuplas(fecha, valor).
#	 - Cerrar().- Cierra BD SQLite, tabla Mercado



import Mercado.fichero as f
#  Este módulo agrupa las funciones que se realizan con ficheros, ficheros excel .csv. NO utiliza módulo csv
#
#    - AbrirFichero(fichero,modo).- toma dos parámetros, el fichero con todo su path y el modo de apertura.
#    - LeerFichero().- lee una lánea del fichero y devuelve la lista (accián,fecha,valor).
#    - CerrarFichero().- cierra el fichero.


import Mercado.tabla as t
#  Este mádulo agrupa las funciones que se realizan con tablas, BD SQLite.
#
#    - InsertaRegistro(lista).- inserta en la tabla Mercado la lista (accián, fecha, valor).
#    - LeerAccion(accion).- devuelve tupla (fecha,valor) de los registros de la tabla Mercado de la accián 
#    - CerrarTabla().- cierra la BD SQLite


import Mercado.analisis as a
#  Este mádulo agrupa las funciones de análisis de datos de los valores
#
#    - AnalizarValores(valores).- Realiza un análisis de la cartera enviada como parámetro (tipo diccionario)


import Tiempos.medirtiempos as tiempo
#  Usamos el módulo medirtiempos para conocer el rendimiento de los accesos a ficheros y tablas (y análisis)
#
#    - Inicio().- Recupera la hora de inicio
#    - Duración(inicio).- Devuelve el tiempo transcurrido en segundos desde el parámetro inicio hasta la hora actual.




#  Funcián GrabarDatosFichero(fichero).- toma como parámetro un string con el nombre del fichero con
#			la informacián acción, fecha, valor y lo carga en BD, tabla Mercado.
def GrabarDatosFichero(fichero):
	lectura = 'r'
	fichero = f.AbrirFichero(fichero,lectura)
	leido = f.LeerFichero(fichero)		# El primer registro contiene las cabeceras, pasamos de el

	contador = 0
	horainicio = tiempo.Hora()			# tomamos la hora para contabilizar el tiempo que tarda en grabar los registros
	leidoant = leido
	while leido[0] != '':
		leido = f.LeerFichero(fichero)	# lectura de valores desde fichero [accián, fecha, valor]
		if leido[0] != '':
			contador += 1
			leido[1] = tiempo.FormatearFecha(leido[1])
			if (contador % 100) == 0:
				print ('Llevamos ', str (contador), 'registros.')
			if leido[1] != leidoant[1]:		# no grabamos registro si está duplicado por fecha
				t.InsertaRegistro(leido)	# graba en BD SQLite en tabla Mercado [accián, fecha, valor]
				leidoant = leido

	tarda = tiempo.Duracion(horainicio)
	tardaregistro = '%.2f' % (tarda/contador)
	tarda = '%.2f' % tarda
	print ('Hemos tardado: ' + str(tarda) + ' segundos para ' + str(contador) + ' registros. Tarda ' + str(tardaregistro) + ' en grabar un regitro.')
	f.CerrarFichero(fichero)


	
#  Funcián RecuperarValor(accion).- toma como parámetro un string con el nombre de la accián 
#			a recuperar de la BD. Devuelve una lista de tuplas(fecha, valor).
def RecuperarValor(accion):
	return t.LeerAccion(accion)


	
#  Funcián RecuperarValores().- Accede a la tabla Mercado y devuelve un diccionario con clave la accián y 
#			como valores una lista de tuplas(fecha, valor).
def RecuperarValores():
	return t.LeerMercado()


	
#  Funcián AnalizarValores(valores).- Realiza un análisis de la cartera enviada como parámetro (tipo diccionario)
def AnalizarValores(valores):
	a.Analisis(valores)



#  Funcián CerrarTabla().- cierra la BD SQLite
def Cerrar():
	t.CerrarTabla()
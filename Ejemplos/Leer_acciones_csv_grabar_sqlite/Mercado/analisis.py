#    Módulo para el análisis de datos de los valores de las acciones
#      - Media(lista).- Calcula la media de los valores de la lista


import Tiempos.medirtiempos as tiempo
#  Usamos el módulo medirtiempos para conocer el rendimiento de los accesos a ficheros y tablas (y análisis)
#
#    - Inicio().- Recupera la hora de inicio
#    - Duración(inicio).- Devuelve el tiempo transcurrido en segundos desde el parámetro inicio hasta la hora actual.
#    - DisplayFecha(fecha).- Convierte un string AAAA/MM/DD a string DD/MM/AAAA
#    - EnlamismaSemana(fecha1,fecha2).- Devuelve True si las dos fechas est�n en la misma semana



#  Función Analisis(valores).- Muestra un análisis de todas las acciones del diccionario
def Analisis(valores):
	for accion in valores.keys():
		# Cabeceras por accóon de la cartera 
		print ('\n','\n','*********************')
		print ("Analisis de: ", accion,'\n')
		
		val,fecha1,mediaant = [], '', 0
		for fecha,valor in valores[accion]:
			#print (fecha, '%.3f' % valor)
			if fecha1 == '':
				fecha1 = fecha
				val.append(valor)
			else:
				if tiempo.EnlamismaSemana(fecha1,fecha):
					val.append(valor)
				else:
					if mediaant == 0:
						porc = 0
					else:
						porc = (Media(val) - mediaant)*100/mediaant
					print (' -> ', tiempo.DisplayFecha(fecha1),'  Max: ', '%.3f' % max(val), '  Min: ', '%.3f' % min(val), '  Media: ', '%.3f' % Media(val), '%.2f%%' % porc)
					mediaant = Media(val)
					fecha1 = fecha
					val =[]
					val.append(valor)
		if mediaant == 0:
			porc = 0
		else:
			porc = (Media(val) - mediaant)*100/mediaant
		print (' -> ', tiempo.DisplayFecha(fecha1),'  Max: ', '%.3f' % max(val), '  Min: ', '%.3f' % min(val), '  Media: ', '%.3f' % Media(val), '%.2f%%' % porc)



#  Función Media(lista).- Calcula la media de los valores de la lista
def Media(lista):
	return sum(lista)/len(lista)

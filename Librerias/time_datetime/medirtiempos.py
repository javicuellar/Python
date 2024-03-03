#  Módulo de gestión del tiempo de ejecución, sirve principalmente para medir el rendimiento
#		Utiliza el módulo time para recuperar la hora
from time import time	   

#    - Hora().- Recupera la hora actual
#    - Duración(inicio).- Calcula el tiempo transcurrido, en segundos, desde "inicio" hasta la hora actual


# from datetime import datetime, date, time, timedelta
from datetime import datetime

#    - Fecha(fecha).- Convierte un string DD/MM/AAAA a fecha en formato datetime
#    - FormatearFecha(fecha).- Convierte un string DD/MM/AAAA a string AAAA/MM/DD
#    - DisplayFecha(fecha).- Convierte un string AAAA/MM/DD a string DD/MM/AAAA
#    - EnlamismaSemana(fecha1,fecha2).- Devuelve True si las dos fechas están en la misma semana

# import calendar



# Asigna formatofecha de fecha DD/MM/AAAA
formatofecha = "%d/%m/%Y"
formatoaaaammdd = "%Y/%m/%d"
formatonumsemana = "%W"


#  Función Hora().- Devuelve la hora actual utilizando el módulo time.
def Hora():
	return time() 		


#  Función Duracion(inicio).- Devuelve los segundos transcurridos desde el parámetro de entrada inicio hasta la hora actual
def Duracion(inicio):
	tiempo_final = time()
	return tiempo_final - inicio



#  Función Fecha(fecha).- Convierte un string DD/MM/AAAA a fecha en formato datetime
def Fecha(fecha):
	return datetime.strptime(fecha, formatoaaaammdd)

	

#  Función FormatearFecha(fecha).- Convierte un string DD/MM/AAAA a string AAAA/MM/DD
def FormatearFecha(fecha):
	return datetime.strptime(fecha, formatofecha).strftime(formatoaaaammdd)


	
#  Función DisplayFecha(fecha).- Convierte un string AAAA/MM/DD a string DD/MM/AAAA
def DisplayFecha(fecha):
	return datetime.strptime(fecha, formatoaaaammdd).strftime(formatofecha)



#  Función EnlamismaSemana(fecha1,fecha2).- Devuelve True si las dos fechas est�n en la misma semana
def EnlamismaSemana(fecha1,fecha2):
	fecha_date1, fecha_date2 = Fecha(fecha1), Fecha(fecha2)
	if fecha_date1.strftime(formatonumsemana) == fecha_date2.strftime(formatonumsemana):
		return True
	else:
		return False

print("Fecha: ", fecha, datetime.isocalendar(fecha_datetime))

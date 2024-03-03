#    Módulo de gestión de tablas de BD SQLite
#  -------------------------------------------

import sqlite3


con = sqlite3.connect('mercado_valores.db')

#    - InsertaRegistro(lista).- toma una entrada una lista (acción, fecha, valor) y la inserta en la tabla Mercado.
#    - LeerAccion(accion).- devuelve tupla (fecha,valor) de los registros de la tabla Mercado con el campo acción 
#			igual al parámetro de entrada.
#    - CerrarTabla().- cierra la BD SQLite



#  Función InsertaRegistro(lista).- toma una entrada una lista (acción, fecha, valor) y la inserta en la tabla Mercado.
def InsertaRegistro(lista):
	query = 'INSERT INTO Mercado (accion,fecha,apertura,maximo,minimo,valor,volumen) VALUES (?,?,?,?,?,?,?)'
	con.execute(query, lista)
	con.commit()


#  Función LeerAccion(accion).- lee de la tabla Mercado los registros con el campo acción igual al parámetro de entrada.
#		Devuelve tupla (fecha,valor)
def LeerAccion(accion):
	salida =[]
	a = "'" + accion + "'"
	query = 'SELECT fecha,valor FROM Mercado WHERE accion = ' + a
	for i in con.execute(query):
		salida.append(i)
	return salida


#  Función LeerMercado().- Devuelve todos los registros de la tabla Mercado, en formato diccionario.
#		Devuelve diccionario {clave = acción ; valores = lista [lista(fecha,valor)]
def LeerMercado():
	salida ={}
	query = 'SELECT accion,fecha,valor FROM Mercado where fecha > "2017/05/00" order by fecha'
	for registro in con.execute(query):
		i = [registro[1], registro[2]]
		if registro[0] in salida:
			salida[registro[0]].append(i)
		else:
			salida[registro[0]] = []
			salida[registro[0]].append(i)
	return salida


	
#  Función CerrarTabla().- Cierra la BD SQLite
def CerrarTabla():
	con.close()

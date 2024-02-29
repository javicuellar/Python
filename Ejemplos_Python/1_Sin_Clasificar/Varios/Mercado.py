#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  M�dulo de lectura y archivado de informaci�n de valores para su an�lisis


import Mercado.mercadofunciones as m
#  Las funciones de este m�dulo se han agrupado en Mercado.mercadofunciones
#
#    - GrabarDatosFichero(fichero).- toma como par�metro un string con el nombre del fichero con
#			la informaci�n acci�n, fecha, valor y lo carga en BD, tabla Mercado.
#
#    - RecuperarValor(accion).- toma como par�metro un string con el nombre de la acci�n 
#			a recuperar de la BD. Devuelve una lista de tuplas(fecha, valor).
#
#    - RecuperarValores().- Accede a la tabla Mercado y devuelve un diccionario con clave la acci�n y 
#			como valores una lista de tuplas(fecha, valor).
#
#    - Cerrar().- Cierra la BD SQLite con la tabla Mercados


#  El alta de registros (acci�n, fecha, valor) inicialmente se har� por fichero csv (posteriormente leyendo de webs)
# --------------------------------------------------------------------------------
# fichero = 'd:\\python\\Mercado\\mercado.csv'
# m.GrabarDatosFichero(fichero)



#  Probando a recuperar las fechas y valores de la acci�n BBVA
# --------------------------------------------------------------------------------
# accion = 'BBVA'
# valores = m.RecuperarValor(accion)
# print (valores, '\n', '\n')



#  Recuperar todas las accciones (fechas, valores) en un diccionario
#  An�lisis de los valores de la tabla Mercado
m.AnalizarValores(m.RecuperarValores())



#  Cerrando la BD SQLite
m.Cerrar()

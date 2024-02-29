#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Módulo de lectura y archivado de información de valores para su análisis


import Mercado.mercadofunciones as m
#  Las funciones de este módulo se han agrupado en Mercado.mercadofunciones
#
#    - GrabarDatosFichero(fichero).- toma como parámetro un string con el nombre del fichero con
#			la información acción, fecha, valor y lo carga en BD, tabla Mercado.
#
#    - RecuperarValor(accion).- toma como parámetro un string con el nombre de la acción 
#			a recuperar de la BD. Devuelve una lista de tuplas(fecha, valor).
#
#    - RecuperarValores().- Accede a la tabla Mercado y devuelve un diccionario con clave la acción y 
#			como valores una lista de tuplas(fecha, valor).
#
#    - Cerrar().- Cierra la BD SQLite con la tabla Mercados


#  El alta de registros (acción, fecha, valor) inicialmente se hará por fichero csv (posteriormente leyendo de webs)
# --------------------------------------------------------------------------------
# fichero = 'd:\\python\\Mercado\\mercado.csv'
# m.GrabarDatosFichero(fichero)



#  Probando a recuperar las fechas y valores de la acción BBVA
# --------------------------------------------------------------------------------
# accion = 'BBVA'
# valores = m.RecuperarValor(accion)
# print (valores, '\n', '\n')



#  Recuperar todas las accciones (fechas, valores) en un diccionario
#  Análisis de los valores de la tabla Mercado
m.AnalizarValores(m.RecuperarValores())



#  Cerrando la BD SQLite
m.Cerrar()

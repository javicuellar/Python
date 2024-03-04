# -*- coding: utf-8 -*-
import csv

# Mostrar lista de diccionarios a partir CSV y 
# consultar número de líneas (registros), dialecto y campos:

filecsv = u'.\Espacio\Tmp\Informe.csv'


csvarchivo = open(filecsv)
entrada = csv.DictReader(csvarchivo)
listadicc = list(entrada)  # Obtener lista de diccionarios
# print('Lista:', listadicc[0])  # Mostrar lista de diccionarios

print('LÃ­neas:', entrada.line_num)  # Obtener nÃºmero de registros
print('Dialecto:', entrada.dialect)  # Obtener dialecto
print('Campos:', entrada.fieldnames)  # Obtener nombre de campos

del entrada, listadicc
csvarchivo.close()
del csvarchivo
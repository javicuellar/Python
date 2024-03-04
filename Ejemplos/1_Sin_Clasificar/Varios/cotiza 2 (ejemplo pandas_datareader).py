# importando pandas y datetime
import pandas as pd
import pandas_datareader.data as web
import datetime as dt

# Extrayendo información financiera de Yahoo! Finnance
inicio = dt.datetime(2016, 1, 1)
fin = dt.datetime(2017, 8, 3)

bbva = web.DataReader("BBVA.MC", 'yahoo', inicio, fin) 
san = web.DataReader("SAN.mc", 'yahoo', inicio, fin) 

# print (bbva.head())

# tambien se puede seleccionar un rango de tiempo
print(bbva['2017-08':'2017-08-03'])    # desde el 1 al 3 de agosto
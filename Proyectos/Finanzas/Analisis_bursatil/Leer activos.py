import investpy as inv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data
from tqdm import tqdm       # librería para crear BARRA DE PROGRESO


#    Función que devuelve la lista de activos de un pais
#  Parámetros:
#   - productos:    'stocks', 'funds' or 'etfs'
#   - pais:         spain, United States
def ListaActivos(producto, pais):
    if producto == 'stocks':
        lista = inv.get_stocks_list(country=pais)
    elif producto == 'funds':
        lista = inv.get_funds_list(country=pais)
    elif producto == 'etfs':
        lista = inv.get_etfs_list(country=pais)
    return lista

#    Función que devuelve diccionario con todos los activos (simbolos) del producto y pais  
# con información en dataframe de históricos diarios con la informacion solicitada
#  Parámetros:
#   - productos: 'stocks', 'funds' or 'etfs'
#   - pais:  spain, United States
#   - fecInicio y fecFin:  fechas desde hasta de la información a obtener. Formato 'yyyy-mm-dd'
def ObtenerHist(fecInicio, fecFin, producto, pais):
    data_res = dict()
    error_list = list()
    data_list = ListaActivos(producto, pais)    # recuperamos la lista de activos
    for activo in tqdm(data_list):
        print(' Tratar: ', activo)
        df_hist = data.DataReader(activo + '.MC', "yahoo", fecInicio, fecFin)
        try:
            df_hist = data.DataReader(activo + '.MC', "yahoo", fecInicio, fecFin)
        except:
            error_list.append(activo)
        else:
            if df_hist.isnull().values.any() == False:
                data_res[activo] = df_hist
                print(' -> leido: ', activo)
    print("lista errores: ", error_list)
    return data_res


prod = 'stocks'
pais = 'spain'
pais = 'United States'
fDesde = "2024-01-01"
fHasta = "2024-09-26"

lista = ListaActivos(prod, pais)
print('Lista de activos: ', pais, '(', len(lista), '\n', lista)

print('\n------------------\n')
import yfinance as yf

#   Descargar el historial de Apple (AAPL) desde el 1 enero 2024 al 8 de marzo 2024
# aapl = yf.download('AAPL', start='2024-01-01', end='2024-03-09')
nvidia1 = yf.download(lista)
exit()

#  No funciona -> type error ??
dicActivos = ObtenerHist(fDesde, fHasta, prod, pais)
print(dicActivos['BBVA'])


#  Vamos a analizar dos activos:  BBVA y TSLA

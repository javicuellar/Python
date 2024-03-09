########  Recupera el histórico de valores de google/finance vía web(requests)  ########

#   Sacado de Ejemplos > Predicción_acciones_twiter

##  No funciona, no convierte bien la url leída en datos

import os
import sys
import requests
import numpy as np


# Aquí guardaremos el archivo en un csv
FILE_NAME = 'historical.csv'


def get_historical(quote):
    # Descarga el histórico de google finance
    url = 'http://www.google.com/finance/historical?q=BMV%3A'+quote+'&output=csv'
    r = requests.get(url, stream=True)

    if r.status_code != 400:
        with open(FILE_NAME, 'wb') as f:
            for chunk in r:
                f.write(chunk)
        return True


def extraer_datos():
    # Recolecta los datos del archivo csv
    dataset = []

    with open(FILE_NAME) as f:
        for n, line in enumerate(f):
            if n != 0:
                dataset.append(float(line.split(',')[1]))

    dataset = np.array(dataset)

    # Crea el dataset en forma matricial (X=t and Y=t+1)
    def create_dataset(dataset):
        dataX = [dataset[n+1] for n in range(len(dataset)-2)]
        return np.array(dataX), dataset[2:]

    print(create_dataset(dataset))

# Para predecir el rango de precios de cualquier acción registrada en la BMV:

# Preguntar al usuario la consulta de una acción a predecir
stock_quote = input('Ingrese el nombre de la acción en formato BMV que desea predecir (ej: CEMEXCPO, ELEKTRA, ALSEA): ').upper()

# Verifica si existe o no el histórico
if not get_historical(stock_quote):
    print('Google regresó un 404, por favor ejecute de nuevo el código')
    print('ingrese una acción válida en el formato BMV')
    sys.exit()

print(extraer_datos())

# Hemos terminado así que procedemos a borrar el archivo csv
# os.remove(FILE_NAME)
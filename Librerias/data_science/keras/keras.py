#   Sacado de Ejemplos > Predicción_acciones_twiter

#   Ejemplo incompleto, sólo la parte de creación del modelo, entrenamiento y predicciones

import os
import sys
import requests
import numpy as np

from keras.models import Sequential
from keras.layers import Dense


# Aquí guardaremos el archivo en un csv
FILE_NAME = 'historical.csv'

def Extraer_datos():
    # Recolecta los datos del archivo csv
    dataset = []

    with open(FILE_NAME) as f:
        for n, line in enumerate(f):
            if n != 0:
                dataset.append(float(line.split(',')[1]))

    return np.array(dataset)

dataset = Extraer_datos()

#  Datos de entrenamiento X e Y
    # Crea el dataset en forma matricial (X=t and Y=t+1)
def create_dataset(dataset):
    dataX = [dataset[n+1] for n in range(len(dataset)-2)]
    return np.array(dataX), dataset[2:]

     
trainX, trainY = create_dataset(dataset)

# Crea y entrena modelo Perceptron Multilineal 
model = Sequential()
model.add(Dense(8, input_dim=1, activation='relu'))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, nb_epoch=200, batch_size=2, verbose=2)

#  Nuestra prediction al día de mañana
prediction = model.predict(np.array([dataset[0]]))
print('El precio se moverá entre %s y %s' % (dataset[0], prediction[0][0]))


# Hemos terminado así que procedemos a borrar el archivo csv
os.remove(FILE_NAME)
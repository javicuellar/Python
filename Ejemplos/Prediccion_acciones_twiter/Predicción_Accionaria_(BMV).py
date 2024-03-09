########  Predicción de Acciones (Bolsa Mexicana de Valores)  ########

import os
import sys
import tweepy
import requests
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from textblob import TextBlob

# Entramos a Twitter vía API
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
user = tweepy.API(auth)

# Aquí guardaremos el archivo en un csv
FILE_NAME = 'historical.csv'

# Para ver lo que se opina del corporativo (Como ejemplo tomamos Cemex)

list_of_tweets = user.search('#cemex')

for tweet in list_of_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)


def stock_sentiment(quote, num_tweets):
    # Comprueba si el sentimiento de nuestra consulta es
    # positivo o negativo, regresa True si la
    # mayoría de tweets válidos tienen un sentimiento positivo
    list_of_tweets = user.search(quote, count=num_tweets)
    positive, null = 0, 0

    for tweet in list_of_tweets:
        blob = TextBlob(tweet.text).sentiment
        if blob.subjectivity == 0:
            null += 1
            next
        if blob.polarity > 0:
            positive += 1

    if positive > ((num_tweets - null)/2):
        return True


# Probamos para Cemex
stock_sentiment('cemex', 50)

def get_historical(quote):
    # Descarga el histórico de google finance
    url = 'http://www.google.com/finance/historical?q=BMV%3A'+quote+'&output=csv'
    r = requests.get(url, stream=True)

    if r.status_code != 400:
        with open(FILE_NAME, 'wb') as f:
            for chunk in r:
                f.write(chunk)
        return True


def stock_prediction():
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
        
    trainX, trainY = create_dataset(dataset)

    # Crea y entrena modelo Perceptron Multilineal 
    model = Sequential()
    model.add(Dense(8, input_dim=1, activation='relu'))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(trainX, trainY, nb_epoch=200, batch_size=2, verbose=2)

    #  Nuestra prediction al día de mañana
    prediction = model.predict(np.array([dataset[0]]))
    result = 'El precio se moverá entre %s y %s' % (dataset[0], prediction[0][0])
    return result


# Para predecir el rango de precios de cualquier acción registrada en la BMV:

# Preguntar al usuario la consulta de una acción a predecir
stock_quote = input('Ingrese el nombre de la acción en formato BMV que desea predecir (ej: CEMEXCPO, ELEKTRA, ALSEA): ').upper()

# Comprueba si el sentimiento de la acción es positivo
if not stock_sentiment(stock_quote, num_tweets=100):
    print('La acción tiene sentimiento negativo, por favor ejecute de nuevo el código para otra acción')
    sys.exit()
# Verifica si existe o no el histórico
if not get_historical(stock_quote):
    print('Google regresó un 404, por favor ejecute de nuevo el código')
    print('ingrese una acción válida en el formato BMV')
    sys.exit()
# Tenemos el histórico así que creamos la red neuronal y obtenemos la predicción
print(stock_prediction())


# Hemos terminado así que procedemos a borrar el archivo csv
os.remove(FILE_NAME)
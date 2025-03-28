import requests
import json


# URL del API
url = 'https://api.themoviedb.org/3/genre/movie/list'
headers = {'Content-Type': 'application/json;charset=UTF-8'}
params =  {'api_key': 'f200bb1c1249524e90b2a2d490b0b158'}


# Realizar la solicitud POST
try:
    # response = requests.post(url, json=data)
    response = requests.get(url, headers=headers, params=params)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    exit(1)


print("Código de estado de la respuesta:", response.status_code)

# Verificar el estado de la respuesta
if response.status_code == 200:
    # print("Cabeceras de la respuesta:", response.headers)
    # print("Contenido de la respuesta:", response.text)
    # print("Contenido de la respuesta en JSON:", response.json())
    result = response.json()
    print("\nGeneros:")
    for genre in result['genres']:
        print(f"ID: {genre['id']} - Nombre: {genre['name']}")
else:
    print(f"Error: {response.status_code} - {response}")

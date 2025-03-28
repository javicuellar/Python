import requests
import json

# URL del API
url = 'http://127.0.0.1:5000/sum'

# Datos a enviar en la solicitud
data = {
        'num1': 5,
        'num2': 3
       }

# Realizar la solicitud POST
try:
    response = requests.post(url, json=data)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    exit(1)

# Verificar el estado de la respuesta
if response.status_code == 200:
    # Convertir la respuesta a JSON
    result = response.json()
    print(f"La suma de {data['num1']} y {data['num2']} es: {result['result']}")
else:
    print(f"Error: {response.status_code} - {response.json().get('error', 'Error desconocido')}")

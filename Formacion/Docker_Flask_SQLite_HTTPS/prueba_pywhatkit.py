#   Instalación librería ->  pip install pywhatkit

import pywhatkit
from datetime import datetime


movil = '+34690662411'
mensaje = "Mensaje desde Python usando la libreria Pywhatkit, conforme si te llego el mensaje"

prueba = 1

if prueba == 1:
    hora_actual = datetime.now()
    hora = hora_actual.hour
    minuto = hora_actual.minute
    if minuto > 56:
        minuto = 0
        hora += 1
    
    tiempo_espera = 21   # tiempo para abrir navegador y preparar mensaje whatsapp a enviar

    try:
        pywhatkit.sendwhatmsg(movil, "Hola Python", hora, minuto + 1, tiempo_espera)
        print("Mensaje enviado correctamente")
    except:
        print("Error al enviar el mensaje WhatsApp")


    try:
        pywhatkit.sendwhatmsg(movil, "Hola Python2", hora, minuto + 3, tiempo_espera)
        print("Mensaje enviado correctamente")
    except:
        print("Error al enviar el mensaje WhatsApp")

else:
    try:
        pywhatkit.sendwhatmsg_instantly(movil, mensaje)
        print("Enviado mensaje instantáneo WhatsApp")
    except:
        print("Error al enviar mensaje instantaneo WhatsApp")
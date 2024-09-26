from email import message
import os
import smtplib
# import imghdr
from email.message import EmailMessage
import time

import yfinance as yf
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr



EMAIL_ADRESS = "ralleuc@gmail.com"
EMAIL_PASSWORD = "fgor aihs oaiy ivvy"

msg=EmailMessage()


yf.pdr_override()
start=dt.datetime(2021,3,1)
now=dt.datetime.now()

stock = "TSLA"
TargetPrice = 243


msg["Subject"] = "ALERTA Bolsa - " + stock
msg["From"] = EMAIL_ADRESS
msg["To"] = 'javicu25@gmail.com'

alerted = False

while 1:

    df= pdr.get_data_yahoo(stock, start, now)
    currentClose=df["Adj Close"][-1]
    
    condition = currentClose > TargetPrice
    print('> Analizando ' + stock + '  Cierre: ' + str(currentClose) + '  Precio objetivo: ' + str(TargetPrice))

    if (condition and alerted == False):
            alerted=True

            message= stock +" Ha activado su alerta de precio de " + str(TargetPrice) +\
            "\n\nPrecio Actual: " + str(currentClose)
         
            msg.set_content(message)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)

            print("Completado, salimos del programa.")
            exit()

    
    else:
        print("no hay alertas")

        time.sleep(43200)
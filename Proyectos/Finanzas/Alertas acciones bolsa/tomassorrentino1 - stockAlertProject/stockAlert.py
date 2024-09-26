from email import message
import os
import smtplib
import imghdr
from email.message import EmailMessage
import time


import yfinance as yf
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr

EMAIL_ADRESS = "stockalert40@gmail.com"
EMAIL_PASSWORD = "tomas.12345"

msg=EmailMessage()


yf.pdr_override()
start=dt.datetime(2021,3,1)
now=dt.datetime.now()

stock="TSLA"
TargetPrice=600



msg["Subject"]= "Alerta en" + stock
msg["From"] = EMAIL_ADRESS
msg["To"] = 'sorrentinotomas1@gmail.com'

alerted=False

while 1:

    df= pdr.get_data_yahoo(stock, start, now)
    currentClose=df["Adj Close"][-1]
    
    condition=currentClose>TargetPrice

    if(condition and alerted==False):
            alerted=True

            message= stock +" Ha activado su alerta de precio de" +str(TargetPrice) +\
            "\nPrecio Actual: " +str(currentClose)

            
            msg.set_content(message)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)

            print("completed")

    
    else:
        print("no hay alertas")

        time.sleep(43200)
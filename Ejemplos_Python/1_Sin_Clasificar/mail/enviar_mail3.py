#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Enviar correo Gmail con Python    www.pythondiario.com
 
import smtplib
 
fromaddr = 'ralleuc@gmail.com'
toaddrs  = 'javicu25@gmail.com'
msg = 'Correo enviado utilizano Python + smtplib en www.pythondiario.com'
 
 
# Datos
username = 'ralleuc@gmail.com'
password = 'ccjavi50'
 
# Enviando el correo
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

import smtplib
from email.message import EmailMessage



email = EmailMessage()
email['from'] = 'origen@gmail.com'
email['to'] = 'destino@gmail.com'
email['subject'] = 'Correo automático con python'
email.set_content('Hola, este correo fue enviado con python')


with smtplib.SMTP(host='smtp.gmail.com', port=465) as smtp:
    smtp.login('micorreo@gmail.com', "password")
    smtp.send_message(email)
    print('Correo enviado')

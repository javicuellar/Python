import smtplib, ssl
from email.message import EmailMessage




def email_alert(user, password, asunto, mensaje, destinatario):
    msg = EmailMessage()
    msg['subject'] = asunto
    msg['to'] = destinatario
    msg.set_content(mensaje)

    context = ssl.create_default_context()
    port = 465
    server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
    server.login(user, password)
    server.send_message(msg)
    print('Mail enviado correctamente.')
    
    server.quit()



if __name__ == '__main__':
    pass
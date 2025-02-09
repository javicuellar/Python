import smtplib, ssl
from email.message import EmailMessage



def email_alerta(asunto, mensaje, destinatario, user, password):
    msg = EmailMessage()
    msg['subject'] = asunto
    msg['to'] = destinatario
    msg.set_content(mensaje)
    
    # msg['from'] = user
    
    # msg["Importance"] = "high"
    # msg['X-Priority'] = '0'
    # msg['priority'] = "high"

    # Create a secure SSL context
    context = ssl.create_default_context() 

    segura = True
    if segura:
        #  Start an SMTP connection that is secured from the beginning using SMTP_SSL()
        port = 465
        server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
        print('Enviado por SSL')
    else:
        #  Start an unsecured SMTP connection that can then be encrypted using .starttls()
        port = 587
        server = smtplib.SMTP("smtp.gmail.com", port)
        #  con starttls securizamos la conesión
        server.starttls(context=context)
        print('Enviado por starttls')
    
    server.login(user, password)
    server.send_message(msg)
    # server.sendmail(user, destinatario, msg.as_string())

    server.quit()




if __name__ == '__main__':
    import sys, os

    # Para Windows añadimos path a librerías python, para añadir librerías mías de Herramientas
    if os.name == 'nt':
        sys.path.append(os.path.join(os.path.dirname(__file__), '\\Python'))
        DIRECTORIO = 'D:\\'
    else:
        DIRECTORIO = '/video'


    from Herramientas.variables import Variables

    var = Variables()

    email_alerta("ALERTA - mail", "Mensaje de prueba desde python", "javicu25@gmail.com", var.usuario, var.password)

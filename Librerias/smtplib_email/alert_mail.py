import smtplib, ssl
from email.message import EmailMessage


def email_alert(asunto, mensaje, destinatario):
    msg = EmailMessage()
    msg['subject'] = asunto
    msg['to'] = destinatario
    msg.set_content(mensaje)
    
    # msg['from'] = user
    
    # msg["Importance"] = "high"
    # msg['X-Priority'] = '0'
    # msg['priority'] = "high"

    user = "ralleuc@gmail.com"
    password = "fgor aihs oaiy ivvy"

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
    activo = 'SSL'
    tipo_alerta = 'Bajada precio '    # Tipo de alerta
    alerta = tipo_alerta + activo

    # email_alert("IMPORTANTE - " + alerta, "Mensaje de prueba desde python", "javicu25@gmail.com")
    
    #  En el móvil no avisa, popup, si en el asunto va ALERTA en lugar de IMPORTANTE.
    email_alert("ALERTA - " + alerta, "Mensaje de prueba desde python", "javicu25@gmail.com")

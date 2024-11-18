import smtplib, ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os




#  Configuración y envío del mail 
def Conexion(user, password, mensaje):
    context = ssl.create_default_context()
    smtp = "smtp.gmail.com"
    port = 465
    
    try:
        # Configurar el servidor SMTP y enviar el correo
        with smtplib.SMTP_SSL(smtp, port, context=context) as server:
            server.login(user, password)
            server.send_message(mensaje)
            print('Mail enviado correctamente.')
    except Exception as e:
        print(f"Error al enviar mail: {e}")
    

#  Envío mail sencillo (sin adjuntos)
def Envio_mail(user, password, asunto, mensaje, destinatario):
    msg = EmailMessage()
    msg['subject'] = asunto
    msg['to'] = destinatario
    msg.set_content(mensaje)

    Conexion(user, password, msg)


#  Envío mail con fichero adjunto
def Envio_mail_adjunto(user, password, asunto, mensaje, destinatario, archivo_adjunto):
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = destinatario
    msg['Subject'] = asunto
    msg.attach(MIMEText(mensaje, 'plain'))

    # Adjuntar archivo
    with open(archivo_adjunto, 'rb') as adjunto:
        parte = MIMEBase('application', 'octet-stream')
        parte.set_payload(adjunto.read())
        encoders.encode_base64(parte)
        parte.add_header('Content-Disposition', f'attachment; filename={os.path.basename(archivo_adjunto)}')
        msg.attach(parte)

    Conexion(user, password, msg)




if __name__ == '__main__':
    pass
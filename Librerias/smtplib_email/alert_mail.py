import smtplib
from email.message import EmailMessage


def email_alert(asunto, mensaje, a):
    msg = EmailMessage()
    msg.set_content(mensaje)
    msg['subject'] = asunto
    msg['to'] = a

    user = "formacionjavi0@gmail.com"
    msg['from'] = user
    password = "Gformacion0"

    server = smtplib.SMTP("smtp.gmail,com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


if __name__ == '__main__':
    email_alert("Hola", "Mensaje Hola mundo", "javicu25@gmail.com")

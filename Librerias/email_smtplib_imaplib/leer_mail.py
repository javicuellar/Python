from Herramientas.variables import USUARIO_JAVI, PASSWORD_JAVI   # Recuperar variables de usuario y contraseña

import imaplib
import email 



# Conexión al servidor IMAP de Gmail 
mail = imaplib.IMAP4_SSL('imap.gmail.com') 

# Inicio de sesión 
mail.login(USUARIO_JAVI, PASSWORD_JAVI) 


# Leer las etiquetas del correo gmail
print('\nEtiquetas:')
for etiqueta in mail.list()[1]:
    print(etiqueta)


# Selección de la bandeja de entrada 
mail.select('inbox') 

# Búsqueda de correos electrónicos con "control" en el asunto 
#   se puede buscar todos los correos con 'ALL'
criterio = 'ALL'

#  En lugar de poner _, se puede poner result para controlar el resultado
result, data = mail.search(None, criterio)
print('Result: ', result)                   # Devuelve 'OK' si todo está bien

#  Para entender la información que devuelve data (no es necesario)
ids = data[0]                   # IDS es una cadena separada por espacios
id_list = ids.split()           # Recupera el ID de cada mensaje
latest_email_id = id_list[-1]   # Obtiene el ultimo ID, el último correo

#  Ultimo correo recibido
_, data = mail.fetch(latest_email_id, '(RFC822)')
    
# Obtiene el cuerpo del correo electrónico 
msg = email.message_from_bytes(data[0][1]) 
# Parsea el mensaje 
print('Asunto:', msg['subject']) 
print('Remitente:', msg['from']) 
    
print('Mensaje:')
for part in msg.walk():
    if part.get_content_type() == 'text/plain':
        print(part.get_payload())



#   buscar en el asunto (SUBJECT) con los correos que contengan una palabra
criterio = '(SUBJECT "ALERTA")'
_, data = mail.search(None, criterio) 

contador = 0
# Itera sobre los IDs de los correos electrónicos encontrados 
for num in data[0].split(): 
    contador += 1
    _, data = mail.fetch(num, '(RFC822)')
    
    # Obtiene el cuerpo del correo electrónico 
    msg = email.message_from_bytes(data[0][1]) 
    # Parsea el mensaje 
    print('Asunto:', msg['subject']) 
    print('Remitente:', msg['from']) 
    
    print('Mensaje:')
    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            print(part.get_payload())


print(f"Se han encontrado {contador} correos con el asunto '{criterio}'")

# Cierra la conexión 
mail.close()
mail.logout()
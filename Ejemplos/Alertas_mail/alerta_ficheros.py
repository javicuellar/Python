import os
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Recuperación variables de configuración
from Herramientas.variables import USUARIO, PASSWORD, DESTINATARIO



# Configuración del directorio y parámetros de correo
DIRECTORIO = '\\NAS\video'
TAMANO_MINIMO = 5 * 1024 * 1024 * 1024      # 5 GB en bytes
EMAIL_REMITE = USUARIO
EMAIL_DESTINO = DESTINATARIO
PASSWORD = PASSWORD
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587



# Función para buscar archivos mayores a 5GB
def buscar_archivos_grandes(directorio):
    archivos_grandes = []
    for carpeta_raiz, _, archivos in os.walk(directorio):
        for archivo in archivos:
            ruta_archivo = os.path.join(carpeta_raiz, archivo)
            if os.path.getsize(ruta_archivo) > TAMANO_MINIMO:
                archivos_grandes.append((archivo, ruta_archivo, os.path.getsize(ruta_archivo)))
    return archivos_grandes

# Función para enviar correo electrónico
def enviar_correo(archivo_adjunto):
    mensaje = MIMEMultipart()
    mensaje['From'] = EMAIL_REMITE
    mensaje['To'] = EMAIL_DESTINO
    mensaje['Subject'] = 'Alerta: Archivos Grandes Encontrados'

    # Adjuntar archivo
    with open(archivo_adjunto, 'rb') as adjunto:
        parte = MIMEBase('application', 'octet-stream')
        parte.set_payload(adjunto.read())
        encoders.encode_base64(parte)
        parte.add_header('Content-Disposition', f'attachment; filename={os.path.basename(archivo_adjunto)}')
        mensaje.attach(parte)

    # Configurar el servidor SMTP y enviar el correo
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_REMITE, PASSWORD)
        server.send_message(mensaje)

# Función principal
def main():
    archivos_grandes = buscar_archivos_grandes(DIRECTORIO)
    if archivos_grandes:
        # Crear DataFrame y guardar en Excel
        df = pd.DataFrame(archivos_grandes, columns=['Nombre', 'Ruta', 'Tamaño (bytes)'])
        archivo_excel = 'archivos_grandes.xlsx'
        df.to_excel(archivo_excel, index=False)

        # Enviar correo
        enviar_correo(archivo_excel)
        print(f'Alerta enviada. Se encontraron {len(archivos_grandes)} archivos grandes.')
    else:
        print('No se encontraron archivos mayores de 5GB.')

# Ejecutar el script
if __name__ == "__main__":
    main()
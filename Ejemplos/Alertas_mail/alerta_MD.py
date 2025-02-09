import pandas as pd
from Herramientas.variables import USUARIO, PASSWORD, DESTINATARIO
from Herramientas.mail import Envio_mail


#  Recuperamos los puestos que hay en la web de Madrid Digital, si los hay.
# --------------------------------------------------------------------------
#       Url Madrid Digital
URL_MD = "https://www.comunidad.madrid/servicios/empleo/procesos-selectivos-agencia-administracion-digital"
#
#  Se recupera la tabla de puestos que hay en la web.


#  Recuperamos la tabla con los puestos
try:
    tablas = pd.read_html(URL_MD, header=0)   # Usar la primera fila como índice de las columnas
except Exception as e:
    print(f"Error al acceder a la web: {e}")


#  Comprobamos si hay puestos, y si los hay se envía alerta
try:
    puestos = tablas[0].iloc[:, :2]
    
    if puestos.iloc[0].nunique() == 1:    # Si no hay puestos, todos los valores son los mismos
        # print('No hay ningún puesto.')
        alerta = 'Puestos Madrid Digital - NO HAY NINGUNO'
        mensaje = f"{puestos.iloc[0,1]}\nVisita la pagina web\n{URL_MD}"
        Envio_mail(USUARIO, PASSWORD , alerta, mensaje, DESTINATARIO)
    else:
        alerta = 'ALERTA - Puestos Madrid Digital'
        mensaje = f"Han salido los siguientes puestos en Madrid Digital.\n\n{puestos.to_string(index=False)}\n\n Visita la pagina web\n{URL_MD}"
        Envio_mail(USUARIO, PASSWORD , alerta, mensaje, DESTINATARIO)
except Exception as e:
    print(f"Error al enviar mail: {e}")
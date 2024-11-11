import pandas as pd
from herramientas.variables import Variables
from herramientas.mail import email_alert




v = Variables() 

#  Recuperamos la tabla con los puestos
try:
    tablas = pd.read_html(v.url, header=0)   # Usar la primera fila como índice de las columnas
except Exception as e:
    print(f"Error al acceder a la web: {e}")


#  Comprobamos si hay puestos, y si los hay se envía alerta
try:
    puestos = tablas[0].iloc[:, :2]
    
    if puestos.iloc[0].nunique() == 1:    # Si no hay puestos, todos los valores son los mismos
        # print('No hay ningún puesto.')
        alerta = 'Puestos Madrid Digital - NO HAY NINGUNO'
        mensaje = f"{puestos.iloc[0,1]}\nVisita la pagina web\n{v.url}"
        email_alert(v.usuario, v.password , alerta, mensaje, v.destinatario)
    else:
        alerta = 'ALERTA - Puestos Madrid Digital'
        mensaje = f"Han salido los siguientes puestos en Madrid Digital.\n\n{puestos.to_string(index=False)}\n\n Visita la pagina web\n{v.url}"
        email_alert(v.usuario, v.password , alerta, mensaje, v.destinatario)
except Exception as e:
    print(f"Error al enviar mail: {e}")
'''
TRABAJAR CON ZONAS HORARIAS

En general, trabajar con zonas horarias puede ser complicado. Los usuarios de su aplicación Streamlit no están necesariamente en la misma zona horaria que el servidor que ejecuta su aplicación. Es especialmente cierto en el caso de las aplicaciones públicas, donde cualquier persona en el mundo (en cualquier zona horaria) puede acceder a su aplicación. Como tal, es crucial comprender cómo Streamlit maneja las zonas horarias, para que pueda evitar comportamientos inesperados al mostrar información.datetime

Cómo maneja Streamlit las zonas horarias
Streamlit siempre muestra información en el frontend con la misma información que su instancia correspondiente en el backend. Es decir, la información de fecha u hora no se ajusta automáticamente a la zona horaria de los usuarios. Distinguimos entre los siguientes dos casos:datetimedatetime

datetime Instancia sin zona horaria (ingenua)
Cuando proporciona una instancia sin especificar una zona horaria, el frontend muestra la instancia sin información de zona horaria. Por ejemplo (esto también se aplica a otros widgets como st.dataframe):datetimedatetime

'''

import streamlit as st
from datetime import datetime

st.write(datetime(2020, 1, 10, 10, 30))
# Outputs: 2020-01-10 10:30:00

'''
datetime con una zona horaria
Cuando proporciona una instancia y especifica una zona horaria, el frontend muestra la instancia en esa misma zona horaria. Por ejemplo (esto también se aplica a otros widgets como st.dataframe):datetimedatetime
'''

import streamlit as st
from datetime import datetime
import pytz

st.write(datetime(2020, 1, 10, 10, 30, tzinfo=pytz.timezone("EST")))
# Outputs: 2020-01-10 10:30:00-05:00


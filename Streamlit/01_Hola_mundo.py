import streamlit as st


st.title('Hola Mundo')
st.write('¡Hola, mundo! Esta es una aplicación de Streamlit.')


if st.button('pulsar'): 
    st.write('Buenos días mundo!')


#### Mostrar la hora actual
import datetime 

if st.button('Current Time'):
    st.write(datetime.datetime.now())

import streamlit as st
import pandas as pd




if not st.session_state['logged_in']:
    st.warning("Debes iniciar sesión para ver esta página.")
    st.stop()




import locale

# Configurar la localización
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')




activos = st.session_state.activos

st.subheader('Cartera Activos')
st.dataframe(activos.style.set_table_attributes('style="width:100%;"'), hide_index=True)



#### PARA EJECUTAR EN OTRO PUERTO 
# streamlit run app.py --server.port 8510

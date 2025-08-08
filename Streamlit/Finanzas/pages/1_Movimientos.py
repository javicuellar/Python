import streamlit as st
import pandas as pd




if not st.session_state['logged_in']:
    st.warning("Debes iniciar sesión para ver esta página.")
    st.stop()



import locale

# Configurar la localización
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')




### Columnas
co1, co2 = st.columns([5,1])

with co1:
    st.subheader('Movimientos')


mvtos = st.session_state.mvtos

# Extraer años únicos del DataFrame
años = mvtos['Año'].astype(str).unique().tolist()
años = sorted(años, key=lambda x: int(x), reverse=True)  # Ordenar de mayor a menor
años.insert(0, 'Todos')

with co2:
    año_seleccionado = st.selectbox('Seleccione año:', años, index=1)

if año_seleccionado == 'Todos':
    df_mvtos = mvtos.copy()
else:
    df_mvtos = mvtos[mvtos['Año'] == int(año_seleccionado)].copy()


st.dataframe(df_mvtos.style.set_table_attributes('style="width:100%;"'), hide_index=True)


#### PARA EJECUTAR EN OTRO PUERTO 
# streamlit run app.py --server.port 8510

import streamlit as st
import pandas as pd

if st.session_state.get('logged_in'):
    st.title("Dashboard de Datos")
    st.write("Aquí puedes ver algunas visualizaciones y datos.")

    data = {
        'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
        'Ventas': [100, 150, 120, 180, 200],
        'Gastos': [50, 60, 55, 70, 75]
    }
    df = pd.DataFrame(data)

    st.dataframe(df)
    st.line_chart(df.set_index('Mes'))
else:
    st.warning("Debes iniciar sesión para ver esta página.")

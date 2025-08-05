import streamlit as st

if st.session_state.get('logged_in'):
    st.title("Acerca de Nosotros")
    st.write("Esta página contiene información sobre nuestra aplicación.")
    st.info("Desarrollado con Streamlit y mucho esfuerzo.")
else:
    st.warning("Debes iniciar sesión para ver esta página.")

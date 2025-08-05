import streamlit as st

if st.session_state.get('logged_in'):
    st.title("Página Principal (Home)")
    st.write("Este es el contenido de la página principal, visible solo si has iniciado sesión.")
    st.image("https://via.placeholder.com/600x200?text=Bienvenido+a+Home", caption="Imagen de bienvenida")
else:
    st.warning("Debes iniciar sesión para ver esta página.")

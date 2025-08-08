import streamlit as st
import json
import time

from Mvtos.mvtos import LeerMvtos, Analisis_mvtos




# --- Configuración de la Página ---
st.set_page_config(
    page_title="Finanzas",
    page_icon="👋",
    layout="centered"
)



# --- Archivo de Usuarios (para simplificar) ---
USERS_FILE = 'users.json'

def load_users():
    try:
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

# --- Crear un usuario de ejemplo si no existe ---
if not load_users():
    users = {"usuario1": "pass123"} # Usuario y contraseña de ejemplo
    save_users(users)

# --- Función de Login ---
def login():
    cols = st.columns(3)
    with cols[1]:
        st.subheader("Iniciar Sesión")
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")

        users = load_users()

        if st.button("Entrar"):
            if username in users and users[username] == password:
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.success(f"¡Bienvenido, {username}!")
                time.sleep(1) # Pequeña pausa para que el mensaje sea visible
                st.rerun() # Recargar la página para mostrar el contenido
            else:
                st.error("Usuario o contraseña incorrectos")

# --- Función de Logout ---
def logout():
    if st.session_state.get('logged_in'):
        if st.button("Cerrar Sesión"):
            st.session_state['logged_in'] = False
            st.session_state['username'] = None
            st.info("Sesión cerrada.")
            time.sleep(1)
            st.rerun()



# --- Lógica Principal de la App ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("Bienvenido a Finanzas Personales")
    st.write("Por favor, inicia sesión para acceder al contenido.")
    login()
else:
    st.sidebar.write(f"Conectado como: **{st.session_state['username']}**")
    st.write("# ¡Has iniciado sesión! 👋")
    st.write("Usa el menú de la izquierda para navegar entre las páginas.")
    logout()

    #  Recuperar los movimientos de la hoja de cálculo
    hoja = "Cartera (con valoraciones)"

    st.write(('Cargamos los movimientos de la hoja de cálculo:', hoja))
    mvtos = LeerMvtos(hoja)

    # Recuperar la cartera, las ventas y los intereses y dividendos de los mvtos
    activos, ventas, int_div, nomina = Analisis_mvtos(mvtos)
    st.session_state.mvtos = mvtos
    st.session_state.activos = activos
    st.session_state.ventas = ventas
    st.session_state.int_div = int_div
    st.session_state.nomina = nomina

    #  Grabar_analisis(activos, ventas, int_div, nomina)
    #  print('Cartera analizada y grabada en Google Sheets.')
    
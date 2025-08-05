import streamlit as st
import json
import time

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Mi App Streamlit",
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
    st.sidebar.title("Iniciar Sesión")
    username = st.sidebar.text_input("Usuario")
    password = st.sidebar.text_input("Contraseña", type="password")

    users = load_users()

    if st.sidebar.button("Entrar"):
        if username in users and users[username] == password:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.sidebar.success(f"¡Bienvenido, {username}!")
            time.sleep(1) # Pequeña pausa para que el mensaje sea visible
            st.rerun() # Recargar la página para mostrar el contenido
        else:
            st.sidebar.error("Usuario o contraseña incorrectos")

# --- Función de Logout ---
def logout():
    if st.session_state.get('logged_in'):
        if st.sidebar.button("Cerrar Sesión"):
            st.session_state['logged_in'] = False
            st.session_state['username'] = None
            st.sidebar.info("Sesión cerrada.")
            time.sleep(1)
            st.rerun()

# --- Lógica Principal de la App ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    login()
    st.title("Bienvenido a la App Segura")
    st.write("Por favor, inicia sesión para acceder al contenido.")
else:
    st.sidebar.write(f"Conectado como: **{st.session_state['username']}**")
    logout()
    st.write("# ¡Has iniciado sesión! 👋")
    st.write("Usa el menú de la izquierda para navegar entre las páginas.")

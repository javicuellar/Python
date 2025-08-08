'''
Páginas
A medida que las aplicaciones crecen, resulta útil organizarlas en varias páginas. Esto hace que la aplicación sea más fácil de administrar como desarrollador y más fácil de navegar como usuario. Streamlit proporciona una forma eficaz de crear aplicaciones de varias páginas mediante st. Página y st.navigation. Sólo tienes que crear tus páginas y conectarlas con la navegación de la siguiente manera:

Cree un script de punto de entrada que defina y conecte sus páginas
Crear archivos Python separados para el contenido de cada página
Utilice st. Page para definir tus páginas y st.navigation para conectarlas
Este es un ejemplo de una aplicación de tres páginas:
'''

'''
streamlit_app.py
'''
import streamlit as st

# Define the pages
main_page = st.Page("main_page.py", title="Main Page", icon="🎈")
page_2 = st.Page("page_2.py", title="Page 2", icon="❄️")
page_3 = st.Page("page_3.py", title="Page 3", icon="🎉")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3])

# Run the selected page
pg.run()

'''
main_page.py
'''
import streamlit as st

# Main page content
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

'''
page_2.py
'''
import streamlit as st

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

'''
page_3.py
'''
import streamlit as st

st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")

'''
¡Ahora ejecute y vea su nueva y brillante aplicación de varias páginas! El menú de navegación aparecerá automáticamente, lo que permitirá a los usuarios cambiar entre páginas.streamlit run streamlit_app.py
'''

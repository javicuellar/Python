import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

#  Para "marcar" los valores máximos de cada columna
st.dataframe(dataframe.style.highlight_max(axis=0)) 

st.write('---')

#  Mostrar como tabla, similar pero más condensado al dataframe
st.table(dataframe)

st.write('---')

#  Graficar con líneas
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.write('---')

#  Graficar con mapa geográfico
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

st.write('---')

#  Línea de selección de datos, widget
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

#  Se puede dar nombre añadiendo "key", automáticamente se guarda en Session data
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

'''
EJEMPLOS USO SESSION_STATE
'''
if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")


st.write('---')

#  Uso de checkbox para mostrar u ocultar datos
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


#  Uso de selectbox para elegir entre opciones
df = pd.DataFrame({
   'first column': [1, 2, 3, 4],
   'second column': [10, 20, 30, 40]
   })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

'''
BARRA LATERAL - PANEL IZQUIERDO

Streamlit facilita la organización de sus widgets en una barra lateral del panel izquierdo con st.sidebar. Cada elemento que se pasa a st.sidebar se fija a la izquierda, lo que permite usuarios para que se centren en el contenido de la aplicación sin dejar de tener acceso a la interfaz de usuario mandos.

Por ejemplo, si desea agregar un selectbox y un control deslizante a una barra lateral, use y en lugar de y :st.sidebar.sliderst.sidebar.selectboxst.sliderst.selectbox
'''
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

'''
Más allá de la barra lateral, Streamlit ofrece varias otras formas de controlar el diseño de tu app. st.columns te permite colocar widgets uno al lado del otro, y st.expander te permite ahorrar espacio ocultando contenido grande.
'''

left_column, right_column = st.columns(2)

# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
    
'''
MOSTRAR BARRA PROGRESO
Cuando agregas cálculos de larga duración a una app, puedes usar st.progress() para mostrar el estado en tiempo real.

Primero, importemos el tiempo. Vamos a usar el método para Simule un cálculo de larga duración:time.sleep()
'''
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

'''
ALMACENAMIENTO CACHE PARA FUNCIONES
El almacenamiento en caché le permite guardar la salida de una función para que pueda omitirla al volver a ejecutarla. El estado de sesión le permite guardar información para cada usuario que se conserva entre reejecuciones. Esto no solo le permite evitar recálculos innecesarios, sino que también le permite crear páginas dinámicas y manejar procesos progresivos.

Caché
El almacenamiento en caché permite que tu app siga funcionando incluso cuando cargas datos desde la web, manipulas grandes conjuntos de datos o realizas cálculos costosos.

La idea básica detrás del almacenamiento en caché es almacenar los resultados de costosas llamadas a funciones y devolver el resultado almacenado en caché cuando se vuelven a producir las mismas entradas. Esto evita la ejecución repetida de una función con los mismos valores de entrada.

Para almacenar en caché una función en Streamlit, debe aplicarle un decorador de almacenamiento en caché. Tienes dos opciones:

st.cache_data es la forma recomendada de almacenar en caché los cálculos que devuelven datos. Úselo cuando use una función que devuelva un objeto de datos serializable (por ejemplo, str, int, float, DataFrame, dict, list). Crea una nueva copia de los datos en cada llamada a la función, lo que la hace segura contra mutaciones y condiciones de carrera. El comportamiento de es lo que desea en la mayoría de los casos, así que si no está seguro, ¡comience y vea si funciona!st.cache_datast.cache_datast.cache_data
st.cache_resource es la forma recomendada de almacenar en caché recursos globales, como modelos de AA o conexiones de bases de datos. Úselo cuando la función devuelva objetos no serializables que no desea cargar varias veces. Devuelve el objeto almacenado en caché, que se comparte entre todas las reejecuciones y sesiones sin copiar ni duplicar. Si muta un objeto que se almacena en caché mediante , esa mutación existirá en todas las reejecuciones y sesiones.st.cache_resourcest.cache_resource
'''
@st.cache_data
def long_running_function(param1, param2):
    return param1 + param2






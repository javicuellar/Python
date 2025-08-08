'''
Lógica común con botones
Mostrar un mensaje temporal con un botón
Si desea darle al usuario un botón rápido para verificar si una entrada es válida, pero no mantener esa verificación mostrada a medida que el usuario continúa.

En este ejemplo, un usuario puede hacer clic en un botón para comprobar si su cadena está en la lista. Cuando el usuario haga clic en "Verificar disponibilidad", verá "¡Tenemos ese animal!" o "No tenemos ese animal". Si cambian el animal en st.text_input, el script se vuelve a ejecutar y el mensaje desaparece hasta que vuelven a hacer clic en "Verificar disponibilidad".animalanimal_shelter
'''
import streamlit as st

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

animal = st.text_input('Type an animal')

if st.button('Check availability'):
    have_it = animal.lower() in animal_shelter
    
    ### usa "magia", se imprime el texto sin poner st.write()
    'We have that animal!' if have_it else 'We don\'t have that animal.'


'''
Botón con estado
Si desea que un botón en el que se ha hecho clic siga siendo , cree un valor en y use el botón para establecer ese valor en una devolución de llamada.Truest.session_stateTrue
'''

import streamlit as st

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button('Click me', on_click=click_button)

if st.session_state.clicked:
    # The message and nested widget will remain on the page
    st.write('Button clicked!')
    st.slider('Select a value')
    
'''
Botón de alternancia  - enciende y apaga
Si desea que un botón funcione como un interruptor de palanca, considere usar st.checkbox. De lo contrario, puede usar un botón con una función de devolución de llamada para revertir un valor booleano guardado en .st.session_state

En este ejemplo, usamos para activar y desactivar otro widget. Al mostrar st.slider condicionalmente en un valor en , el usuario puede interactuar con el control deslizante sin que desaparezca.st.buttonst.session_state
'''
import streamlit as st

if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('Click me', on_click=click_button)

if st.session_state.button:
    # The message and nested widget will remain on the page
    st.write('Button is on!')
    st.slider('Select a value')
else:
    st.write('Button is off!')

'''
ALTERNATIVA
Como alternativa, puede utilizar el valor en el parámetro del control deslizante.st.session_statedisabled
'''
import streamlit as st

if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('Click me', on_click=click_button)

st.slider('Select a value', disabled=st.session_state.button)

'''
FASES - Botones para continuar o controlar etapas de un proceso

Otra alternativa a anidar contenido dentro de un botón es usar un valor que designe el "paso" o "etapa" de un proceso. En este ejemplo, tenemos cuatro etapas en nuestro script:st.session_state

0 Antes de que el usuario comience.
1 El usuario introduce su nombre.
2 El usuario elige un color.
3 El usuario recibe un mensaje de agradecimiento.

Un botón al principio avanza la etapa de 0 a 1. Un botón al final reinicia la etapa de 3 a 0. Los otros widgets utilizados en las etapas 1 y 2 tienen devoluciones de llamada para preparar el escenario. Si tiene un proceso con pasos dependientes y desea mantener visibles las etapas anteriores, dicha devolución de llamada obliga a un usuario a volver sobre las etapas posteriores si cambia un widget anterior.
'''
import streamlit as st

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if st.session_state.stage == 0:
    st.button('Begin', on_click=set_state, args=[1])

if st.session_state.stage >= 1:
    name = st.text_input('Name', on_change=set_state, args=[2])

if st.session_state.stage >= 2:
    st.write(f'Hello {name}!')
    color = st.selectbox(
        'Pick a Color',
        [None, 'red', 'orange', 'green', 'blue', 'violet'],
        on_change=set_state, args=[3]
    )
    if color is None:
        set_state(2)

if st.session_state.stage >= 3:
    st.write(f':{color}[Thank you!]')
    st.button('Start Over', on_click=set_state, args=[0])

'''
Un pequeño problema
En este ejemplo, accedemos tanto al antes como al después de los botones que lo modifican. Cuando se hace clic en un botón ("Jane" o "John"), el script se vuelve a ejecutar. La información que se muestra antes de los botones es inferior a la información escrita después del botón. Los datos anteriores al botón no se actualizan. Cuando el script ejecuta la función de botón, es cuando el código condicional para actualizar crea el cambio. Por lo tanto, este cambio se refleja después del botón.st.session_state.namest.session_statest.session_state
'''
import streamlit as st
import pandas as pd

if 'name' not in st.session_state:
    st.session_state['name'] = 'John Doe'

st.header(st.session_state['name'])

if st.button('Jane'):
    st.session_state['name'] = 'Jane Doe'

if st.button('John'):
    st.session_state['name'] = 'John Doe'

st.header(st.session_state['name'])

'''
Lógica utilizada en una devolución de llamada
Las devoluciones de llamada son una forma limpia de modificar . Las devoluciones de llamada se ejecutan como un prefijo para la reejecución del script, por lo que la posición del botón en relación con el acceso a los datos no es importante.st.session_state
'''
import streamlit as st
import pandas as pd

if 'name' not in st.session_state:
    st.session_state['name'] = 'John Doe'

def change_name(name):
    st.session_state['name'] = name

st.header(st.session_state['name'])

st.button('Jane', on_click=change_name, args=['Jane Doe'])
st.button('John', on_click=change_name, args=['John Doe'])

st.header(st.session_state['name'])

'''
OTRA ALTERNATIVA
'''
import streamlit as st
import pandas as pd

if 'name' not in st.session_state:
    st.session_state['name'] = 'John Doe'

st.header(st.session_state['name'])

if st.button('Jane'):
    st.session_state['name'] = 'Jane Doe'
    st.rerun()

if st.button('John'):
    st.session_state['name'] = 'John Doe'
    st.rerun()

st.header(st.session_state['name'])

'''
Botones para agregar otros widgets dinámicamente
Al agregar widgets dinámicamente a la página, asegúrese de usar un índice para mantener las claves únicas y evitar un error. En este ejemplo, definimos una función que representa una fila de widgets. Esa función acepta un como parámetro. Los widgets renderizados por uso dentro de sus claves para que se puedan ejecutar varias veces en un solo script se vuelven a ejecutar sin repetir ninguna tecla de widget.DuplicateWidgetIDdisplay_input_rowindexdisplay_input_rowindexdisplay_input_row

COMO UN FORMULARIO...
'''
import streamlit as st

def display_input_row(index):
    left, middle, right = st.columns(3)
    left.text_input('First', key=f'first_{index}')
    middle.text_input('Middle', key=f'middle_{index}')
    right.text_input('Last', key=f'last_{index}')

if 'rows' not in st.session_state:
    st.session_state['rows'] = 0

def increase_rows():
    st.session_state['rows'] += 1

st.button('Add person', on_click=increase_rows)

for i in range(st.session_state['rows']):
    display_input_row(i)

# Show the results
st.subheader('People')
for i in range(st.session_state['rows']):
    st.write(
        f'Person {i+1}:',
        st.session_state[f'first_{i}'],
        st.session_state[f'middle_{i}'],
        st.session_state[f'last_{i}']
    )


'''
Botones para manejar procesos costosos o de escritura de archivos

Cuando tenga procesos costosos, configúrelos para que se ejecuten al hacer clic en un botón y guarde los resultados en . Esto le permite seguir accediendo a los resultados del proceso sin volver a ejecutarlo innecesariamente. Esto es especialmente útil para los procesos que guardan en el disco o escriben en una base de datos. En este ejemplo, tenemos un que depende de dos parámetros: y . Funcionalmente, cambia la salida, pero no lo hace: está ahí para proporcionar un parámetrost.session_stateexpensive_processoptionaddaddoptionoption
'''
import streamlit as st
import pandas as pd
import time

def expensive_process(option, add):
    with st.spinner('Processing...'):
        time.sleep(5)
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C':[7, 8, 9]}) + add
    return (df, add)

cols = st.columns(2)
option = cols[0].selectbox('Select a number', options=['1', '2', '3'])
add = cols[1].number_input('Add a number', min_value=0, max_value=10)

if 'processed' not in st.session_state:
    st.session_state.processed = {}

# Process and save results
if st.button('Process'):
    result = expensive_process(option, add)
    st.session_state.processed[option] = result
    st.write(f'Option {option} processed with add {add}')
    result[0]

'''
Los observadores astutos pueden pensar: "Esto se siente un poco como el almacenamiento en caché". Solo estamos guardando resultados relativos a un parámetro, pero el patrón podría expandirse fácilmente para guardar resultados relativos a ambos parámetros. En ese sentido, sí, tiene algunas similitudes con el almacenamiento en caché, pero también algunas diferencias importantes. Cuando guarda los resultados en , los resultados solo están disponibles para el usuario actual en su sesión actual. Si utiliza st.cache_data en su lugar, los resultados están disponibles para todos los usuarios en todas las sesiones. Además, si desea actualizar un resultado guardado, debe borrar todos los resultados guardados para que esa función lo haga.st.session_state
'''



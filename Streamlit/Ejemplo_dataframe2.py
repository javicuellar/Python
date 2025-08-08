'''
https://docs.streamlit.io/develop/concepts/design/dataframes

Marcos de datos
Los marcos de datos son una excelente manera de mostrar y editar datos en formato tabular. Trabajar con Pandas DataFrames y otras estructuras de datos tabulares es clave para los flujos de trabajo de ciencia de datos. Si los desarrolladores y científicos de datos quieren mostrar estos datos en Streamlit, tienen múltiples opciones: y . Si desea mostrar únicamente datos en una interfaz de usuario similar a una tabla, st.dataframe es el camino a seguir. Si desea editar datos de forma interactiva, utilice st.data_editor. Exploramos los casos de uso y las ventajas de cada opción en las siguientes secciones.st.dataframest.data_editor

Visualización de tramas de datos con st.dataframe
Streamlit puede mostrar tramas de datos en una interfaz de usuario similar a una tabla a través de:st.dataframe
'''
import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

st.dataframe(df, use_container_width=True)


'''
st.dataframe Características de la interfaz de usuario

st.dataframe Proporciona funcionalidad adicional mediante el uso de glide-data-grid bajo el capó:

Ordenación de columnas: Para ordenar columnas, seleccione sus encabezados o seleccione "Orden ascendente" u "Orden descendente" en el menú de encabezado (more_vert).
Cambio de tamaño de columna: para cambiar el tamaño de las columnas, arrastre y suelte los bordes del encabezado de la columna o seleccione "Tamaño automático" en el menú del encabezado.
Ocultar columnas: Para ocultar columnas, seleccione "Ocultar columna" en el menú de encabezado.
Reordenar y anclar columnas: Para reordenar columnas o anclarlas a la izquierda, arrastre y suelte los encabezados de columna o seleccione "Anclar columna" en el menú de encabezado, respectivamente.
Dar formato a números, fechas y horas: Para cambiar el formato de las columnas numéricas, selecciona una opción en "Formato" en el menú de encabezado.
Cambio de tamaño de tramas de datos: para cambiar el tamaño de las tramas de datos, arrastre y suelte la esquina inferior derecha.
Vista de pantalla completa: para ampliar los marcos de datos a pantalla completa, selecciona el ícono de pantalla completa (pantalla completa) en la barra de herramientas.
Buscar: para buscar en los datos, seleccione el icono de búsqueda (buscar) en la barra de herramientas o use teclas de acceso rápido ( o ).⌘+FCtrl+F
Descargar: Para descargar los datos como un archivo CSV, seleccione el icono de descarga (descargar) en la barra de herramientas.
Copiar al portapapeles: Para copiar los datos en el portapapeles, seleccione una o varias celdas, use las teclas de acceso rápido ( o ) y péguelas en su software de hoja de cálculo favorito.⌘+CCtrl+C

Pruebe todas las características de la interfaz de usuario con la aplicación incrustada de la sección anterior.

Además de Pandas DataFrames, también admite otros tipos comunes de Python, por ejemplo, list, dict o numpy array. También es compatible con Snowpark y PySpark DataFrames, que le permiten evaluar y extraer datos de bases de datos de forma perezosa. Esto puede ser útil para trabajar con grandes conjuntos de datos.st.dataframe
'''

'''
Editar datos con st.data_editor
Streamlit admite tramas de datos editables a través del comando. Echa un vistazo a su API en st.data_editor. Muestra el marco de datos en una tabla, similar a . ¡Pero a diferencia de , esta tabla no es estática! El usuario puede hacer clic en las celdas y editarlas. Los datos editados se devuelven en el lado de Python. Aquí hay un ejemplo:st.data_editorst.dataframest.dataframe
'''

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

edited_df = st.data_editor(df) # 👈 An editable dataframe

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

'''
st.data_editor Características de la interfaz de usuario
st.data_editor También admite algunas cosas adicionales:

Agregar y eliminar filas: puede hacerlo configurando al llamar a . Esto permitirá a los usuarios agregar y eliminar filas según sea necesario.num_rows= "dynamic"st.data_editor
Soporte de copiar y pegar: copie y pegue entre software de hoja de cálculo como Google Sheets y Excel.st.data_editor
Acceder a los datos editados: acceda solo a las ediciones individuales en lugar de a toda la estructura de datos editada a través del estado de sesión.
Ediciones masivas: similar a Excel, simplemente arrastre un controlador para editar las celdas vecinas.
Validación de entrada automática: la configuración de columnas proporciona una sólida compatibilidad con tipos de datos y otras opciones configurables. Por ejemplo, no hay forma de ingresar letras en una celda numérica. Las celdas numéricas pueden tener un mínimo y un máximo designados.
Edite estructuras de datos comunes: admite listas, dictados, NumPy ndarray y más.st.data_editor
'''

'''
Agregar y eliminar filas
Con , los visores pueden agregar o eliminar filas a través de la interfaz de usuario de la tabla. Este modo se puede activar estableciendo el parámetro en :st.data_editornum_rows"dynamic"
'''

edited_df = st.data_editor(df, num_rows="dynamic")

'''
Para agregar nuevas filas, haga clic en el icono más (agregar) en la barra de herramientas. Alternativamente, haga clic dentro de una celda sombreada debajo de la fila inferior de la tabla.
Para eliminar filas, seleccione una o más filas usando las casillas de verificación de la izquierda. Haga clic en el icono de eliminación (b

Acceso a datos editados
----------------------
A veces, es más conveniente saber qué celdas se han cambiado en lugar de recuperar todo el marco de datos editado. Streamlit facilita esto mediante el uso del estado de sesión. Si se establece un parámetro, Streamlit almacenará los cambios realizados en la trama de datos en estado de sesión.key

Este fragmento muestra cómo puede acceder a los datos modificados mediante el estado de sesión:
'''

st.data_editor(df, key="my_key", num_rows="dynamic") # 👈 Set a key
st.write("Here's the value in Session State:")
st.write(st.session_state["my_key"]) # 👈 Show the value in Session State

'''
En este fragmento de código, el parámetro se establece en . Una vez creado el editor de datos, el valor asociado a en el estado de sesión se muestra en la aplicación mediante . Esto muestra las adiciones, ediciones y eliminaciones que se realizaron.key"my_key""my_key"st.write

Esto puede ser útil cuando se trabaja con marcos de datos grandes y solo necesita saber qué celdas han cambiado, en lugar de acceder a todo el marco de datos editado.

Usa todo lo que hemos aprendido hasta ahora y aplícalo a la aplicación integrada anterior. Intente editar celdas, agregar nuevas filas y eliminar filas.

Observe cómo las ediciones de la tabla se reflejan en el estado de la sesión. Cuando realiza cualquier edición, se activa una nueva ejecución que envía las ediciones al backend. El estado del widget es un objeto JSON que contiene tres propiedades: edited_rows, added_rows y deleted rows:.

  * edited_rows es un diccionario que contiene todas las ediciones. Las claves son índices de fila de base cero y los valores son diccionarios que asignan nombres de columna a ediciones (por ejemplo, ).{0: {"col1": ..., "col2": ...}}
  * added_rows es una lista de filas recién agregadas. Cada valor es un diccionario con el mismo formato que el anterior (por ejemplo, ).[{"col1": ..., "col2": ...}]
  * deleted_rows es una lista de números de fila que se han eliminado de la tabla (por ejemplo, ).[0, 2]
st.data_editor no admite la reordenación de filas, por lo que las filas agregadas siempre se anexarán al final de la trama de datos con las ediciones y eliminaciones aplicables a las filas originales.
'''

'''
Editar estructuras de datos comunes
-----------------------------------
¡La edición no solo funciona para Pandas DataFrames! También puede editar listas, tuplas, conjuntos, diccionarios, matrices NumPy o DataFrames de Snowpark y PySpark. La mayoría de los tipos de datos se devolverán en su formato original. Pero algunos tipos (por ejemplo, Snowpark y PySpark) se convierten en DataFrames de Pandas. Para obtener información sobre todos los tipos admitidos, lea la API de st.data_editor.

Por ejemplo, puede permitir fácilmente que el usuario agregue elementos a una lista:
'''

edited_list = st.data_editor(["red", "green", "blue"], num_rows= "dynamic")
st.write("Here are all the colors you entered:")
st.write(edited_list)

'''  O matrices numpy:  '''

import numpy as np

st.data_editor(np.array([
	["st.text_area", "widget", 4.92],
	["st.markdown", "element", 47.22]
]))

'''  O listas de registros: '''

st.data_editor([
    {"name": "st.text_area", "type": "widget"},
    {"name": "st.markdown", "type": "element"},
])

''' ¡O diccionarios y muchos más tipos!  '''

st.data_editor({
	"st.text_area": "widget",
	"st.markdown": "element"
})

'''
Validación automática de entrada
El editor de datos incluye validación de entrada automática para ayudar a evitar errores al editar celdas. Por ejemplo, si tiene una columna que contiene datos numéricos, el campo de entrada restringirá automáticamente al usuario a introducir solo datos numéricos. Esto ayuda a evitar errores que podrían producirse si el usuario introdujera accidentalmente un valor no numérico. Se puede configurar una validación de entrada adicional a través de la API de configuración de columnas. Siga leyendo a continuación para obtener una descripción general de la configuración de columnas, incluidas las opciones de validación.

Configuración de columnas
-------------------------
Puede configurar el comportamiento de visualización y edición de columnas en y a través de la API de configuración de columnas. Hemos desarrollado la API para permitirle agregar imágenes, gráficos y URL en las que se puede hacer clic en el marco de datos y en las columnas del editor de datos. Además, puede hacer que las columnas individuales sean editables, establecer columnas como categóricas y especificar qué opciones pueden tomar, ocultar el índice de la trama de datos y mucho más.st.dataframest.data_editor

La configuración de columnas incluye los siguientes tipos de columnas: Texto, Número, Casilla de verificación, Casilla de selección, Fecha, Hora, Fecha y hora, Lista, Vínculo, Imagen, Gráfico de líneas, Gráfico de barras y Progreso. También hay una opción genérica de columna. Consulte la aplicación integrada a continuación para ver estos diferentes tipos de columnas. Cada tipo de columna se previsualiza individualmente en la documentación de la API de configuración de columnas.

Valores de formato

Hay un parámetro disponible en la configuración de columnas para las columnas Texto, Fecha, Hora y Fecha y hora. También se puede dar formato a columnas similares a gráficos. Las columnas Gráfico de líneas y Gráfico de barras tienen parámetros y para establecer los límites verticales. Para una columna Progreso, puede declarar los límites horizontales con y .formaty_miny_maxmin_valuemax_value

Validar entrada

Al especificar una configuración de columna, puede declarar no solo el tipo de datos de la columna, sino también las restricciones de valor. Todos los elementos de configuración de columna le permiten hacer una columna obligatoria con el parámetro de palabra clave .required=True

En el caso de las columnas Texto y Vínculo, puede especificar el número máximo de caracteres con o utilizar expresiones regulares para validar las entradas a través de . Las columnas numéricas, incluidas Número, Fecha, Hora y Fecha y hora, tienen parámetros y . Las columnas Selectbox tienen una lista configurable de archivos .max_charsvalidatemin_valuemax_valueoptions

El tipo de datos de las columnas Número es de forma predeterminada. Al pasar un valor de tipo a cualquiera de , , , o se establecerá el tipo de la columna como .floatintmin_valuemax_valuestepdefaultint

Configurar una trama de datos vacía

Puede usarlo para recopilar información tabular de un usuario. Cuando se inicia desde una trama de datos vacía, los tipos de columna predeterminados son texto. Utilice la configuración de columnas para especificar los tipos de datos que desea recopilar de los usuarios.st.data_editor
'''

import streamlit as st
import pandas as pd

df = pd.DataFrame(columns=['name','age','color'])
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'name' : st.column_config.TextColumn('Full Name (required)', width='large', required=True),
    'age' : st.column_config.NumberColumn('Age (years)', min_value=0, max_value=122),
    'color' : st.column_config.SelectboxColumn('Favorite Color', options=colors)
}

result = st.data_editor(df, column_config = config, num_rows='dynamic')

if st.button('Get results'):
    st.write(result)

'''
Opciones de formato adicionales
--------------------------------
Además de la configuración de columnas, y tiene algunos parámetros más para personalizar la visualización de su marco de datos.st.dataframest.data_editor

 * hide_index : Establezca en para ocultar el índice de la trama de datos.True
 * column_order : Pase una lista de etiquetas de columna para especificar el orden de visualización.
* disabled : Pase una lista de etiquetas de columna para inhabilitarlas para su edición. Esto le permite evitar deshabilitarlos individualmente.
'''



'''
ver https://docs.streamlit.io/develop/api-reference/data/st.column_config


EJEMPLO DE COLUMNA AreaChartColumn
'''

import pandas as pd
import streamlit as st

data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "sales": st.column_config.AreaChartColumn(
            "Sales (last 6 months)",
            width="medium",
            help="The sales volume in the last 6 months",
            y_min=0,
            y_max=100,
         ),
    },
    hide_index=True,
)


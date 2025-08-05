import streamlit as st
import pandas as pd
from Mvtos.mvtos import LeerMvtos, Analisis_mvtos



import locale

# Configurar la localización
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')



#  Recuperar los movimientos de la hoja de cálculo
hoja = "Cartera (con valoraciones)"
mvtos = LeerMvtos(hoja)

if 'activos' not in st.session_state:
    # Recuperar la cartera, las ventas y los intereses y dividendos de los mvtos
    activos, ventas, int_div, nomina = Analisis_mvtos(mvtos)
    st.session_state.activos = activos
    st.session_state.ventas = ventas
    st.session_state.int_div = int_div
    st.session_state.nomina = nomina
else:
    activos = st.session_state.activos
    ventas = st.session_state.ventas
    int_div = st.session_state.int_div
    nomina = st.session_state.nomina

#  Grabar_analisis(activos, ventas, int_div, nomina)
#  print('Cartera analizada y grabada en Google Sheets.')



### Visualización con Streamlit
# st.title('Cartera IRPF')
# st.subheader('Finanzas Personales')


### Columnas
co1, co2 = st.columns([5,1])

with co1:
    st.subheader('Finanzas Personales')

# Extraer años únicos del DataFrame
años = mvtos['Año'].astype(str).unique().tolist()
años = sorted(años, key=lambda x: int(x), reverse=True)  # Ordenar de mayor a menor
años.insert(0, 'Todos')
with co2:
    año_seleccionado = st.selectbox('Seleccione año:', años)


### Pestañas
tabs = st.tabs(['MOVIMIENTOS','ACTIVOS', 'VENTAS', 'INTERESES Y DIVIDENDOS', 'NÓMINA', 'PRUEBAS'])

# Pestaña Movimientos
with tabs[0]:
    st.subheader('Movimientos de la Cartera')
    st.dataframe(mvtos)

# Pestaña Activos
with tabs[1]:
    st.subheader('Cartera Actual')

    # Mostrar el DataFrame y expandir a todo el ancho
    st.dataframe(activos.style.set_table_attributes('style="width:100%;"'), hide_index=True)

# Pestaña Ventas
with tabs[2]:
    st.subheader('Ventas Realizadas')

    # Mostrar el DataFrame y expandir a todo el ancho
    st.dataframe(ventas.style.set_table_attributes('style="width:100%;"'), hide_index=True)

# Pestaña Intereses y Dividendos
with tabs[3]:
    st.subheader('Intereses y Dividendos')

    # Mostrar el DataFrame y expandir a todo el ancho
    st.dataframe(int_div.style.set_table_attributes('style="width:100%;"'), hide_index=True)

# Pestaña Nómina
with tabs[4]:
    # st.subheader('Nómina')

    # Mostrar el DataFrame y expandir a todo el ancho     NO FUNCIONA
    # st.dataframe(nomina, use_container_width=True, hide_index=True)

    
    # Formatear la fecha, Año y Mes
    if 'formated' not in st.session_state:
        st.session_state.formated = True
        nomina.rename(columns={'Año': 'year', 'Mes': 'month'}, inplace=True)
        nomina['fecha_temporal'] = pd.to_datetime(nomina[['year', 'month']].assign(DAY=1))
        # Formatear la columna de fecha a string
        nomina['Fecha'] = nomina['fecha_temporal'].dt.strftime('%Y - %B')
        
        # Formatear los importes
        nomina['Neto'] = nomina['Neto'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
        nomina['Cotiz. SS'] = nomina['Cotiz. SS'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
        nomina['Retención'] = nomina['Retención'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
        nomina['Imp. Integro'] = nomina['Imp. Integro'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
        
        st.session_state.nomina = nomina


    ### Columnas
    col1, col2 = st.columns([1,1])

    # Extraer años únicos del DataFrame
    # años = nomina['year'].astype(str).unique().tolist()
    # años.insert(0, 'Todos')
    
    # año_seleccionado = st.selectbox('Selecciona el año:', años)
    if año_seleccionado == 'Todos':
        df_filtrado = nomina
    else:
        df_filtrado = nomina[nomina['year'] == int(año_seleccionado)]

    # Extraer pagadores únicos del DataFrame
    pagadores = df_filtrado['Pagador Nómina'].unique().tolist()
    pagadores.insert(0, 'Todos')
    
    with col1:
        pagador_seleccionado = st.selectbox('Selecciona el Pagador Nómina:', pagadores)

    if pagador_seleccionado != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['Pagador Nómina'] == pagador_seleccionado]

    # No mostramos la columnas, 'Year', 'Month', 'fecha_temporal'
    df_filtrado = df_filtrado.drop(columns=['year', 'month', 'fecha_temporal'])
    
    # Reordenamos las columnas
    df_filtrado = df_filtrado[['Fecha', 'Pagador Nómina', 'Imp. Integro', 'Retención', 'Cotiz. SS', 'Neto']]

    # Configurar el ancho de las columnas
    st.dataframe(df_filtrado.style.set_table_attributes('style="width:100%;"'), hide_index=True)


with tabs[5]:
    st.subheader('Pruebas')
    st.write('Contenido de la pestaña de pruebas')

#### PARA EJECUTAR EN OTRO PUERTO 
# streamlit run app.py --server.port 8510

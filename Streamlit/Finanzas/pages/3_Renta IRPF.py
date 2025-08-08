import streamlit as st
import pandas as pd




if not st.session_state['logged_in']:
    st.warning("Debes iniciar sesión para ver esta página.")
    st.stop()




import locale

# Configurar la localización
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')






### Columnas
co1, co2 = st.columns([5,1])

with co1:
    st.subheader('Renta IRPF')

# Extraer años únicos del DataFrame
años = st.session_state.mvtos['Año'].astype(str).unique().tolist()
años = sorted(años, key=lambda x: int(x), reverse=True)  # Ordenar de mayor a menor
años.insert(0, 'Todos')

with co2:
    año_seleccionado = st.selectbox('Seleccione año:', años, index=1)



### Pestañas
tabs = st.tabs(['VENTAS', 'INTERESES Y DIVIDENDOS', 'NÓMINA', 'RESUMEN IRPF'])

# Pestaña Ventas
with tabs[0]:
    if año_seleccionado == 'Todos':
        df_ventas = st.session_state.ventas.copy()
    else:
        df_ventas = st.session_state.ventas[st.session_state.ventas['Año'] == int(año_seleccionado)].copy()

    df_ventas = df_ventas.drop(columns=['Año'])

    # Formatear los importes
    df_ventas['P.Venta'] = df_ventas['P.Venta'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
    df_ventas['P.Compra'] = df_ventas['P.Compra'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
    df_ventas['Ganancias'] = df_ventas['Ganancias'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
    df_ventas['Perdidas'] = df_ventas['Perdidas'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))

    # Mostrar el DataFrame y expandir a todo el ancho
    st.dataframe(df_ventas.style.set_table_attributes('style="width:100%;"'), hide_index=True)


# Pestaña Intereses y Dividendos
with tabs[1]:
    if año_seleccionado == 'Todos':
        df_int_div = st.session_state.int_div.copy()
    else:
        df_int_div = st.session_state.int_div[st.session_state.int_div['Año'] == int(año_seleccionado)].copy()

    # Ordenar el DataFrame por las columnas: Interés, Entidad, Activo y Fecha
    df_int_div = df_int_div.sort_values(by=['Tipo', 'Entidad', 'Activo', 'Fecha'], ascending=[False, True, True, True])

    # Mostrar el DataFrame y expandir a todo el ancho
    st.dataframe(df_int_div.style.set_table_attributes('style="width:100%;"'), hide_index=True)


# Pestaña Nómina
with tabs[2]:
    df_nomina = st.session_state.nomina.copy()

    # Formatear la fecha, Año y Mes y formatear los importes
    df_nomina.rename(columns={'Año': 'year', 'Mes': 'month'}, inplace=True)
    df_nomina['fecha_temporal'] = pd.to_datetime(df_nomina[['year', 'month']].assign(DAY=1))
    # Formatear la columna de fecha a string
    df_nomina['Fecha'] = df_nomina['fecha_temporal'].dt.strftime('%Y - %B')


    ### Columnas
    col1, col2 = st.columns([1,1])

    if año_seleccionado == 'Todos':
        df_nomina = df_nomina
    else:
        df_nomina = df_nomina[df_nomina['year'] == int(año_seleccionado)]

    # Extraer pagadores únicos del DataFrame
    pagadores = df_nomina['Pagador Nómina'].unique().tolist()
    pagadores.insert(0, 'Todos')
    
    with col1:
        pagador_seleccionado = st.selectbox('Selecciona el Pagador Nómina:', pagadores)

    if pagador_seleccionado != 'Todos':
        df_nomina = df_nomina[df_nomina['Pagador Nómina'] == pagador_seleccionado]

    # No mostramos la columnas, 'Year', 'Month', 'fecha_temporal'
    df_nomina = df_nomina.drop(columns=['year', 'month', 'fecha_temporal'])

    # Reordenamos las columnas
    df_nomina = df_nomina[['Fecha', 'Pagador Nómina', 'Imp. Integro', 'Retención', 'Cotiz. SS', 'Neto']]

    # Formatear los importes
    df_nomina['Neto'] = df_nomina['Neto'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
    df_nomina['Cotiz. SS'] = df_nomina['Cotiz. SS'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
    df_nomina['Retención'] = df_nomina['Retención'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
    df_nomina['Imp. Integro'] = df_nomina['Imp. Integro'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))

    # Configurar el ancho de las columnas
    st.dataframe(df_nomina.style.set_table_attributes('style="width:100%;"'), hide_index=True)



# Pestaña Resumen IRPF
with tabs[3]:
    st.subheader('Rendimiento del trabajo')

    df_nomina = st.session_state.nomina.copy()

    # año_seleccionado = st.selectbox('Selecciona el año:', años)
    if año_seleccionado == 'Todos':
        df_suma = df_nomina
    else:
        df_suma = df_nomina[df_nomina['Año'] == int(año_seleccionado)]

    # Agrupar por 'pagador nomina' y sumar las columnas deseadas
    resultado = df_suma.groupby('Pagador Nómina').agg({
                            'Imp. Integro': 'sum',
                            'Retención': 'sum',
                            'Cotiz. SS': 'sum',
                            'Neto': 'sum'
                            }).reset_index()

    # Calcular el total de cada columna
    totales = resultado[['Imp. Integro', 'Retención', 'Cotiz. SS', 'Neto']].sum()
    totales['Pagador Nómina'] = 'Total'  # Añadir etiqueta para la fila de totales

    # Formatear los importes
    resultado['Neto'] = resultado['Neto'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
    resultado['Cotiz. SS'] = resultado['Cotiz. SS'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
    resultado['Retención'] = resultado['Retención'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
    resultado['Imp. Integro'] = resultado['Imp. Integro'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))

    # st.dataframe(resultado.style.set_table_attributes('style="width:100%;"'), hide_index=True)
    st.dataframe(resultado.style.set_table_attributes('style="width:100%;"').set_properties(**{'text-align': 'right'}), hide_index=True)


    # Reordenamos las columnas
    totales = totales.to_frame().T
    totales = totales[['Pagador Nómina', 'Imp. Integro', 'Retención', 'Cotiz. SS', 'Neto']]
    # Formatear los importes
    totales['Neto'] = totales['Neto'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
    totales['Cotiz. SS'] = totales['Cotiz. SS'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
    totales['Retención'] = totales['Retención'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
    totales['Imp. Integro'] = totales['Imp. Integro'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))

    cols = st.columns([2,1,1,1,1])
    cols[0].markdown(f"**TOTALES**")
    cols[1].markdown(totales['Imp. Integro'].values[0])
    cols[2].markdown(totales['Retención'].values[0])
    cols[3].markdown(totales['Cotiz. SS'].values[0])
    cols[4].markdown(totales['Neto'].values[0])


    st.stop()

    ###  Rendimiento de Cuentas e Intereses
    st.write('---')
    df = int_div
    st.subheader('Rendimiento de Cuentas e Intereses')
    st.write((df))
    
    if 'formateado' not in st.session_state:
        # Formatear los importes
        df['Bruto'] = df['Bruto'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
        df['Retención'] = df['Retención'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
        df['Comisión'] = df['Comisión'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
        df['Neto'] = df['Neto'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))


    # año_seleccionado = st.selectbox('Selecciona el año:', años)
    if año_seleccionado == 'Todos':
        df_filtrado_suma = df
    else:
        df_filtrado_suma = df[df['year'] == int(año_seleccionado)]

    # Agrupar por 'Entidad' y 'Activo' y sumar las columnas deseadas
    resultado = df_filtrado_suma.groupby(['Entidad', 'Activo']).agg({
                            'Bruto': 'sum',
                            'Retención': 'sum',
                            'Comisión': 'sum',
                            'Neto': 'sum'
                            }).reset_index()

    
    st.write(resultado)
    st.write('----')

    # Calcular el total de cada columna
    totales = resultado[['Bruto', 'Retención', 'Comisión', 'Neto']].sum()
    totales['Entidad - Activo'] = 'Total'  # Añadir etiqueta para la fila de totales

    # Formatear los importes
    resultado['Neto'] = resultado['Neto'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
    resultado['Comisión'] = resultado['Comisión'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
    resultado['Retención'] = resultado['Retención'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
    resultado['Bruto'] = resultado['Bruto'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))

    # st.dataframe(resultado.style.set_table_attributes('style="width:100%;"'), hide_index=True)
    st.dataframe(resultado.style.set_table_attributes('style="width:100%;"').set_properties(**{'text-align': 'right'}), hide_index=True)

    # Reordenamos las columnas
    totales = totales.to_frame().T
    totales = totales[['Entidad - Activo', 'Bruto', 'Retención', 'Comisión', 'Neto']]
    # Formatear los importes
    totales['Neto'] = totales['Neto'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
    totales['Comisión'] = totales['Comisión'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
    totales['Retención'] = totales['Retención'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))
    totales['Bruto'] = totales['Bruto'].apply(lambda x: locale.currency(x, symbol='€', grouping=True).rjust(15))

    cols = st.columns([2,1,1,1,1])
    cols[0].markdown(f"**TOTALES**")
    cols[1].markdown(totales['Bruto'].values[0])
    cols[2].markdown(totales['Retención'].values[0])
    cols[3].markdown(totales['Comisión'].values[0])
    cols[4].markdown(totales['Neto'].values[0])




#### PARA EJECUTAR EN OTRO PUERTO 
# streamlit run app.py --server.port 8510

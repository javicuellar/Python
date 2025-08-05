import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np

#  Ignora los warnings que muestra los modelos
import warnings
warnings.filterwarnings('ignore')


#   Definir el límite de acceso, el scope = alcance, acceso a hojas de cálculo y drive
alcance =  ['https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive']

Credenciales = ServiceAccountCredentials.from_json_keyfile_name('D:\Python\Credenciales.json', alcance)
cliente = gspread.authorize(Credenciales)


## Función para leer movimientos de una hoja de cálculo de Google Sheets
#  Esta función lee los movimientos de una hoja de cálculo y devuelve un DataFrame con los movimientos.
#  Se eliminan las columnas que no se van a utilizar y se convierten los tipos
def LeerMvtos(hoja_google):
    hoja = cliente.open(hoja_google)
    activos = hoja.worksheet('Mvtos')

    # Recuperar todos los datos
    mvtos = pd.DataFrame(activos.get_all_records())

    # Eliminamos columnas que no vamos a utilizar
    cols_eliminar = ['Broker - Activos', 'Saldo', '', '% Rent', 'Previsión']
    mvtos = mvtos.drop(columns=cols_eliminar, errors='ignore')

    # Convertir de tipos del dataframe
    #  - Fecha en formato datetime
    mvtos['Fecha'] = pd.to_datetime(mvtos['Fecha'], format='%d/%m/%Y')  # Ajusta el formato según sea necesario
    #  - Importe
    mvtos['Importe'] = (mvtos['Importe']
                             .astype(str)
                             .str.replace(' €', '', regex=False)
                             .str.replace('.', '' , regex=False)  # Remove thousands separator
                             .str.replace(',', '.', regex=False)  # Replace decimal separator
                             )
    mvtos['Importe'] = pd.to_numeric(mvtos['Importe'], errors='coerce')

    #  - Num.  (número de acciones)
    mvtos['Num.'] = (mvtos['Num.']
                             .astype(str)
                             .str.replace(' €', '', regex=False)
                             .str.replace('.', '' , regex=False)  # Remove thousands separator
                             .str.replace(',', '.', regex=False)  # Replace decimal separator
                             )
    mvtos['Num.'] = pd.to_numeric(mvtos['Num.'], errors='coerce')

    #  - Precio
    mvtos['Precio'] = (mvtos['Precio']
                             .astype(str)
                             .str.replace(' €', '', regex=False)
                             .str.replace('.', '' , regex=False)  # Remove thousands separator
                             .str.replace(',', '.', regex=False)  # Replace decimal separator
                             )
    mvtos['Precio'] = pd.to_numeric(mvtos['Precio'], errors='coerce')

    #  - P. Venta/Ant.
    mvtos['P. Venta/Ant.'] = (mvtos['P. Venta/Ant.']
                             .astype(str)
                             .str.replace(' €', '', regex=False)
                             .str.replace('.', '' , regex=False)  # Remove thousands separator
                             .str.replace(',', '.', regex=False)  # Replace decimal separator
                             )
    mvtos['P. Venta/Ant.'] = pd.to_numeric(mvtos['P. Venta/Ant.'], errors='coerce')

    return mvtos



#  Versión 2 - Incluimos información nómina e indemnización BBVA
#  Esta función analiza los movimientos y devuelve un DataFrame con el análisis de la cartera,
#  un DataFrame con las ventas y un DataFrame con los intereses y dividendos.
#  También devuelve un DataFrame con la nómina e indemnización de BBVA.
def Analisis_mvtos(df):
    analisis = {}
    ventas = {}
    int_div = {}
    dividendos = {}
    nomina = {}
    fecha = 1

    for i, fila in df.iterrows():
        if fila['Tipo'] == 'Carteras':
            activo = fila['Entidad'] + ' - ' + fila['Producto'] + fila['Descripción']
            clave_div = fila['Entidad'] + ' - ' + fila['Descripción']
            if activo in analisis:
                importe = round(analisis[activo]['Importe'], 2)
                num = analisis[activo]['Num']
            else:
                analisis[activo] = {'Entidad': fila['Entidad'], 'Producto': fila['Producto'], 'Descripción': fila['Descripción'],
                                    'Importe': 0.0, 'Num': 0.0, 'Dividendos': 0.0}
                importe = 0.0
                num = 0.0
                if fila['Producto'] != 'Cuenta':
                    dividendos[clave_div] = {'activo': activo}

            if fila['Subtipo'] == 'Compra':
                analisis[activo]['Importe'] = round(importe + fila['Importe'], 2)
                analisis[activo]['Num'] = round(num + fila['Num.'], 6)
                analisis[activo]['Abierta'] = fila['Abierta']

            if fila['Subtipo'] == 'Traspaso':
                analisis[activo]['Importe'] = round(importe + fila['Importe'], 2)
                analisis[activo]['Num'] = round(num + fila['Num.'], 6)
                analisis[activo]['Abierta'] = fila['Abierta']

            if fila['Subtipo'] == 'Venta':
                if num == 0:
                    print(' * NUM = 0 ', fila['Fecha'], activo, ' --> ', analisis[activo], fila)
                else:
                    if fecha != fila['Fecha']:
                        seq = 1
                    else:
                        seq += 1
                    clave_ventas = fila['Fecha'].strftime("%Y/%m/%d") + '-' + str(seq) + '-' + activo
                    fecha = fila['Fecha']

                    ventas[clave_ventas] = {'Entidad': fila['Entidad'], 'Activo': fila['Descripción'],
                                      'Fecha': fila['Fecha'].strftime("%d/%m/%Y"), 'Año': fila['Fecha'].year,
                                      'P.Venta': -fila['Importe'], 'P.Compra': round(-(fila['Num.'] * ( importe / num )), 2)}

                    plusvalias = round(ventas[clave_ventas]['P.Venta'] - ventas[clave_ventas]['P.Compra'], 2)
                    if plusvalias >= 0:
                        ganancias = plusvalias
                        perdidas = 0.0
                    else:
                        ganancias = 0.0
                        perdidas = plusvalias
                    ventas[clave_ventas]['Ganancias'] = ganancias
                    ventas[clave_ventas]['Perdidas'] = perdidas

                    analisis[activo]['Importe'] = round(importe + fila['Num.'] * ( importe / num ), 2)
                    analisis[activo]['Num'] = round(num + fila['Num.'], 6)

                    analisis[dividendos[clave_div]['activo']]['Dividendos'] = 0.0

        # Recuperamos información de intereses y dividendos
        if fila['Subtipo'] == 'Intereses' or fila['Subtipo'] == 'Dividendos':
            clave_int = fila['Fecha'].strftime("%Y/%m/%d") + '-' + fila['Entidad'] + ' - ' + fila['Descripción']

            if isinstance(fila['Precio'], float) and not np.isnan(fila['Precio']):
                retención = fila['Precio']
            else:
                retención = 0.0

            if isinstance(fila['P. Venta/Ant.'], float) and not np.isnan(fila['P. Venta/Ant.']):
                comisión = fila['P. Venta/Ant.']
            else:
                comisión = 0.0

            int_div[clave_int] = {'Entidad': fila['Entidad'], 'Activo': fila['Descripción'], 'Tipo': fila['Subtipo'],
                                  'Fecha': fila['Fecha'].strftime("%d/%m/%Y"), 'Año': fila['Fecha'].year,
                                  'Bruto': round(fila['Importe'], 2) + retención + comisión,
                                  'Retención': round(retención, 2), 'Comisión': round(comisión, 2),
                                  'Neto': round(fila['Importe'], 2) }
            if fila['Subtipo'] == 'Dividendos':
                analisis[dividendos[clave_div]['activo']]['Dividendos'] += round(fila['Importe'], 2)

        # Recuperamos información de nómina e indemnización de BBVA
        if fila['Subtipo'] == 'Nómina' or fila['Subtipo'] == 'Indemnización BBVA':
            clave_nom = fila['Fecha'].strftime("%Y/%m/%d") + '-' + fila['Entidad'] + ' - ' + fila['Descripción']

            if isinstance(fila['Precio'], float) and not np.isnan(fila['Precio']):
                retención = round(fila['Precio'], 2)
            else:
                retención = 0.0

            if isinstance(fila['P. Venta/Ant.'], float) and not np.isnan(fila['P. Venta/Ant.']):
                gastos_ss = round(fila['P. Venta/Ant.'], 2)
            else:
                gastos_ss = 0.0

            if isinstance(fila['Num.'], float) and not np.isnan(fila['Num.']):
                imp_integro = round(fila['Num.'], 2)
            else:
                imp_integro = 0.0

            nomina[clave_nom] = {'Pagador Nómina': fila['Descripción'], 'Año': fila['Fecha'].year, 'Mes': fila['Fecha'].month,
                                  'Imp. Integro': imp_integro, 'Retención': round(retención, 2), 'Cotiz. SS': round(gastos_ss, 2),
                                  'Neto': round(fila['Importe'], 2) }

            if fila['Subtipo'] == 'Dividendos':
                analisis[dividendos[clave_div]['activo']]['Dividendos'] += round(fila['Importe'], 2)

    analisis = pd.DataFrame.from_dict(analisis, orient='index')
    # analisis['Abierta'].fillna('J', inplace=True)
    analisis = analisis[analisis['Abierta'] == 'A']
    analisis = analisis.drop(columns='Abierta', errors='ignore')
    ventas = pd.DataFrame.from_dict(ventas, orient='index')
    int_div = pd.DataFrame.from_dict(int_div, orient='index')
    nomina = pd.DataFrame.from_dict(nomina, orient='index')

    return analisis.sort_index(), ventas.sort_index(), int_div.sort_index(), nomina.sort_index()




# Función para grabar hoja Google Sheets
def Grabar_analisis(activos, ventas, int_div, nomina):
    # Crear hoja de cálculo
    # hoja = cliente.create('Cartera Python')
    # Abrir hoja de cálculo
    hoja = cliente.open('Cartera Python')
    hoja1 = hoja.get_worksheet(1)
    hoja2 = hoja.get_worksheet(2)
    hoja3 = hoja.get_worksheet(3)
    hoja4 = hoja.get_worksheet(4)

    hoja1.clear()
    hoja2.clear()
    hoja3.clear()
    hoja4.clear()

    cabecera = activos.columns.values.tolist()
    # Replace NaN values with None for JSON compatibility
    datos = activos.replace({np.nan: None}).values.tolist()
    hoja1.update([cabecera] + datos)

    cabecera = ventas.columns.values.tolist()
    # Replace NaN values with None for JSON compatibility
    datos = ventas.replace({np.nan: None}).values.tolist()
    hoja2.update([cabecera] + datos)

    cabecera = int_div.columns.values.tolist()
    # Replace NaN values with None for JSON compatibility
    int_div['Bruto'].fillna(0.0, inplace=True)
    int_div['Neto'].fillna(0.0, inplace=True)
    datos = int_div.replace({np.nan: None}).values.tolist()
    hoja3.update([cabecera] + datos)

    cabecera = nomina.columns.values.tolist()
    # Replace NaN values with None for JSON compatibility
    datos = nomina.replace({np.nan: None}).values.tolist()
    hoja4.update([cabecera] + datos)



if __name__ == "__main__":
    #  Recuperar los movimientos de la hoja de cálculo
    hoja = "Cartera (con valoraciones)"
    mvtos = LeerMvtos(hoja)

    # Recuperar la cartera, las ventas y los intereses y dividendos de los mvtos
    activos, ventas, int_div, nomina = Analisis_mvtos(mvtos)

    Grabar_analisis(activos, ventas, int_div, nomina)
    print('Cartera analizada y grabada en Google Sheets.')
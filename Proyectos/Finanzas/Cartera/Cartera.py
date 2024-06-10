import pandas as pd
import datetime as dt
from tqdm import tqdm       # librería para crear BARRA DE PROGRESO
import leer_google as g
import funciones as f
import leer_web as w



#  Proceso la lista de activos analizando los datos y transformando campos numéricos
#      Devuelve una tupla con dos listas
#        - lista con el índice de campos de la información
#        - lista con la información procesada (formateada)
def Preproceso_activos(lista):
    cont = 0
    datos = list()
    for linea in tqdm(lista):           # con barra de proceso
        try:
            cont += 1
            if cont == 1:
                indice = linea[0:14]
            elif linea[11] != '':
                # print("P. Compra: ", linea[10], " -> ", linea[0:3] + linea[6:12])
                compra = f.ExtraerNum(linea[7])
                # fecha = linea[9]
                num = f.ExtraerNum(linea[10])
                traspaso = f.ExtraerNum(linea[11])
                valor = f.ExtraerNum(linea[12])
                datos.append(linea[0:7] + [compra] + linea[8:10] + [num, traspaso, valor] + [linea[13]])
        except ValueError:
            print("Error línea: ", cont, " línea[7:12]-> ", linea[7:14])
    return (indice, datos)


def Valorar(entrada):
    activo = entrada[0]
    producto = entrada[1]
    isin = entrada[2]
    morningstar = entrada[3]
    if morningstar == '':
        valor = 0
    else:
        valor = w.LeerPrecio(producto, activo, morningstar)
    return valor


def Valoración_activos(dfActivos, hoja, pestaña):
    #  Eliminamos activos duplicados
    df_valor = dfActivos[['Activo', 'Producto', 'ISIN', 'MorningStar']].drop_duplicates()

    #  Usamos la función Valorar con todos los parámetros del Dataframe
    df_valor['Valor'] = df_valor.apply(Valorar, axis=1)
    # df_valor.head()

    #  Grabamos los datos de Valoración en su pestaña "Valoración"
    cabecera = df_valor.columns.values.tolist()
    datos = df_valor.values.tolist()
    g.Grabar_hoja(hoja, pestaña, cabecera, datos)


def LeerCartera(hoja, pestaña):
    lista_activos = g.Leer_hoja(hoja, pestaña)
    index, activos = Preproceso_activos(lista_activos)
    return pd.DataFrame(activos, columns=index)


#  ---------  INICIO PROGRAMA  ------------
hoja_google = "Cartera limpia"
pestaña_Activos = "Activos"
pestaña_Valoración = "Valoración"
pestaña_Historial = "Historial"
pestaña_Cartera = "Cartera"

#  Lectura de hoja google "Cartera limpia" , pestaña "Activos"  => Graba en DataFrame
df = LeerCartera(hoja_google, pestaña_Activos)

#  Valoración de cartera de activos => Graba pesstaña "Valoración"
Valoración_activos(df, hoja_google, pestaña_Valoración)

#  Volvemos a leer la cartera con la valoración recien actualizada para Grabar históricos
df = LeerCartera(hoja_google, pestaña_Activos)

print(df.head())
#  Informe de Activos vigentes (posición abierta) => Grabar en "Historial"
dfActivos = df[df['Abierta'] == 'A']
dfActivos = dfActivos.groupby(['Bloque','Tipo','Activo']).sum()
dfActivos.reset_index(inplace=True)
#  Grabamos en pestaña "Historial"
cabecera = dfActivos.columns.values.tolist()
datos = dfActivos.values.tolist()
g.Grabar_hoja(hoja_google, pestaña_Historial, cabecera, datos)





#  Informe de Cartera de activos en formato horizontal => 
cartera = dfActivos
cartera = cartera.drop(columns=['P. Compra','Num.','P. Traspaso'], axis=1)
cartera = cartera.transpose()
cartera.reset_index(inplace=True)

#  Arreglamos columna Index
cartera.loc[0, 'index'] = ''
cartera.loc[1, 'index'] = ''
cartera.loc[3, 'index'] = str(dt.date.today())

#  Recorrer las filas de Bloques y Tipos y crear columnas para totales
#  Acumulamos el valor en la última línea
bloque = cartera.iloc[0][0]
tipo = cartera.iloc[1][0]
suma = 0
ins = 0
n = 0
total = 0
totalCartera = 0
tamaño = len(cartera.iloc[1])
print(tamaño)
for i in range(tamaño - 1):
    print("> ", i, str(cartera.iloc[0][i]), str(cartera.iloc[1][i]), str(cartera.iloc[2][i]))
    if tipo == str(cartera.iloc[1][i]) and bloque == str(cartera.iloc[0][i]):
        n += 1
        suma += cartera.iloc[3][i]
    else:
        if n > 1:
            total += 1
            nombre = 'Total' + str(total)
            ins += 1
            print("  > ", nombre)
            columna = [bloque, tipo, 'VALOR', round(cartera.iloc[3][i-n+ins : i+ins].sum())]
            cartera.insert(loc=i+ins, column=nombre, value=columna)
            print(round(cartera.iloc[3][i-n+ins : i+ins].sum()))
        
        if bloque != str(cartera.iloc[0][i]):
            totalCartera += 1
            nombre = 'Cartera' + str(totalCartera)
            ins += 1
            columna = [bloque, 'TOTAL', 'TOTAL', suma]
            cartera.insert(loc=i + ins, column=nombre, value=columna)
            suma = cartera.iloc[3][i]
        else:
            suma += cartera.iloc[3][i]
        
        tipo =  str(cartera.iloc[1][i])
        bloque = str(cartera.iloc[0][i])
        n = 1

i = i+1
total += 1
nombre = 'Total' + str(total)
ins += 1
columna = [bloque, tipo, 'VALOR', round(cartera.iloc[3][i-n+ins : i+ins].sum())]
cartera.insert(loc=i+ins, column=nombre, value=columna)

totalCartera += 1
nombre = 'Cartera' + str(totalCartera)
ins += 1
columna = [bloque, 'TOTAL', 'TOTAL', suma]
cartera.insert(loc=i + ins, column=nombre, value=columna)

#  Grabamos en pestaña "Cartera"
datos = cartera.values.tolist()
g.Grabar_hoja(hoja_google, pestaña_Cartera, [], datos)
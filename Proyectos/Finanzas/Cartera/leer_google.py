import gspread
from oauth2client.service_account import ServiceAccountCredentials

#  Ignora los warnings que muestra los modelos
import warnings
warnings.filterwarnings('ignore')

#   Definir el límite de acceso, el scope = alcance, acceso a hojas de cálculo y drive
alcance =  ['https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive']

fic_Credenciales = "D:\\Python\\Cartera\\Credenciales.json"
Credenciales = ServiceAccountCredentials.from_json_keyfile_name(fic_Credenciales, alcance)

cliente = gspread.authorize(Credenciales)



#  Lectura de la "pestaña" de la "hoja" de google, devuelve una lista.
def Leer_hoja(hoja, pestaña):
    h = cliente.open(hoja)
    p = h.worksheet(pestaña)
    return p.get_all_values()


#  Grabamos los datos de Valoración en su pestaña "Valoración" con la información de:
#   - cabeceera.- lista con la cabecera de los datos
#   - datos.- lista con la información
def Grabar_hoja(hoja, pestaña, cabecera, datos):
    h = cliente.open(hoja)
    valoracion = h.worksheet(pestaña)
    valoracion.update([cabecera] + datos)

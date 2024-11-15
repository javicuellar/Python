import pandas as pd



def Recuperar_tablas(url):
    '''  Recuperar tablas de la página web dada, url. '''
    try:
        tablas = pd.read_html(url, header=0)       # Usar la primera fila como índice de las columnas
    except Exception as e:
        print(f"Error al acceder a la web: {e}")
    
    return tablas

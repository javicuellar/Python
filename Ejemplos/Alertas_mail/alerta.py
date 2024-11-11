import pandas as pd


url = "https://es.investing.com/equities/bbva" 

#  Recuperamos la tabla con los puestos
try:
    tablas = pd.read_html(url, header=0)   # Usar la primera fila como índice de las columnas
except Exception as e:
    print(f"Error al acceder a la web: {e}")

print(tablas)
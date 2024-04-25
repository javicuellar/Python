import os
import pandas as pd

path_carpeta = u'D:\Python'

for fichero in os.listdir(path_carpeta):
    if fichero.endswith('.csv'):
        print("CSV -> ", fichero)
    else:
        print("No vale: ", fichero)

exit()

df_combinar = pd.concat([pd.read_csv(os.path.join(path_carpeta, fichero)) 
            for fichero in os.listdir(path_carpeta) if fichero.endswith('.csv')], ignore_index=True)

print(df_combinar)
import os
import shutil



source = 'C:/Users/javic/Downloads'
destino = 'C:/Users/javic/Downloads/Archivos'

for fichero in os.listdir(source):
    if fichero.endswith('.pdf') or fichero.endswith('.PDF'):
        print(fichero)
        shutil.move(os.path.join(source, fichero), os.path.join(destino, fichero))

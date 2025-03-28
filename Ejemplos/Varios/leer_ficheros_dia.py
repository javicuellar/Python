import os
import pandas as pd
from datetime import datetime, timedelta



def get_modified_files(directory, days_ago=7, file_types=None, min_size=None, max_size=None):
    """
    Obtiene los archivos modificados o creados en los últimos 'days_ago' días
    en un directorio y sus subdirectorios, con filtros opcionales por tipo y tamaño.

    Args:
        directory (str): El directorio a escanear.
        days_ago (int): Número de días atrás para considerar.
        file_types (list): Lista de extensiones de archivo a filtrar (por ejemplo, ['txt', 'csv']).
        min_size (int): Tamaño mínimo del archivo en bytes.
        max_size (int): Tamaño máximo del archivo en bytes.

    Returns:
        pandas.DataFrame: Un DataFrame con la información de los archivos modificados.
    """

    today = datetime.now()
    limit_date = today - timedelta(days=days_ago)
    files = []

    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            created_time = datetime.fromtimestamp(os.path.getctime(file_path))
            file_size = os.path.getsize(file_path)

            # Filtro por tipo de archivo
            if file_types is not None and not any(filename.endswith(ext) for ext in file_types):
                continue

            # Filtro por tamaño
            if min_size is not None and file_size < min_size:
                continue
            if max_size is not None and file_size > max_size:
                continue

            # Filtro por fecha
            if modified_time >= limit_date or created_time >= limit_date:
                files.append([file_path, modified_time, created_time, file_size])

    df = pd.DataFrame(files, columns=['Ruta del Archivo', 'Fecha de Modificación', 'Fecha de Creación', 'Tamaño (bytes)'])
    return df



# Ejemplo de uso:
directory = '//NAS\\video'
df_modified_files = get_modified_files(directory, file_types=['txt', 'csv', 'mkv', 'avi'], min_size=1024)

print(df_modified_files)
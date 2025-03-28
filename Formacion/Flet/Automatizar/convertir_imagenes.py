import os
from PIL import Image



def convertir_imagen(ruta_entrada, formato_salida):
    """
    Convierte una imagen a formato especificado.

    Args:
        ruta_entrada (str): Ruta de la imagen original
        formato_salida (str): Formato de salida de la imagen (por ejemplo: 'png', 'jpg', 'bmp', 'gif')
    """
    try:
        # Obtener el nombre del archivo sin extensión
        nombre_base = os.path.splitext(ruta_entrada)[0]
        
        # Abrir la imagen y guardarla en el formato especificado
        with Image.open(ruta_entrada) as img:
            # Si la imagen es RGBA, y queremos convertir a JPEG, se convierte a RGB
            if img.mode == ('RGBA', 'LA') and formato_salida.upper() == 'JPEG':
                img = img.convert('RGB')
            
            # Crear el nombre del archivo de salida
            ruta_salida = f"{nombre_base}.{formato_salida.lower()}"
            img.save(ruta_salida, formato_salida.upper())
            print(f"Imagen convertida correctamente: {formato_salida.upper()}")
        
    except Exception as e:
        print(f"Error al convertir imagen: {e}")




if __name__ == '__main__':
    imagen = "C:\\Users\javic\Downloads\Archivos\Imagenes\Jamon.jpg"
    convertir_imagen(imagen, formato_salida='gif')

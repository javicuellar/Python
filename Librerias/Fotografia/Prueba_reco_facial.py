from Reconocimiento_facial import *


# Descarga de las imágenes de referencia
# ==============================================================================
def Descarga_imagenes():
    import urllib
    import zipfile

    url = ('https://github.com/JoaquinAmatRodrigo/Estadistica-machine-learning-python/'
           'raw/master/images/imagenes_referencia_reconocimiento_facial.zip')

    extract_dir = './images/imagenes_referencia_reconocimiento_facial'

    zip_path, _ = urllib.request.urlretrieve(url)

    with zipfile.ZipFile(zip_path, "r") as f:
        f.extractall(extract_dir)



# Detectar si se dispone de GPU cuda
# ==============================================================================
import torch

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print(F'Running on device: {device}')


# Crear diccionario de referencia para cada persona
# ==============================================================================
dic_referencias = crear_diccionario_referencias(
                    folder_path    = './images/imagenes_referencia_reconocimiento_facial',
                    min_face_size  = 40,
                    min_confidence = 0.9,
                    device         = device,
                    verbose        = True )


# Reconocimiento en imágenes
# ==============================================================================
# Identificar las personas en la imagen
fig, ax = plt.subplots(figsize=(12, 7))
imagen = Image.open('Fotos/imagen_2.jpg')

pipeline_deteccion_imagen(
    imagen = imagen,
    dic_referencia        = dic_referencias,
    min_face_size         = 20,
    thresholds            = [0.6, 0.7, 0.7],
    min_confidence        = 0.5,
    threshold_similaridad = 0.6,
    device                = device,
    ax                    = ax,
    verbose               = False )


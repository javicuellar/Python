from PIL import Image


def Imagen_pdf(fichero, output):
    imagenes = []
    
    for fich in fichero:
        im = Image.open(fich)
        im = im.convert('RGB')
        imagenes.append(im)

    imagenes[0].save(output, save_all=True, append_images=imagenes[1:])


#  Lista imagenes, fichero salida pdf
Imagen_pdf(['06_StarWars_Negro.jpg', '06_StarWars_Blanco.jpg', '06_Mercado.jpeg'], '06_Imagen_a_pdf.pdf')

import pyexiv2



#   Funcion que devuelve en pantalla la informacion exif
def Metadatos(archivo):
    print("Analizando foto ->  ", archivo, "\n")
    
    imagen = pyexiv2.Image(archivo)
    # admite caracteres Unicode
    
    # img = Image(path, encoding='utf-8')
    # img = Image(path, encoding='ISO-8859-1')

    data = imagen.read_exif()
    imagen.close()
    
    # Se puede abrir también con With
    with pyexiv2.Image(archivo) as imagen:
        print("Comentarios: ", imagen.read_comment())
        print("Tamaño: ", imagen.read_icc(), "bytes")
        print("Raw_xmp: ", imagen.read_raw_xmp())
        print("Thumbnail: ", imagen.read_thumbnail(), "bytes")

        print(" --------------- EXIF --------------------------")
        for clave, valor in imagen.read_exif().items():
                print(f"{clave}  --> {valor}")
    
        print(" --------------- IPTC --------------------------")
        
        for clave, valor in imagen.read_iptc().items():
                print(f"{clave}  --> {valor}")

        print(" ---------------- XMP -------------------------")
        
        for clave, valor in imagen.read_xmp().items():
                print(f"{clave}  --> {valor}")

    print("********************************************\n")


#  Función para modificar metadatos
def Modificar_metadatos(archivo):
    img = pyexiv2.Image(archivo)

    # Prepare the XMP data you want to modify
    dict1 = {'Xmp.xmp.CreateDate': '2019-06-23T19:45:17.834',   # Assign a value to a tag. This will overwrite its original value, or add it if it doesn't exist
             'Xmp.xmp.Rating': None}                            # Assign None to delete the tag
    img.modify_xmp(dict1)
    dict2 = img.read_xmp()       # Check the result
    print(dict2['Xmp.xmp.CreateDate'])
    #  mostrará ->  '2019-06-23T19:45:17.834'        # This tag has been modified
    print(dict2['Xmp.xmp.Rating'])
    #  mostrará ->  KeyError: 'Xmp.xmp.Rating'       # This tag has been deleted

    #  algunos metadatos no pueden ser modificados, como:  img.modify_exif({'Exif.Photo.MakerNote': 'Hello'})

    #  se puede usar clear para borrar todos los metadatos:  img.clear_exif()

    img.close()


#  Función para modificar el comentario
def Modificar_comentario(archivo):
    img = pyexiv2.Image(archivo)

    print("Comentario inicial: ", img.read_comment())
    
    img.modify_comment('Hello World!   \n你好！\n')
    print("Comentario modif.: ", img.read_comment())

    #  Borrar comentario
    img.clear_comment()
    print("Comentario borrado: ", img.read_comment())


#  Función para copiar metadatos de una foto en otra
def Copiar_metadatos(archivo):
    with pyexiv2.Image(archivo) as img1:
        with pyexiv2.Image(r'.\Fotos_Cara\StarWars.jpg') as img2:
            img1.copy_to_another_image(img2, exif=True, iptc=True, xmp=True, comment=False, icc=False, thumbnail=False)


def Copiar_metadatos_raw_xmp(archivo):
    img1 = pyexiv2.Image(archivo)
    img2 = pyexiv2.Image(r'.\Fotos_Cara\Paco.jpg')
    dict2 = img2.read_raw_xmp()

    img1.modify_raw_xmp(dict2)

    img1.close()
    img2.close()




if __name__ == "__main__":
    for i in range(0,6):
        foto = ".\Fotos\\foto  (" + str(i) + ")" + ".jpg"
        Metadatos(foto)
    
    #  Pruebas modificación fotos: poner marca reconocimiento facial, en read_raw_xmp()
    foto = r'.\Fotos_Cara\Paco.jpg'
    Metadatos(foto)
    
    foto = r'.\Fotos_Cara\PacoSI.jpg'
    Copiar_metadatos_raw_xmp(foto)
    Metadatos(foto)

    foto = r'.\Fotos_Cara\PacoNo.jpg'
    Metadatos(foto)

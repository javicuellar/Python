import exiftool

#  IMPORTANTE - Necesita tener instalado EXIFTOOL.EXE


#   Funcion que devuelve en pantalla la informacion exif
def Meta(archivo):
    with exiftool.ExifToolHelper() as et:
        for imagen in et.get_metadata(archivo):
            for clave, valor in imagen.items():
                print(f"Dict: {clave} = {valor}")



if __name__ == "__main__":
    for i in range(1,7):
        foto = "..\Fotos\\foto (" + str(i) + ")" + ".jpg"
        print("Analizando foto ->  ", foto)
        print("---------------------------------------------")
        Meta(foto)
        print("********************************************\n")

from pytube import YouTube


def descargar_video(link):
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()

    try:
        yt.download()
    except:
        print("Ha habido un problema con la descarga.")
    
    print("Descarga realizada correctamente.")


link = input("l descargar: ")

#  Descargamos el video
descargar_video(link)
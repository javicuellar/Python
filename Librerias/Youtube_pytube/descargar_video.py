from pytube import YouTube


def descargar_video(link):
    from pytube.innertube import _default_clients
    _default_clients["ANDROID_MUSIC"] = _default_clients["WEB"]
    
    yt = YouTube(link)
    print(" -- Información video Youtube  --")
    print("Título: ", yt.title)
    print("Descripción: ", yt.description)
    print("Tamaño:  ", yt.length // 60, "min.", yt.length % 60, "seg.")
    print("Metadata: ", yt.metadata)
    print("Fecha publicación:  ", yt.publish_date)
    print("Puntuación:  ", yt.rating)
    print("Se ha visto ", yt.views, " veces.")
    
    ytStream = yt.streams.get_highest_resolution()

    try:
        ytStream.download(skip_existing=True)
    except:
        print("Ha habido un problema con la descarga.")
    
    print("Descarga realizada correctamente.")



link = input("Video a descargar: ")

#  Descargamos el video
descargar_video(link)

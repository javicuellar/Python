from pytube import YouTube


def descargar_video_audio(link):
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
    
    try:
        ytStream = yt.streams.get_highest_resolution()
        ytStream.download(skip_existing=True)
    except:
        print("Ha habido un problema con la descarga.")
    
    print("Descarga video realizada correctamente.")

    # Descarga del audio
    audio_stream = yt.streams.filter(only_audio=True).first()

    try:
        audio_stream.download()
    except:
        print("Ha habido un problema con la descarga.")
    
    print("Descarga audio realizada correctamente.")





link = input("Video a descargar: ")

#  Descargamos el video
descargar_video_audio(link)

import os, re
from themoviedb import TMDb
from Herramientas.variables import TMDB_API_KEY 



tmdb = TMDb(key=TMDB_API_KEY, language="es-ES", region="ES")

# Carpeta donde están los archivos de películas
carpeta_peliculas = '//NAS\\video\\Descargas'


def buscar_pelicula(nombre_archivo):
    """Busca una película en TMDB por nombre."""
    patron = r'$$(\d{4})$$|\b(\d{4})\b'     # Patrón para buscar años entre paréntesis o no
    nombre_archivo_sin_año = re.sub(patron, '', nombre_archivo)

    try:
        movies = tmdb.search().movies(nombre_archivo_sin_año)
        movie_id = movies[0].id   # Obtener el primer resultado
        return tmdb.movie(movie_id).details(append_to_response="credits,external_ids, images, videos")
    except Exception as e:
        print(f"Error al buscar {nombre_archivo}: {e}")
        return None


def procesar_archivos():
    """Procesa los archivos de la carpeta y busca las películas en TMDB."""
    for nombre_archivo in os.listdir(carpeta_peliculas):
        if os.path.isfile(os.path.join(carpeta_peliculas, nombre_archivo)):
            nombre_pelicula = os.path.splitext(nombre_archivo)[0] # Quita la extensión del archivo
            print(f"Buscando: {nombre_pelicula}")
            pelicula = buscar_pelicula(nombre_pelicula)
            if pelicula:
                print(f"Encontrada: {pelicula.title}")
                # Aquí puedes hacer lo que quieras con la información de la película
            else:
                print(f"No encontrada: {nombre_pelicula}")
                break


if __name__ == "__main__":
    procesar_archivos()
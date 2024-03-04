##  Python - Busca ficheros duplicados


### Uso de las siguientes librerías

* **hashlib** - Uso de md5 para obtener el hash del fichero
* **multiprocessing** - Para obtener el número de cores (cpu_count)
* **os** - Usa walk para obtener los directorios y ficheros de una ruta
* **os.path** - Para obtener el tamaño del fichero y verificar si existe (exists, getsize)
* **queue** - Para crear una cola de tareas
* **sys** - Para el tratamiento de los argumentos de ejecución del script, los parámetros (argv)
* **threading** - Usa para determinar el hijo en ejecución (current_thread), para crear un recurso a bloquear (Lock) para evitar su uso simultáneo por varios hilos
* **logging** - ¿?

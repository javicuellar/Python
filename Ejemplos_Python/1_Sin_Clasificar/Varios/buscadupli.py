#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from hashlib import md5
from multiprocessing import cpu_count
from os import walk
from os.path import exists, getsize
try:
    from Queue import Queue
except ImportError:
    from queue import Queue
from sys import argv
from threading import current_thread, Lock, Thread
import logging
logging.basicConfig(filename="search.log", level=logging.DEBUG)
# A partir de este tamaño crítico los archivos se leen
# por partes.
CRITIC_SIZE = 100000000  # 100 MB.
# Archivos máx grandes serán ignorados.
MAX_SIZE = 120000000  # 120 MB.
def safe_print(lock, *args):
    """
    Prevents multiple threads writing at the same time.
    """
    lock.acquire()
    print(*args)
    lock.release()
def get_file_md5(f, size):
    h = md5()
    split = size > CRITIC_SIZE
    if split:
        logging.info(
            "{0} will be splitted ({1} bytes).".format(f.name, size))
    while True:
        # Leer por partes a partir de un tamaño crítico.
        token = f.read(CRITIC_SIZE if split else -1)
        if token:
            h.update(token)
        else:
            break
    return h.hexdigest()
def worker(q, lock, files):
    while True:
        path, filename = q.get()
        if path is not None:
            process_file(path, filename, files, lock)
        q.task_done()
        if path is None:
            break
    safe_print(lock, current_thread().name, "exited.")
def process_file(path, filename, files, lock):
    filepath = "{0}/{1}".format(path, filename)
    try:
        size = getsize(filepath)
    except OSError as e:
        logging.error(
            "getsize() failed for {0}. {1}.".format(filepath, e))
        # Omit.
        size = MAX_SIZE + 1
    # Ignorar archivos de gran tamaño.
    if size > MAX_SIZE:
        safe_print(lock, filepath, "omitted.")
        return 0
    f = None
    try:
        f = open(filepath, "rb")
    except IOError as e:
        logging.error("open() failed for {0}. {1}.".format(filepath, e))
    else:
        # Obtener el hash MD5 del contenido y
        # almacenarlo en el diccionario.
        h = get_file_md5(f, size)
        files.append((filepath, h))
    finally:
        if f is not None:
            f.close()
def main():
    if len(argv) < 2:
        return
    
    begin_path = argv[1]
    
    if not exists(begin_path):
        print("Invalid path.")
        return
    
    files = []   # Archivos procesados.
    q = Queue()
    # Para evitar la superposición en la impresión
    # de textos.
    lock = Lock()
    cores = cpu_count()
    threads = []
    logging.info("{} cores available.".format(cores))
    
    # Lanzar tantos hilos como núcleos disponibles.
    for i in range(cores):
        t = Thread(target=worker, args=(q, lock, files))
        t.start()
        threads.append(t)
    
    try:
        # Recorrer el árbol de directorios.
        for path, dirnames, filenames in walk(begin_path):
            print(path)
            for filename in filenames:
                q.put((path, filename))
    except KeyboardInterrupt:
        # Detener el proceso.
        logging.info("Manually stopped.")
    
    # Terminar hilos.
    for i in range(cores):
        q.put((None, None))
    
    # Esperar a que finalice el procesamiento de cada hilo.
    print("Waiting for threads...")
    for t in threads:
        t.join()
    
    scanned = len(files)
    print(scanned, "processed files.")
    
    filepath = [None, None]
    filehash = [None, None]
    output = open("output.txt", "a")
    # Cantidad de archivos duplicados o multiplicados.
    count = 0
    
    print("Writing results...")
    
    while files:
        filepath[0], filehash[0] = files[0]
        
        # Nombre del archivo sin la ruta.
        filename = filepath[0][filepath[0].rfind("/") + 1:]
        matches = 0
        matches_path = []
        
        limit = len(files)
        i = 0
        while i < limit:
            filepath[1], filehash[1] = files[i]
            # Determinar si coincide el nombre.
            name_match = filepath[1].endswith(filename)
            # Verificación del hash.
            if filehash[0] == filehash[1] and name_match:
                matches += 1
                matches_path.append(filepath[1])
                del files[i]
                limit -= 1
            else:
                i += 1
        
        if matches > 1:
            # Escribir resultados a output.txt.
            output.write(u"{0} found {1} times {2}.\n".format(
                         filename, matches, matches_path))
            count += 1
    
    output.close()
    print(count, "multiplied files.")
if __name__ == "__main__":
    main()
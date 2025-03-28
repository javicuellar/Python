import os
import hashlib



def hash_file(filename):
    h = hashlib.md5()
    # Open,close, read file and calculate MD5 on its contents 
    with open(filename, "rb") as file:
        while chunk := file.read(8192):
            h.update(chunk)
    return h.hexdigest()


def find_duplicates(path):
    hashes = {}
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            file_hash = hash_file(full_path)
            if file_hash in hashes:
                print(f"Se encontraron duplicados: {full_path} = {hashes[file_hash]}")
                delete = input(f"¿Desea eliminar el archivo duplicado {full_path}? (s/n): ").strip().lower()
                if delete == "s":
                    os.remove(full_path)
                    print(f"Archivo eliminado: {full_path}")
                else:
                    print(f"Archivo conservado: {full_path}")
            else:
                hashes[file_hash] = full_path



source = "C:\\Users\javic\Downloads\Archivos"
find_duplicates(source)


'''
archivo = "C:\\Users\javic\Downloads\Archivos\prueba.pdf"
print(hash_file(archivo))
archivo = "C:\\Users\javic\Downloads\Archivos\\foto.jpg"
print(hash_file(archivo))
archivo = "C:\\Users\javic\Downloads\Archivos\\foto2.jpg"
print(hash_file(archivo))
'''
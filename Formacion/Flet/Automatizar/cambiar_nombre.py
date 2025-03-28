import os



def cambiar_nombre(directorio, opcion, valor):
    """
    Cambia el nombre de los archivos en el directorio especificado.

    Args:
        directorio:  Ruta del directorio donde se encuentran los archivos.
        opcion:  Opción de renombrado ('cambiar' para cambiar una palabra, 'prefijo' para agregar un prefijo)
        valor:  La palabra a cambiar o el prefijo a agregar.
    """

    for nombre_archivo in os.listdir(directorio):
        ruta_archivo = os.path.join(directorio, nombre_archivo)     # c://archivos + /archivo1.txt
        if os.path.isfile(ruta_archivo):
            nuevo_nombre = ""
            if opcion == 'cambiar':
                nuevo_nombre = nombre_archivo.replace(valor[0], valor[1])
            elif opcion == 'prefijo':
                nuevo_nombre = f"{valor[0]}_{nombre_archivo}" if isinstance(valor, list) else f"{valor}_{nombre_archivo}"
            else:
                print("Opción no válida. Usa 'cambiar' o 'prefijo'")
                return
            
            nueva_ruta = os.path.join(directorio, nuevo_nombre)
            os.rename(ruta_archivo, nueva_ruta)
            print(f"Renombrado: {nombre_archivo} a {nuevo_nombre}")




if __name__ == "__main__":
    ruta = "C:\\Users\\javic\\Downloads\\Archivos\\renombrar"
    # cambiar_nombre(ruta, 'prefijo', valor=["2024-12-05", ""])

    # cambiar_nombre(ruta, 'prefijo', valor="2024-12-05")

    cambiar_nombre(ruta, 'cambiar', valor=["2024-12-05_", ""])

def load_file(file_name: str) -> dict:
    """
    Carga datos de un archivo CSV con el formato 'llave, Type1, Type2' y devuelve un diccionario.

    Args:
    - file_name (str): El nombre del archivo CSV a cargar.

    Returns:
    - dict: Un diccionario de diccionarios. Un diccionario donde las llaves son la primera columna del 
            archivo CSV y los valores son diccionarios con claves 'Type1' y 'Type2', representando la 
            segunda y tercera columna respectivamente. Si no hay valores en la tercera columna, 
            se asigna 'N/A' a 'Type2'.
    """
    dictionary = {}
    file = open(file_name, "r")
    title = file.readline()

    line = file.readline()
    while len(line) > 0:
        data = line.split(",")
        pkey = data[0]
        record = {}
        
        if len(data) > 2:
            record['Type1'] = data[1]
            record['Type2'] = data[2][:-1]
        else:
            record['Type1'] = data[1][:-1]
            record['Type2'] = 'N/A'

        dictionary[pkey] = record
        line = file.readline()

    file.close()
    return dictionary

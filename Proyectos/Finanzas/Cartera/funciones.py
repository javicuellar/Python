caracterEliminar = '. €+EURSD'

#  Defino función para transformar los números de la hoja con puntos y coma y símbolo euro
def ExtraerNum(texto):
    if texto == '':
        valor = 0
    else:
        for x in range(0, len(caracterEliminar)):
            texto = texto.replace(caracterEliminar[x], '')
        
        valor = float(texto.replace(",", "."))
    return valor

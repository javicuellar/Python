# Leer cuántas millas tiene la longitud dada y referenciarlo con la variable millas
# Leer cuántos pies tiene la longitud dada y referenciarlo con la variable pies
# Leer cuántas pulgadas tiene la longitud dada y referenciarlo con la variable pulgadas
 
#  Calcular metros = 1609.344 * millas + 0.3048 * pies + 0.0254 * pulgadas

print ("Convierte medidas inglesas a sistema metrico")

millas = float(input('Cuantas millas?: '))
pies = float(input('Y cuantos pies?: '))
pulgadas = float(input("Y cuantas pulgadas?: "))

metros = 1609.344 * millas + 0.3048 * pies + 0.0254 * pulgadas
print ("La longitud es de ", metros, " metros")

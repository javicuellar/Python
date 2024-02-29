from zipfile import ZipFile

# Comprimir fichero "text.txt" a "prueba.zip" 
# al realizar con with se controlan las excepciones y siempre se cierra el fichero
def comprimir(fichero, ficherozip="prueba.zip"):
	with ZipFile(ficherozip, 'w') as myzip:
		myzip.write(fichero)

#    Equivale a:
# myzip = ZipFile('prueba.zip', 'w')
# myzip.write('text.txt')
# myzip.cloe()


# Para extraer el fichero:
def descomprimir(ficherozip="prueba.zip"):
	with ZipFile(ficherozip) as myzip:
		myzip.extractall()


#   ----------------------------------------------
ficherozip = "prueba.zip"
fichero = "text.txt"

comprimir(fichero)
comprimir(fichero, ficherozip)
from zipfile import ZipFile

# Comprimir fichero "eggs.txt" a "spam.zip" 
# al realizar con with se controlan las excepciones y siempre se cierra el fichero
#

'''
with ZipFile('spam.zip', 'w') as myzip:
	myzip.write('eggs.txt')
# Equivale a:
#
# myzip = ZipFile('spam.zip', 'w')
# myzip.write('eggs.txt')
# myzip.cloe()
'''

# Para extraer el fichero:
with ZipFile('spam.zip') as myzip:
	myzip.extractall()


from zipfile import ZipFile

with ZipFile('spam.zip', 'w') as myzip:
	myzip.write('eggs.txt')

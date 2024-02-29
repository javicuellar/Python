import csv

doc = open('d:\\python\\Ficheros\\fichero.csv', 'r')

doc_csv = csv.reader(doc) 		# variable declarada por convencion entre programadores

for l in doc_csv:
	print (l)

doc.close()                    		
 
import csv

doc = open('d:\\python\\Ficheros\\fichero.csv', 'w')

doc_csv_w = csv.writer(doc) 	# variable declarada por convencion entre programadores

lista = [["Pedro", 99586],['Javi',98],['mama', 7]]

for x in lista:
	doc_csv_w.writerow(x)         

doc.close()                    		

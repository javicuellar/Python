#  1) Ficheros: apertura, lectura, escritura (input/output)
# -----------------------------------------------------
# Generates a list of squares of the numbers 1 - 10
my_list = [i**2 for i in range(1,11)]

#  Apertura fichero en modo w, escritura, r+ para lectura
f = open("output.txt", "w")

#  Escritura del fichero elemento a elemento, en bucle. 
for item in my_list:
    # Se utiliza '\n' para saltar a la siguiente linea
    # Antes de guardarlo, se convierte a tipo string
    f.write(str(item) + "\n")

#  Siempre hay que cerrar el fichero
f.close()


#  2) Ficheros: añadir registros
# -----------------------------------------------------------
my_list = [i*3 for i in range(1,11)]
#  Abrimos el fichero anterio en modo añadir registros
my_file = open("output.txt", "a")
for item in my_list:				
    my_file.write(str(item)+'\n')

my_file.close()


#  3) Ficheros: Lectura de registros
# -------------------------------------------------------------
my_file = open('output.txt','r')
# imprime todas los numeros (sin bucle de lectura para linea)
print(my_file.read())
my_file.close()


#  3) Ficheros: Lectura de fichero por línea, leyendo el caracter salto de línea
# --------------------------------------------------------------
# imprime cada linea, dejando una linea en blanco entre ellas
my_file = open('text.txt','r')
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
my_file.close()


#  4) Ficheros Uso de fichero de lectrua y escritura al mismo tiempo
# ----------------------------------------------------------------
# Open the file for reading
read_file = open("text.txt", "r")
# Use a second file handler to open the file for writing
write_file = open("text.txt", "w")
# lectura del fichero
print(read_file.read())
# Write to the file
write_file.write("Not closing files is VERY BAD.")
write_file.close()
read_file.close()

# --> error "ValueError: I/O operation on closed file"  -> lectura de fichero tras cerrarlo
# print(read_file.read())


#  5) Uso de ficheros usando with y as, no hace falta cerrar el fichero
#--------------------------------------------------------------------
with open("text.txt", "w") as textfile:
	textfile.write("Success!")

if textfile.closed:	      # devuelve True si el fichero esta cerrado
    print('cerrar.')
else:
    textfile.close()
    print('ahora esta cerrado.')

print(textfile.closed)				# True


#  6) Lectura de fichero y lo saca por pantalla. Con la coma, lo saca en la misma linea
#--------------------------------------------------------------------
f = open('output.txt','r')
for linea in f:
	print(linea,)		# para cada linea del fichero la imprime y con la coma, no salta una linea
f.close()
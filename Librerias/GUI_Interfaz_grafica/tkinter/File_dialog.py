# Ejemplos de uso de la librería filedialog de TKINTER
from tkinter import *
from tkinter import filedialog



raiz = Tk()

# función para abrir archivo
def abrirArchivo():
     # En archivo se guarda el path del archivo seleccionado
     # usando initaldir se define desde que carpeta se va a abrir el fichero
     # usando filetypes se ofrece en la barra opciones de tipos de archivos
    archivo = filedialog.askopenfilename(title="abrir", initialdir="./Ficheros", filetypes=(("Archivos de Python", "*.py"), ("Archivos de Texto", "*.txt"), ("Archivos pdf", "*.pdf"), ("Todos los archivos", "*.*")))
    print(archivo)


Button(raiz, text="Abrir Archivo", command=abrirArchivo).pack()


raiz.mainloop()
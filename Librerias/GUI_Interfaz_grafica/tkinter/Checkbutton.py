# Ejemplo de uso del Checkbutton
from tkinter import *


raiz = Tk()

raiz.geometry("700x880+250+1")    # para dar tamaño y situar la ventana
raiz.title("Bienes Raíces")

miImagen = PhotoImage(file="./Ficheros/bienes_raices.png")     # debe ser formato png, no me funciona con jpg
Label(raiz, image=miImagen).pack()

miFrame = Frame(raiz)
miFrame.pack()

Label(miFrame, text="Elige tu búsqueda: ").pack()

# variables definidas para los checkbotones
Departamento = IntVar()
Casa = IntVar()
Local = IntVar()

# función definida para manejar la pulsación del checkbotón, conectada con command.
def opcionElegida():
    miOpcion = ""
    if Departamento.get() == 1:
        miOpcion += "Departamento\n"
    if Casa.get() == 1:
        miOpcion += "Casa\n"
    if Local.get() == 1:
        miOpcion += "Local\n"

    etiqueta_abajo.config(text=miOpcion)

# definimos los checkbutton en el frame, ponemos texto, asociamos variable y valores 1 pulsado 0 sino.
Checkbutton(miFrame, text="Departamento", onvalue=1, offvalue=0, variable=Departamento, command=opcionElegida).pack()
Checkbutton(miFrame, text="Casa", onvalue=1, offvalue=0, variable=Casa, command=opcionElegida).pack()
Checkbutton(miFrame, text="Local", onvalue=1, offvalue=0, variable=Local, command=opcionElegida).pack()

# definimos etiqueta para manejar el uso de las variables, como ejemplo asignamos en los chehkbutton la función opcionElegida y como salida hemos usado la etiqueta que nos lo muestra.
etiqueta_abajo = Label(miFrame)
etiqueta_abajo.pack()

raiz.mainloop()
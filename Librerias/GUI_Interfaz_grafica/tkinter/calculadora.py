from tkinter import *


raiz = Tk()
raiz.title("Calculadora")

miFrame = Frame(raiz)
miFrame.pack()

#-------------------------------------------------------------------- Visor (fila 0)
varVisor = StringVar()          
# definimos variable string para el visor y la conectamos incluyendo la opción textvariable
miVisor = Entry(miFrame, textvariable=varVisor)
# definimos el visor con un grid para introducir texto, 
# en la posición fila 0 columna 0, con un tamaño de 4, columspan
miVisor.grid(row=0, column=0, columnspan=4)
miVisor.config(bg="gray", fg="white", justify="right")

#-------------------------------------------------------------------- Funciones de botones
def funboton7():
    varVisor.set("7")

def funboton8():
    varVisor.set("8")

def funboton9():
    varVisor.set("9")

def funbotondiv():
    varVisor.set("/")

#-------------------------------------------------------------------- Botones
#-------------------------------------------------------------------- row 1
# creamos el boton 7, texto 7, situado en la fila 1, columna 0
# como quedan pequeños vamos a añadir un ancho, width
# hemos definido una función para el boton, para conectar añadimos "command"
boton7 = Button(miFrame, text="7", width=4, command=funboton7)
boton7.grid(row=1, column=0)
# idem con el resto
boton8 = Button(miFrame, text="8", width=4, command=funboton8)
boton8.grid(row=1, column=1)
boton9 = Button(miFrame, text="9", width=4, command=funboton9)
boton9.grid(row=1, column=2)
botondiv = Button(miFrame, text="/", width=4, command=funbotondiv)
botondiv.grid(row=1, column=3)


raiz.mainloop()
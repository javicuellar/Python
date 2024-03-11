from tkinter import *


raiz = Tk()
raiz.title("Calculadora")

miFrame = Frame(raiz)
miFrame.pack()

#-------------------------------------------------------------------- Visor (fila 0)
varVisor = StringVar()          
miVisor = Entry(miFrame, textvariable=varVisor, font = "Arial 18")
miVisor.grid(row=0, column=0, columnspan=4)   # ipadx=70, ipady=20)
miVisor.config(bg="gray", fg="white", justify="right")   # width=43

#-------------------------------------------------------------------- Funciones de botones
# modificamos el código de la función para coger lo que está en pantalla
# y añadir el caracter pulsado

borrar = False

def funboton1():
    # es necesario declarar borrar global para estar disponible en las funciones
    global borrar                        
    if borrar:
        varVisor.set("1")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "1")    # get() coge lo que hay y lo concatena con 1

def funboton2():
    global borrar
    if borrar:
        varVisor.set("2")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "2")


def funboton3():
    global borrar
    if borrar:
        varVisor.set("3")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "3")

def funboton4():
    global borrar
    if borrar:
        varVisor.set("4")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "4")

def funboton5():
    global borrar
    if borrar:
        varVisor.set("5")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "5")

def funboton6():
    global borrar
    if borrar:
        varVisor.set("6")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "6")

def funboton7():
    global borrar
    if borrar:
        varVisor.set("7")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "7")

def funboton8():
    global borrar
    if borrar:
        varVisor.set("8")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "8")

def funboton9():
    global borrar
    if borrar:
        varVisor.set("9")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "9")

def funboton0():
    global borrar
    if borrar:
        varVisor.set("0")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "0")

def funbotondiv():
    varVisor.set(varVisor.get() + "/")

def funbotonmult():
    varVisor.set(varVisor.get() + "*")

def funbotonres():
    varVisor.set(varVisor.get() + "-")

def funbotonsum():
    varVisor.set(varVisor.get() + "+")

def funbotonpunto():
    varVisor.set(varVisor.get() + ".")

def funbotonigual():
    global borrar
    try:
        varVisor.set(eval(varVisor.get()))      # Esto se ejecutará si va bien
    except ZeroDivisionError:
        varVisor.set("Error div zero")          # Esto se ejecuta si da error
    finally:
        borrar = True                           # Esto queremos que se ejecute siempre

#-------------------------------------------------------------------- Botones
#-------------------------------------------------------------------- row 1 (fila 1)
boton7 = Button(miFrame, text="7", width=8, height=3, command=funboton7)
boton7.grid(row=1, column=0)
boton8 = Button(miFrame, text="8", width=8, height=3, command=funboton8)
boton8.grid(row=1, column=1)
boton9 = Button(miFrame, text="9", width=8, height=3, command=funboton9)
boton9.grid(row=1, column=2)
botondiv = Button(miFrame, text="/", width=8, height=3, command=funbotondiv)
botondiv.grid(row=1, column=3)

#-------------------------------------------------------------------- row 2 (fila 2)
boton4 = Button(miFrame, text="4", width=8, height=3, command=funboton4)
boton4.grid(row=2, column=0)
boton5 = Button(miFrame, text="5", width=8, height=3, command=funboton5)
boton5.grid(row=2, column=1)
boton6 = Button(miFrame, text="6", width=8, height=3, command=funboton6)
boton6.grid(row=2, column=2)
botonmult = Button(miFrame, text="*", width=8, height=3, command=funbotonmult)
botonmult.grid(row=2, column=3)

#-------------------------------------------------------------------- row 3 (fila 3)
boton1 = Button(miFrame, text="1", width=8, height=3, command=funboton1)
boton1.grid(row=3, column=0)
boton2 = Button(miFrame, text="2", width=8, height=3, command=funboton2)
boton2.grid(row=3, column=1)
boton3 = Button(miFrame, text="3", width=8, height=3, command=funboton3)
boton3.grid(row=3, column=2)
botonres = Button(miFrame, text="-", width=8, height=3, command=funbotonres)
botonres.grid(row=3, column=3)

#-------------------------------------------------------------------- row 4 (fila 4)
botonpunto = Button(miFrame, text=".", width=8, height=3, command=funbotonpunto)
botonpunto.grid(row=4, column=0)
boton0 = Button(miFrame, text="0", width=8, height=3, command=funboton0)
boton0.grid(row=4, column=1)
botonigual = Button(miFrame, text="=", width=8, height=3, command=funbotonigual)
botonigual.grid(row=4, column=2)
botonsum = Button(miFrame, text="+", width=8, height=3, command=funbotonsum)
botonsum.grid(row=4, column=3)


raiz.mainloop()
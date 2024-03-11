# Ejemplo de uso del Radiobutton
from tkinter import *


raiz = Tk()


raiz.geometry("500x200+250+100")    # para dar tamaño y situar la ventana
raiz.title("Bienes Raíces")

IntVariable = IntVar()
Label(raiz, text="Defina su búsqueda:\n").pack()     # usamos \n para saltar línea con radioboton

# creamos una función para que imprima el texto de nuestra elección: departamento, casa o local
# y lo asociamos al radioboton con el comando "command"
def ImprimirSeleccion():
    if IntVariable.get() == 1:
        print("Departamento")                   # se verá en la consola, no en la ventana
        etiqueta.config(text="Has elegido Departamento")    # la etiqueta se ve en la ventana
    elif IntVariable.get() == 2:
        print("Casa")
        etiqueta.config(text="Has elegido Casa")
    elif IntVariable.get() == 3:
        print("Local")
        etiqueta.config(text="Has elegido Local")

# creamos el radiobutton pulsado
Radioboton1 = Radiobutton(raiz, text="Departamento", variable=IntVariable, value=1, command=ImprimirSeleccion).pack()   
Radioboton2 = Radiobutton(raiz, text="Casa", variable=IntVariable, value=2, command=ImprimirSeleccion).pack() 
Radioboton3 = Radiobutton(raiz, text="Local", variable=IntVariable, value=3, command=ImprimirSeleccion).pack() 

etiqueta = Label(raiz)
etiqueta.pack()

raiz.mainloop()
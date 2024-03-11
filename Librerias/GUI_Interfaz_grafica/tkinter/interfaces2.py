# Práctica 2 con librería Tkinter
from tkinter import *



raiz = Tk()                                         # creación de la raiz o marco principal

miframe = Frame(raiz, width=1000, height=600)       # Definimos el frame de raiz, y su tamaño
miframe.pack()

miImagen = PhotoImage(file="./Ficheros/earth.gif")            # usamos una foto


# place es la distancia del marco, punto superior izquierda
Label(miframe, image=miImagen).place(x=100, y=100)  

# probamos el place 0,0, esquina superior izquierda
Label(miframe, image=miImagen).place(x=0, y=0) 

raiz.mainloop()  
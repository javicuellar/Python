# Práctica con librería Tkinter
from tkinter import *



raiz = Tk()                     # creación de la raiz o marco principal


raiz.title("Mi aplicación")     # pone título al marco principal
raiz.iconbitmap("./Ficheros/bing.ico")     # cambia el icono en el menú, parte superior izquierda
raiz.geometry("600x400")        # permite definir el tamaño de la ventana
raiz.resizable(0,0)             # bloqueamos cambiar el tamaño.
raiz.config(bg="blue")          # configura opciones como el background (fondo =bg) o azul

miframe = Frame()               # Definimos el frame
miframe.pack()                  # Empaqueta el frame para usarse en el raiz
miframe.config(bg="red")        # definimos el background rojo
# no vemos nada porque está dentro de la raiz, definimos un tamaño distinto.
miframe.config(bg="red",width="500",height="200")

# definimos una etiqueta, el texto, el fondo con tipo letra, el background...
mietiqueta = Label(miframe, text="esta es mi aplicación", font=("times new roman", 25), background="white")  
# mietiqueta.place(x=500, y=500)  # definimos situación
mietiqueta.pack()               # Empaqueta para usarla

raiz.mainloop()                 # lo que hace es estar funcionando eterno (while eterno), hasta que se cierra la ventana.
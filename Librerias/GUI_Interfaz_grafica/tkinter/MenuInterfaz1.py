# Código ejemplo para crear menús en ventanas tkinter
from tkinter import *



raiz = Tk()

miMenu = Menu(raiz)
raiz.config(menu=miMenu)

# creamos los opciones del menú 
miFile = Menu(miMenu, tearoff=0)        # tearoff = 0 se usa para eliminar una línea punteada inicial
miFile.add_command(label="New File")
miFile.add_command(label="New Window")
miFile.add_separator()
miFile.add_command(label="Open File...")
miFile.add_command(label="Open Editor")
miFile.add_command(label="Close File")
miFile.add_separator()
miFile.add_command(label="Exit")

miEdit = Menu(miMenu, tearoff=0)
miEdit.add_command(label="Undo")
miEdit.add_command(label="Redo")
miEdit.add_separator()
miEdit.add_command(label="Cut")
miEdit.add_command(label="Copy")
miEdit.add_command(label="Paste")

miHelp = Menu(miMenu, tearoff=0)
miHelp.add_command(label="Welcome")
miHelp.add_command(label="About")

# Una vez definidos los menús, usamos add_cascade para mostrarlos
miMenu.add_cascade(label="File", menu=miFile)
miMenu.add_cascade(label="Edit", menu=miEdit)
miMenu.add_cascade(label="Help", menu=miHelp)


raiz.mainloop()
# Creacción de ventanas emergentes en el menú y funciones a los menús creados.
from tkinter import *
from tkinter import messagebox     # para sacar ventanas de mensaje.



raiz = Tk()

miMenu = Menu(raiz)
raiz.config(menu=miMenu)


# Creamos funciones a ejecutar al pulsar las opciones
# Sub-opción About de HELP - Muestra ventana simple con título y mensaje.
def info():
    messagebox.showinfo("JAVI", "Versión 1.01\nFecha creación: 12/01/2022")
                #  Titulo  +  mensajes

# Sub-opción Close archivo de FILE - Muestra ventana de aviso con título y mensaje.
def aviso():
    messagebox.showwarning("Advertencia", "Este archivo no fue guardado")

# Sub-opción Exit de FILE - pregunta si quiere salir, si se pulsa si sale con función destroy()
def avisoSalir():
    respuesta = messagebox.askquestion("Cuidado", "¿Está seguro que quiere salir?")
    if respuesta == "yes":
        raiz.destroy()

# Sub-opción New File de FILE - pregunta si quiere abrir nuevo fichero usando opción OK o CANCEL
def nuevoArchivo():
    respuestaNuevo = messagebox.askokcancel("New File", "¿Desea abrir un nuevo fichero?")
    if respuestaNuevo == True:
        raiz.destroy()

# creamos los opciones del menú 
miFile = Menu(miMenu, tearoff=0)        # tearoff = 0 se usa para eliminar una línea punteada inicial
miFile.add_command(label="New File", command=nuevoArchivo)
miFile.add_command(label="New Window")
miFile.add_separator()
miFile.add_command(label="Open File...")
miFile.add_command(label="Open Editor")
miFile.add_command(label="Close File", command=aviso)
miFile.add_separator()
miFile.add_command(label="Exit", command=avisoSalir)

miEdit = Menu(miMenu, tearoff=0)
miEdit.add_command(label="Undo")
miEdit.add_command(label="Redo")
miEdit.add_separator()
miEdit.add_command(label="Cut")
miEdit.add_command(label="Copy")
miEdit.add_command(label="Paste")

miHelp = Menu(miMenu, tearoff=0)
miHelp.add_command(label="Welcome")
miHelp.add_command(label="About", command=info)      # conectada con función info

# Una vez definidos los menús, usamos add_cascade para mostrarlos
miMenu.add_cascade(label="File", menu=miFile)
miMenu.add_cascade(label="Edit", menu=miEdit)
miMenu.add_cascade(label="Help", menu=miHelp)

raiz.mainloop()
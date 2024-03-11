from tkinter import *
from tkinter import messagebox
import sqlite3



raiz = Tk()
raiz.title("Formulario de mi Base de Datos")
raiz.geometry("500x400")

miMenu = Menu(raiz)
raiz.config(menu=miMenu)

miFrame = Frame(raiz)
miFrame.pack()

# ---------------------------  funciones del menú  -------------------------------------------
def info():
    messagebox.showinfo("Mi interfaz de Base de Datos", "Versión 12/01/2022")

def aviso():
    messagebox.showwarning("Advertencia", "Este archivo no fue guardado")

def avisoCerrar():
    respuesta = messagebox.askquestion("Cuidado", "¿Está seguro de que quiere Cerrar?")
    if respuesta == "yes":
        raiz.destroy()

# ---------------------------  opciones del menú  -------------------------------------------
miDB = Menu(miMenu, tearoff=0)
miDB.add_command(label="Nuevo Registro")
miDB.add_command(label="Buscar Registro")
miDB.add_command(label="Cerrar")

miEdit = Menu(miMenu, tearoff=0)
miEdit.add_command(label="Modificar Registro")
miEdit.add_command(label="Eliminar Registro")

miHelp = Menu(miMenu, tearoff=0)
miHelp.add_command(label="About", command=info)

miMenu.add_cascade(label="File", menu=miDB)
miMenu.add_cascade(label="Edit", menu=miEdit)
miMenu.add_cascade(label="Help", menu=miHelp)

# ---------------------------  Commands Rows  -------------------------------------------
def codigobotonNuevo():
    pass
def codigobotonBuscar():
    pass
def codigobotonModificar():
    pass
def codigobotonEliminar():
    pass
def codigobotonLimpiar():
    pass
def codigobotonCerrar():
    pass

# ---------------------------  Row 1  -------------------------------------------
varCodigoID = StringVar()
EntryCodigoID = Entry(miFrame, textvariable=varCodigoID)
EntryCodigoID.grid(row=1, column=1, sticky=W, padx=10, pady=10)
labelCodigoID = Label(miFrame, text="CÓDIGOID:")
labelCodigoID.grid(row=1, column=0, sticky=W)
botonNuevo = Button(miFrame, text="Nuevo Registro", command=codigobotonNuevo, width=15)
botonNuevo.grid(row=1, column=2, sticky=W)

# ---------------------------  Row 2  -------------------------------------------
varNombre = StringVar()
EntryNombre = Entry(miFrame, textvariable=varNombre)
EntryNombre.grid(row=2, column=1, sticky=W, padx=10, pady=10)
labelNombre = Label(miFrame, text="NOMBRE:")
labelNombre.grid(row=2, column=0, sticky=W)
botonBuscar = Button(miFrame, text="Buscar Registro", command=codigobotonBuscar, width=15)
botonBuscar.grid(row=2, column=2, sticky=W)

# ---------------------------  Row 3  -------------------------------------------
varApellido = StringVar()
EntryApellido = Entry(miFrame, textvariable=varApellido)
EntryApellido.grid(row=3, column=1, sticky=W, padx=10, pady=10)
labelApellido = Label(miFrame, text="APELLIDO:")
labelApellido.grid(row=3, column=0, sticky=W)
botonModificar = Button(miFrame, text="Modificar Registro", command=codigobotonModificar, width=15)
botonModificar.grid(row=3, column=2, sticky=W)

# ---------------------------  Row 4  -------------------------------------------
varDireccion = StringVar()
EntryDireccion = Entry(miFrame, textvariable=varDireccion)
EntryDireccion.grid(row=4, column=1, sticky=W, padx=10, pady=10)
labelDireccion = Label(miFrame, text="DIRECCIÓN:")
labelDireccion.grid(row=4, column=0, sticky=W)
botonEliminar = Button(miFrame, text="Eliminar Registro", command=codigobotonEliminar, width=15)
botonEliminar.grid(row=4, column=2, sticky=W)

# ---------------------------  Row 5  -------------------------------------------
varTelefono = StringVar()
EntryTelefono = Entry(miFrame, textvariable=varTelefono)
EntryTelefono.grid(row=5, column=1, sticky=W, padx=10, pady=10)
labelTelefono = Label(miFrame, text="TELÉFONO:")
labelTelefono.grid(row=5, column=0, sticky=W)
botonLimpiar = Button(miFrame, text="Limpiar Registro", command=codigobotonLimpiar, width=15)
botonLimpiar.grid(row=5, column=2, sticky=W)

# ---------------------------  Row 6  -------------------------------------------
varEmail = StringVar()
EntryEmail = Entry(miFrame, textvariable=varEmail)
EntryEmail.grid(row=6, column=1, sticky=W, padx=10, pady=10)
labelEmail = Label(miFrame, text="EMAIL:")
labelEmail.grid(row=6, column=0, sticky=W)
botonCerrar = Button(miFrame, text="Cerrar", command=codigobotonCerrar, width=15)
botonCerrar.grid(row=6, column=2, sticky=W)

# ---------------------------  Row 7  -------------------------------------------
# para definir un campo texto con paginación en lugar de variable
TextComentarios = Text(miFrame, width=10, height=1)     # tipo texto en lugar de variable, entry
TextComentarios.grid(row=7, column=1, sticky=W, padx=10, pady=10, ipadx=30, ipady=60)
labelComentarios = Label(miFrame, text="COMENTARIOS:")
labelComentarios.grid(row=7, column=0, sticky=W)
ScrollbarComentarios = Button(miFrame, command=TextComentarios.yview)   # para el scroll
ScrollbarComentarios.grid(row=7, column=2, sticky=W)


raiz.mainloop()
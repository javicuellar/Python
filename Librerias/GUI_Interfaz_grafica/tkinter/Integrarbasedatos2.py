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



# ---------------------------  Funciones Generales  -------------------------------------------
def deleteEntries():
    EntryCodigoID.delete(0, 'end'), EntryNombre.delete(0, 'end'), EntryApellido.delete(0, 'end'), EntryDireccion.delete(0, 'end'), EntryTelefono.delete(0, 'end'), EntryEmail.delete(0, 'end'),
    TextComentarios.delete(1.0, END)
    

# ---------------------------  funciones del menú  -------------------------------------------
def info():
    messagebox.showinfo("Mi interfaz de Base de Datos", "Versión 12/01/2022")

def aviso():
    messagebox.showwarning("Advertencia", "Este archivo no fue guardado")

def avisoCerrar():
    respuesta = messagebox.askquestion("Cuidado", "¿Está seguro de que quiere Cerrar?")
    if respuesta == "yes":
        raiz.destroy()

# --------------------------  funciones de los botones  -------------------------------------
def codigobotonGuardar():
    conexion1 = sqlite3.connect("./Ficheros/base1.db")
    miCursor = conexion1.cursor()
    try:
        miCursor.execute("""
            CREATE TABLE USUARIOS (
                CODIGOID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50),
                APELLIDO VARCHAR(50),
                DIRECCION VARCHAR(50),
                TELEFONO VARCHAR(50),
                EMAIL VARCHAR(50),
                COMENTARIOS VARCHAR(500))
        """)
    except sqlite3.OperationalError:
        pass
    finally:
        datos = (varNombre.get(), varApellido.get(), varDireccion.get(), varTelefono.get(), varEmail.get(), TextComentarios.get(1.0, END))
        miCursor.execute('INSERT INTO USUARIOS VALUES (NULL, ?, ?, ?, ?, ?, ?)', datos)
        deleteEntries()
        conexion1.commit()
        conexion1.close()


def codigobotonBuscar():
    conexion1 = sqlite3.connect("./Ficheros/base1.db")
    miCursor = conexion1.cursor()

    Datos = [varCodigoID.get(), varNombre.get(), varApellido.get(), varDireccion.get(), varTelefono.get(),
    varEmail.get()]
    for valor in Datos:
        if valor != "":
            try:
                miCursor.execute("""SELECT * FROM USUARIOS WHERE (CODIGOID=(?) OR NOMBRE=(?) OR APELLIDO=(?) OR DIRECCION=(?) OR TELEFONO=(?) OR EMAIL=(?))""", (valor, valor, valor, valor, valor, valor))
                verRegistro = miCursor.fetchall()
                varCodigoID.set(verRegistro[0][0])
                varNombre.set(verRegistro[0][1])
                varApellido.set(verRegistro[0][2])
                varDireccion.set(verRegistro[0][3])
                varTelefono.set(verRegistro[0][4])
                varEmail.set(verRegistro[0][5])
                TextComentarios.delete(1.0, END)
                TextComentarios.insert(END, verRegistro[0][6])
                break
            except IndexError:
                deleteEntries()
                break
            except TypeError:
                deleteEntries()
                break


def codigobotonModificar():
    conexion1 = sqlite3.connect("./Ficheros/base1.db")
    miCursor = conexion1.cursor()

    Datos = [varCodigoID.get(), varNombre.get(), varApellido.get(), varDireccion.get(), varTelefono.get(),
    varEmail.get(), TextComentarios.get(1.0, END)]
    miCursor.execute("""UPDATE USUARIOS SET CODIGOID = ?, NOMBRE = ?, APELLIDO = ?, DIRECCION = ?, TELEFONO = ?, EMAIL = ?, COMENTARIOS = ? WHERE CODIGOID={}""".format(varCodigoID.get()), Datos)
    deleteEntries()
    conexion1.commit()
    conexion1.close()


def codigobotonEliminar():
    conexion1 = sqlite3.connect("./Ficheros/base1.db")
    miCursor = conexion1.cursor()

    miCursor.execute("""DELETE FROM USUARIOS WHERE CODIGOID={}""".format(varCodigoID.get()))
    deleteEntries()
    conexion1.commit()
    conexion1.close()


def codigobotonCerrar():
    raiz.destroy()



# ---------------------------  opciones del menú  -------------------------------------------
miDB = Menu(miMenu, tearoff=0)
miDB.add_command(label="Nuevo Registro", command=codigobotonGuardar)
miDB.add_command(label="Buscar Registro", command=codigobotonBuscar)
miDB.add_command(label="Cerrar", command=avisoCerrar)

miEdit = Menu(miMenu, tearoff=0)
miEdit.add_command(label="Modificar Registro", command=codigobotonModificar)
miEdit.add_command(label="Eliminar Registro", command=codigobotonEliminar)

miHelp = Menu(miMenu, tearoff=0)
miHelp.add_command(label="About", command=info)

miMenu.add_cascade(label="DB", menu=miDB)
miMenu.add_cascade(label="Edit", menu=miEdit)
miMenu.add_cascade(label="Help", menu=miHelp)

# ---------------------------  Row 1  -------------------------------------------
varCodigoID = StringVar()
EntryCodigoID = Entry(miFrame, textvariable=varCodigoID)
EntryCodigoID.grid(row=1, column=1, sticky=W, padx=10, pady=10)
labelCodigoID = Label(miFrame, text="CÓDIGOID:")
labelCodigoID.grid(row=1, column=0, sticky=W)
botonNuevo = Button(miFrame, text="Nuevo Registro", command=codigobotonGuardar, width=15)
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
botonLimpiar = Button(miFrame, text="Limpiar Registro", command=deleteEntries, width=15)
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
ScrollbarComentarios = Scrollbar(miFrame, command=TextComentarios.yview)   # para el scroll
ScrollbarComentarios.grid(row=7, column=2, sticky=W)

raiz.mainloop()
import sqlite3

con = sqlite3.connect('pythondb.db')


def selecttodo():
    query = 'SELECT * FROM tabla'
    resultado=con.execute(query)

    for i in resultado:
        print(i)
    return 'Regirstro leidos.'
    con.close()


def selectmutiplevar(edad):
    e= str(edad)

    query = 'SELECT * FROM tabla WHERE edad < ' + e
    print (query)
    resultado = con.execute(query)
    #resultado = con.fetchall()

    for i in resultado:
        print(i)

    return 'Regirstro leidos.'
    con.close()
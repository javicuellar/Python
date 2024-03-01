import sqlite3


con = sqlite3.connect('pythondb.db')


def insertaregistro():
    query = '''INSERT INTO tabla
                (nombre,tipo,edad)
         VALUES ('Pepe','normal',67)'''

    con.execute(query)
    con.commit()
    return 'Regirstro insertado.'
    con.close()

def insertavalores(nombre,tipo,edad):
    query = '''INSERT INTO tabla
                (nombre,tipo,edad)
         VALUES (?,?,?)'''

    con.execute(query,(nombre,tipo,edad))
    con.commit()
    return 'Regirstro insertado.'
    con.close()

def insertatupla(tupla):
    # funciona recibiendo una tupla (val1, val2,val3) y listas [val1,...]

    query = '''INSERT INTO tabla
                (nombre,tipo,edad)
         VALUES (?,?,?)'''

    con.execute(query,tupla)
    con.commit()
    return 'Regirstro insertado.'
    con.close()
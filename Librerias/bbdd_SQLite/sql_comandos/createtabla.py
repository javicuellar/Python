import sqlite3

con = sqlite3.connect('pythondb.db')        # conecta con la bd SQLite


def creatabla():
    query = '''CREATE TABLE tabla
            (id 		INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    		 nombre 	TEXT,
    		 tipo  		TEXT,
    		 edad 		INTEGER)'''

    con.execute(query)
    con.commit()		# para actualizar cambios
    con.close()		    # cerrar base de datos
    return 'tabla creada.'
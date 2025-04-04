import sqlite3



class TareasBD():
    def __init__(self):
        self.conexion = sqlite3.connect("tareas.db", check_same_thread=False)
        self.cursor = self.conexion.cursor()

    def ejecutar(self, sql, datos=None):
        if datos is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, datos)
        
    def actualizar(self):
        self.conexion.commit()

    def obtener_ultimoId(self):
        return self.cursor.lastrowid

    def obtener_todos(self):
        return self.cursor.fetchall()
    
    def close(self):
        self.conexion.close()


bd = TareasBD()

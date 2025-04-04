import sqlite3



class TareasBD():
    def __init__(self):
        self.conn = sqlite3.connect("tareas.db", check_same_thread=False)
        self.cur = self.conn.cursor()
        sql = "create table if not exists tareas (id integer primary key autoincrement, nombre text)"
        self.cur.execute(sql)
        self.conn.commit()

    def alta_tarea(self, nombre: str):
        self.cur.execute("insert into tareas (nombre) values (?)", (nombre), )
        self.conn.commit()
        return self.cur.lastrowid

    def obtener_tareas(self):
        self.cur.execute("select * from tareas")
        return self.cur.fetchall()

    def borrar_tarea(self, id: int):
        self.cur.execute("delete from tareas where id = ?", (id,))
        self.conn.commit()
    
    def actualizar_tarea(self, id: int, nombre: str):
        self.cur.execute("update tareas set nombre = ? where id = ?", (nombre, id))
        self.conn.commit()
    
    def close(self):
        self.conn.close()

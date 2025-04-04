# import sys
# import os

# Agregar el directorio padre al sys.path
# parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(parent_dir)

from tareas_bd import bd



class Tb_Lista_Tareas():
    def __init__(self):
        sql = '''CREATE TABLE if not exists lista_tareas 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    descripcion TEXT,
                    color TEXT
                 )'''
        bd.ejecutar(sql)
        bd.actualizar()

    def alta_lista_tareas(self, nombre: str, descripcion: str = '', color: str = ""):
        registro = (nombre, descripcion, color)
        sql = "insert into lista_tareas (nombre, descripcion, color) values (?,?,?)"
        bd.ejecutar(sql, registro, )
        bd.actualizar()
        return bd.obtener_ultimoId()

    def obtener_listas_tareas(self):
        bd.ejecutar("select * from lista_tareas")
        return bd.obtener_todos()

    def borrar_lista_tareas(self, id: int):
        bd.ejecutar("delete from lista_tareas where id = ?", (id,))
        bd.actualizar()
    
    def actualizar_lista_tareas(self, id: int, nombre: str, descripcion:str, color: str):
        sql = '''"UPDATE lista_tareas 
                     SET nombre = ?,
                         descripcion = ?,
                         color = ? 
                   WHERE id = ?"
              '''
        bd.ejecutar(sql, (nombre, descripcion, color, id))
        bd.actualizar()
    
    def close(self):
        bd.close()



TB_Lista_tareas = Tb_Lista_Tareas()
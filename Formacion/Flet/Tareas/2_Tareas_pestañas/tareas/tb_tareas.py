# import sys
# import os

# Agregar el directorio padre al sys.path
# parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(parent_dir)

from tareas_bd import bd



class Tb_Tareas():
    def __init__(self):
        sql = '''CREATE TABLE if not exists tareas 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    descripcion TEXT,
                    completado INT,
                    id_padre INT,
                    id_lista INT
                    )'''
        bd.ejecutar(sql)
        # Si existe la tabla, añadimos las siguientes columnas
        # bd.ejecutar("ALTER TABLE tareas ADD COLUMN descripcion TEXT")
        bd.actualizar()

    def alta_tarea(self, nombre: str, descripcion: str = '', 
                   completado: int = 0, id_padre: int = 0, id_lista: int = 0):
        registro = (nombre, descripcion, completado, id_padre, id_lista)
        sql = "insert into tareas (nombre, descripcion, completado, id_padre, id_lista) values (?,?,?,?,?)"
        bd.ejecutar(sql, registro, )
        bd.actualizar()
        return bd.obtener_ultimoId()

    def obtener_tareas(self):
        bd.ejecutar("select * from tareas")
        return bd.obtener_todos()

    def borrar_tarea(self, id: int):
        bd.ejecutar("delete from tareas where id = ?", (id,))
        bd.actualizar()
    
    def actualizar_tarea(self, id: int, nombre: str, descripcion: str = '', 
                   completado: int= 0, id_padre: int = 0, id_lista: int = 0):
        sql = '''UPDATE tareas 
                     SET nombre = ?,
                         descripcion = ?,
                         completado = ?,
                         id_padre = ?,
                         id_lista = ?
                   WHERE id = ?
              '''
        registro = (nombre, descripcion, completado, id_padre, id_lista, id)
        bd.ejecutar(sql, registro)
        bd.actualizar()
    
    def marcar_completada(self, id: int, completado: int = 1):
        sql = "UPDATE tareas SET completado = ? WHERE id = ?"
        registro = (completado, id)
        bd.ejecutar(sql, registro)
        bd.actualizar()
    
    def close(self):
        bd.close()



TB_Tareas = Tb_Tareas()
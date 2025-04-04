import flet as ft
from tareas.tareas_bd import TareasBD



tareasbd = TareasBD()


class TareasApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.tarea_nueva = ft.TextField(width=350, expand=True, on_submit=self.addClick)
        self.bt_añadir_tarea = ft.FloatingActionButton(icon= ft.icons.ADD, on_click=self.addClick)

        self.tareas = ft.Column()
        
        self.controls = [
            ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                   controls=[self.tarea_nueva,],
                ),
            self.tareas
            ]
        
        self.cargar_tareas()

    def cargar_tareas(self):
        for tarea in tareasbd.obtener_tareas():
            self.tareas.controls.append(Tarea(tarea[0], tarea[1], self.borrar_tarea))
    
    def addClick(self, e):
        self.tareas.controls.append(Tarea(None, self.tarea_nueva.value, self.borrar_tarea))
        self.tarea_nueva.value = ""
        self.update()

    def borrar_tarea(self, tarea):
        self.tareas.controls.remove(tarea)
        self.update()




class Tarea(ft.Column):
    def __init__(self, id, nombre, func_Borrado):
        super().__init__()
        self.nombre = nombre
        self.func_Borrado = func_Borrado
        if id:
            self.tareaId = id
        else:
            self.tareaId = tareasbd.alta_tarea((nombre, ))

        self.mostrarTarea = ft.Checkbox(label=self.nombre, value=False)
        self.mostrar = ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[self.mostrarTarea, 
                                        ft.Row(controls=[ft.IconButton(ft.icons.CREATE_OUTLINED, on_click=self.editClick),
                                                         ft.IconButton(ft.icons.DELETE_OUTLINED, on_click=self.deleteClick)])])
        
        self.editTarea = ft.TextField(width=350, expand=True, on_submit=self.saveClick)
        self.editar = ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, visible=False,
                            controls=[self.editTarea, ft.IconButton(ft.icons.DONE_OUTLINED, on_click=self.saveClick)])
        
        self.controls=[self.mostrar, self.editar]
    
    def editClick(self, e):
        self.mostrar.visible = False
        self.editar.visible = True
        self.editTarea.value = self.mostrarTarea.label
        self.update()

    def saveClick(self, e):
        self.mostrar.visible = True
        self.editar.visible = False
        self.mostrarTarea.label = self.editTarea.value
        self.nombre = self.editTarea.value
        tareasbd.actualizar_tarea(self.tareaId, self.nombre)
        self.update()

    def deleteClick(self, e):
        tareasbd.borrar_tarea(self.tareaId)
        self.func_Borrado(self)

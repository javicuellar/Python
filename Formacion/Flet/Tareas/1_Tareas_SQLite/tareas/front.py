import flet as ft
from tareas.tareas_bd import TareasBD



tareasbd = TareasBD()


class TareasApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.tarea_nueva = ft.TextField(width=350, expand=True, on_submit=self.addClick)
        self.bt_añadir_tarea = ft.FloatingActionButton(icon= ft.icons.ADD, on_click=self.addClick)

        self.tareas = ft.Column()
        
        self.pestañas = ft.Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[ft.Tab(text="all"), ft.Tab(text="active"), ft.Tab(text="completed")],
            )
        
        self.items_left = ft.Text("0 items left")

        self.width = 600
        
        self.controls = [
            ft.Row(
                [ft.Text(value="Todos", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                alignment=ft.MainAxisAlignment.CENTER,
                ),
            ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                   controls=[self.tarea_nueva,],
                ),
            ft.Column(
                spacing=25,
                controls=[
                    self.pestañas,
                    self.tareas,
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            self.items_left,
                            ft.OutlinedButton(
                                text="Clear completed", on_click=self.clear_clicked
                                ),
                            ],
                        ),
                    ],
                ),
            ]
        
        self.cargar_tareas()

    def cargar_tareas(self):
        for tarea in tareasbd.obtener_tareas():
            self.tareas.controls.append(Tarea(tarea[0], tarea[1], self.task_status_change, self.borrar_tarea))
    
    def addClick(self, e):
        self.tareas.controls.append(Tarea(None, self.tarea_nueva.value, self.task_status_change, self.borrar_tarea))
        self.tarea_nueva.value = ""
        self.update()

    def borrar_tarea(self, tarea):
        self.tareas.controls.remove(tarea)
        self.update()

    def clear_clicked(self, e):
        for task in self.tareas.controls[:]:
            if task.completed:
                self.task_delete(task)

    def before_update(self):
        status = self.pestañas.tabs[self.pestañas.selected_index].text
        count = 0
        for task in self.tareas.controls:
            task.visible = (
                status == "all"
                or (status == "active" and task.completed == False)
                or (status == "completed" and task.completed)
                )
            if not task.completed:
                count += 1
        self.items_left.value = f"{count} active item(s) left"

    def tabs_changed(self, e):
        self.update()

    def task_status_change(self, e):
        self.update()

    def add_clicked(self, e):
        task = Tarea(None, self.tarea_nueva.value, self.task_status_change, self.borrar_tarea)


class Tarea(ft.Column):
    def __init__(self, id, nombre, task_status_change, func_Borrado):
        super().__init__()
        self.nombre = nombre
        self.completed = False
        self.status_change = task_status_change
        self.func_Borrado = func_Borrado
        if id:
            self.tareaId = id
        else:
            self.tareaId = tareasbd.alta_tarea((nombre, ))

        self.mostrarTarea = ft.Checkbox(label=self.nombre, value=False, on_change=self.status_changed)
        self.mostrar = ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                              vertical_alignment=ft.CrossAxisAlignment.CENTER,
                              controls=[self.mostrarTarea, 
                                        ft.Row(spacing=0,
                                               controls=[ft.IconButton(ft.icons.CREATE_OUTLINED, 
                                                                       tooltip="Edit To-Do", 
                                                                       on_click=self.editClick),
                                                         ft.IconButton(ft.icons.DELETE_OUTLINED, 
                                                                       tooltip="Delete To-Do",
                                                                       on_click=self.deleteClick)])])
        
        self.editTarea = ft.TextField(width=350, expand=True, on_submit=self.saveClick)
        self.editar = ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, 
                             vertical_alignment=ft.CrossAxisAlignment.CENTER,
                             visible=False,
                             controls=[self.editTarea, 
                                       ft.IconButton(ft.icons.DONE_OUTLINE_OUTLINED,
                                                     icon_color=ft.colors.GREEN,
                                                     tooltip="Update To-Do",
                                                     on_click=self.saveClick)])
        
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

    def status_changed(self, e):
        self.completed = self.mostrarTarea.label
        self.task_status_change()
    
    def deleteClick(self, e):
        tareasbd.borrar_tarea(self.tareaId)
        self.func_Borrado(self)

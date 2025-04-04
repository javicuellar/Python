import flet as ft
from tareas.tareas_bd import TareasBD



tareasbd = TareasBD()


class TareasApp(ft.UserControl):
    def build(self):
        self.tarea_nueva = ft.TextField(on_submit=self.addClick)
        # self.bt_añadir_tarea = ft.FloatingActionButton(icon= ft.icons.ADD, on_click=self.addClick)

        self.tareas = ft.Column(
                        # on_scroll=on_scroll, 
                        # scroll=ft.ScrollMode.AUTO, 
                        # expand=True
                        )

        self.contenedor_tareas = ft.Container(content=self.tareas,
                                        expand=True,
                                        margin=10,
                                        padding=10,
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.colors.BLUE_100,
                                        width=150,
                                        height=150,
                                        border_radius=10,
                                        )
        
        tareas = ft.Column(controls=[ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[self.tarea_nueva],
                                            expand=True,
                                            ),
                                     self.tareas,
                                     ])
                                    

        self.cargar_tareas()

        return tareas

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




class Tarea(ft.UserControl):
    def __init__(self, id, nombre, func_Borrado):
        super().__init__()
        self.nombre = nombre
        self.func_Borrado = func_Borrado
        if id:
            self.tareaId = id
        else:
            self.tareaId = tareasbd.alta_tarea((nombre, ))

    def build(self):
        self.mostrarTarea = ft.TextButton(text=self.nombre, on_click=self.editTarea)
        self.mostrar = ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                              controls=[ft.Checkbox(value=False, on_change=self.actualizar),
                                        self.mostrarTarea,
                                        ft.Container(expand=True),
                                        ft.Row(controls=[ft.IconButton(ft.icons.CREATE_OUTLINED, on_click=self.editClick),
                                                         ft.IconButton(ft.icons.DELETE_OUTLINED, on_click=self.deleteClick)])])
        
        self.editTarea = ft.TextField(expand=True, on_submit=self.saveClick, autofocus=True)
        self.editar = ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, visible=False,
                            controls=[self.editTarea, 
                                      # ft.Container(expand=True),
                                      ft.IconButton(ft.icons.DONE_OUTLINED, on_click=self.saveClick)])
        

        self.prueba = ft.BottomAppBar(
            # on_click=self.editClick,
            bgcolor=ft.colors.WHITE,
            # shape=ft.NotchShape.CIRCULAR,
            content=ft.Row(
                controls=[
                    ft.Checkbox(value=False, on_change=self.actualizar),
                    self.mostrarTarea,
                    ft.Container(expand=True),
                    ft.IconButton(icon=ft.icons.CREATE_OUTLINED),
                    ft.IconButton(icon=ft.icons.DELETE_OUTLINED, icon_color=ft.colors.WHITE),
                    ]
                ),
            )


        # return ft.Column(controls=[self.prueba])




        return ft.Column(controls=[self.mostrar, self.editar])
    
    def actualizar(self, e):
        self.mostrarTarea.disabled = not self.mostrarTarea.disabled
        self.update()

    def editTarea(self, e):
        self.mostrar.visible = False
        self.editar.visible = True
        self.editTarea.value = self.mostrarTarea.text
        self.update()

    def editClick(self, e):
        self.mostrar.visible = False
        self.editar.visible = True
        self.editTarea.value = self.mostrarTarea.text
        self.update()

    def saveClick(self, e):
        self.mostrar.visible = True
        self.editar.visible = False
        self.mostrarTarea.text = self.editTarea.value
        self.nombre = self.editTarea.value
        tareasbd.actualizar_tarea(self.tareaId, self.nombre)
        self.update()

    def deleteClick(self, e):
        tareasbd.borrar_tarea(self.tareaId)
        self.func_Borrado(self)

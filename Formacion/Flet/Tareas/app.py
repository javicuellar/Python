"""
  Prueba de la aplicación Flet
  ============================

@author: Javier Cuéllar
"""
import flet as ft



class TaskApp(ft.UserControl):
    def build(self):
        self.textField = ft.TextField(width=350, on_submit=self.on_key_down)
        self.addBtn = ft.FloatingActionButton(icon= ft.icons.ADD, on_click=self.addClick)

        self.tasks = ft.Column()
        taskRow = ft.Column(controls=[
            ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                   controls=[self.textField, self.addBtn]),
            self.tasks])
        
        return taskRow

    def addClick(self, e):
        task = Task(self.textField.value, self.taskDelete)
        self.tasks.controls.append(task)
        self.textField.value = ""
        self.update()

    # Define la acción al presionar Enter
    def on_key_down(self, e):
        task = Task(self.textField.value, self.taskDelete)
        self.tasks.controls.append(task)
        self.textField.value = ""
        self.update()

    def taskDelete(self, task):
        self.tasks.controls.remove(task)
        self.update()


class Task(ft.UserControl):
    def __init__(self, taskName, taskDelete):
        super().__init__()
        self.taskName = taskName
        self.taskDelete = taskDelete

    def build(self):
        self.displayTask = ft.Checkbox(label=self.taskName, value=False)
        self.editName = ft.TextField()

        self.displayView = ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                  controls=[self.displayTask,
                                            ft.Row(controls=[ft.IconButton(ft.icons.CREATE_OUTLINED,
                                                                                 on_click=self.editClick),
                                                             ft.IconButton(ft.icons.DELETE_OUTLINED,
                                                                                 on_click=self.deleteClick)])])
        
        self.editView = ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                               visible=False,
                               controls=[self.editName,
                                         ft.IconButton(ft.icons.DONE_OUTLINED, on_click=self.saveClick)])
        
        return ft.Column(controls=[self.displayView, self.editView])
    
    def editClick(self, e):
        self.displayView.visible = False
        self.editView.visible = True
        self.editName.value = self.displayTask.label
        self.update()

    def saveClick(self, e):
        self.displayView.visible = True
        self.editView.visible = False
        self.displayTask.label = self.editName.value
        self.update()

    def deleteClick(self, e):
        self.taskDelete(self)




def main(page: ft.page):
    # Ponemos título a la aplicación"
    page.title = "Task App By Javier Cuéllar"
    # Definimos el tamaño de la ventana
    page.window_width = 500
    page.window_height = 600
    # Cambiamos el color, se pueden buscar los códigos de color en color hunt
    # page.bgcolor = "#C7DB9C"
    page.bgcolor = "WHITE"

    # Añadimos el control TaskApp
    taskApp = TaskApp()

    # page.add(textField, addBtn)     # ya no mostramos los componentes sueltos sino la fila Row
    page.add(taskApp)



# Ejecutar la aplicación en escritorio
ft.app(target=main)
# ft.app(target=main, view=ft.WEB_BROWSER)

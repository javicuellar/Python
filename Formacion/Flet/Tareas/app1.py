"""
  Prueba de la aplicación Flet
  ============================

@author: Javier Cuéllar
"""
import flet as ft


def main(page: ft.page):

    def addTask(p):
        # Añadimos un checkbox en la sgunda fila
        checBox = ft.Checkbox(value=False)
        checBoxText = ft.Text(value=textField.value, width=350, bgcolor="WHITE", size=16)
        textField.value = ""
        # Los añadimos a la fila Row de tareas
        taskRow = ft.Row(controls=[checBox, checBoxText], alignment=ft.MainAxisAlignment.START)
        page.add(taskRow)


    # Definimos el tamaño de la ventana
    page.window_width = 500
    page.window_height = 600
    # Cambiamos el color, se pueden buscar los códigos de color en color hunt
    # page.bgcolor = "#C7DB9C"
    page.bgcolor = "WHITE"

    # Campo texto
    textField = ft.TextField(width=350)
    # Añadimos botón
    # addBtn = ft.ElevatedButton(text="Add", on_click=addTask)
    # Cambiamos el botón por un icono, FloatingActionButton
    addBtn = ft.FloatingActionButton(icon= ft.icons.ADD, on_click=addTask)

    # Añadimos columna y los espaciamos con MainAxisAlignment.SPACE_BETWEEN
    entriesRow = ft.Row(controls=[textField, addBtn], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    

    # page.add(textField, addBtn)     # ya no mostramos los componentes sueltos sino la fila Row
    page.add(entriesRow)



# Ejecutar la aplicación en escritorio
ft.app(target=main)

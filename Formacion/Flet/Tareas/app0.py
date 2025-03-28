"""
  Prueba de la aplicación Flet
  ============================

@author: Javier Cuéllar
"""
import flet as ft


def main(page: ft.page):
    # Definimos el tamaño de la ventana
    page.window_width = 500
    page.window_height = 600
    # Cambiamos el color, se pueden buscar los códigos de color en color hunt
    page.bgcolor = "#C7DB9C"

    # Campo texto
    textField = ft.TextField(width=350)
    # Añadimos botón
    addBtn = ft.ElevatedButton(text="Add")
    # Añadimos columna y los espaciamos con MainAxisAlignment.SPACE_BETWEEN
    entriesRow = ft.Row(controls=[textField, addBtn], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    # Añadimos un checkbox en la sgunda fila
    checBox = ft.Checkbox(value=True)
    checBoxText = ft.Text(value="Task 1", width=350, bgcolor="WHITE", size=16)
    # Los añadimos a la fila Row de tareas
    taskRow = ft.Row(controls=[checBox, checBoxText], alignment=ft.MainAxisAlignment.START)

    
    # page.add(textField, addBtn)     # ya no mostramos los componentes sueltos sino la fila Row
    page.add(entriesRow,
             taskRow)



# Ejecutar la aplicación en escritorio
ft.app(target=main)

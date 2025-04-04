"""
  Copiado:  https://github.com/flet-dev/examples/blob/main/python/apps/todo/todo.py
"""
import flet as ft
from tareas.front import TareasApp





def main(page: ft.page):
    page.title = "Task App By Javier Cuéllar"
    # page.window_width = 500
    # page.window_height = 600
    page.scrooll = ft.ScrollMode.ADAPTIVE
    page.bgcolor = "WHITE"      # buscar colores en color hunt (ej. #C7DB9C)

    # Añadimos el control TaskApp
    tareaApp = TareasApp()

    page.add(tareaApp)



# Ejecutar la aplicación en escritorio
# ft.app(target=main)
ft.app(target=main, view=ft.WEB_BROWSER)

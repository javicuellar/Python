"""
  Copiado:  https://github.com/flet-dev/examples/blob/main/python/apps/todo/todo.py
"""
import flet as ft
from tareas.front_lista_tareas import Lista_TareasApp





def main(page: ft.page):
    page.title = "Pruebas lista de tareas"
    page.bgcolor = "WHITE"      # buscar colores en color hunt (ej. #C7DB9C)

    page.add(Lista_TareasApp(page))


# Ejecutar la aplicación en escritorio
# ft.app(target=main)
ft.app(target=main, view=ft.WEB_BROWSER)

"""
  Copiado:  https://github.com/flet-dev/examples/blob/main/python/apps/todo/todo.py
"""
import flet as ft
from tareas.front_tareas import TareasApp





def main(page: ft.page):
    page.title = "Aplicación de tareas"
    # page.window_width = 500
    # page.window_height = 600
    page.bgcolor = "WHITE"      # buscar colores en color hunt (ej. #C7DB9C)

    # Incluimos scrooll, primero intento con el scroll en la columna, pero no funciona, scroll en el page tampoco, theme??
    # page.scrooll = ft.ScrollMode.ALWAYS   # eliminado porque no funciona
    # page.theme = ft.Theme(
    prueba = ft.Theme(
      scrollbar_theme=ft.ScrollbarTheme(
          track_color={
              ft.MaterialState.HOVERED: ft.colors.AMBER,
              ft.MaterialState.DEFAULT: ft.colors.TRANSPARENT,
              },
          track_visibility=True,
          track_border_color=ft.colors.BLUE,
          thumb_visibility=True,
          thumb_color={
              ft.MaterialState.HOVERED: ft.colors.RED,
              ft.MaterialState.DEFAULT: ft.colors.GREY_300,
              },
          thickness=30,
          radius=15,
          main_axis_margin=5,
          cross_axis_margin=10,
          )
      )

    # Añadimos el control TaskApp
    tareaApp = TareasApp()

    page.add(tareaApp)



# Ejecutar la aplicación en escritorio
# ft.app(target=main)
ft.app(target=main, view=ft.WEB_BROWSER)

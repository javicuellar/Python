import flet as ft



def main(page: ft.Page):
    page.window.width = 620
    page.window.height = 520
    page.window.resizable = False
    # page.padding = 24
    # page.margin = 24

    page.add(ft.Text("Hola, Flet!"))



ft.app(main)

#   Se ejecuta por defecto en Windows ->   python hola_mundo.py   o  flet run hola_mundo.py
#
#   Para ejecutar en web -> flet run --web hola_mundo.py
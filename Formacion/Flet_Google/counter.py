import flet as ft
import time


def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ft.ElevatedButton(text="Say my name!")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    for i in range(4):
        txt_number.value = f"Step {i}"
        txt_number.update()
        # page.update()
        time.sleep(1)
    
    for i in range(1000):
        page.controls.append(ft.Text(f"Line {i}"))

    page.scroll = "always"
    page.update()



ft.app(main)

#   Hot Reload ->  "Modificaciones en caliente"
#  si ejecutamos poniendo -d al final -> flet run counter.py -d    (mira el directorio)
#
#  al modificar la variable number en el código, se modifica en la ejecución (en caliente). 

#  si ejecutamos -d -r  (lo mismo que -d pero añade también los subdirectorios )
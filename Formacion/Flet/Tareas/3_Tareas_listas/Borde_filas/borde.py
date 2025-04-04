import flet as ft

def main(page: ft.Page):
    # Crear una fila con bordes
    row = ft.Row(
        controls=[
            ft.Container(
                ft.Text("ID: 1"),
                padding=ft.padding.all(10),
                decoration= ft.bo(
                    border= ft.Border.all(color=ft.colors.GRAY, width=1),
                )
            ),
            ft.Container(
                ft.Text("Nombre: Elemento 1"),
                padding=ft.padding.all(10),
                decoration= ft.BoxDecoration(
                    border= ft.Border.all(color=ft.colors.GRAY, width=1),
                )
            ),
        ],
        spacing=10,
    )

    page.add(row)

ft.app(target=main)

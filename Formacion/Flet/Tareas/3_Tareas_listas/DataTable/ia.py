import flet as ft

def main(page: ft.Page):
    # Crear una lista de datos de ejemplo
    data = [
        {"id": 1, "nombre": "Elemento 1"},
        {"id": 2, "nombre": "Elemento 2"},
        {"id": 3, "nombre": "Elemento 3"},
    ]

    # Función para editar una fila
    def editar_fila(id):
        print(f"Editando fila con ID: {id}")
        # Aquí puedes agregar la lógica para editar la fila

    # Función para borrar una fila
    def borrar_fila(id):
        print(f"Borrando fila con ID: {id}")
        # Aquí puedes agregar la lógica para borrar la fila

    # Crear una tabla
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Acciones")),
        ],
        rows=[
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(item["id"])),
                ft.DataCell(ft.Text(item["nombre"])),
                ft.DataCell(
                    ft.Row([
                        ft.IconButton(ft.icons.EDIT, on_click=lambda e: editar_fila(item["id"])),
                        ft.IconButton(ft.icons.DELETE, on_click=lambda e: borrar_fila(item["id"])),
                    ])
                ),
            ])
            for item in data
        ]
    )

    # print("Tabla creada con éxito.")
    page.add(table)

ft.app(target=main)

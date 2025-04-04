#  Cómo Crear una Data Table con Flet y Guardar en Excel
#      https://codigoespinoza.com/blog/aprende-a-crear-una-datatable-con-flet-y-guardar-datos-en-excel.html

#    Introducción
#
#  En este tutorial, aprenderás a crear una Data Table utilizando Flet y Python. También verás cómo guardar los datos en un archivo Excel.
#  Vamos a construir una aplicación donde puedes ingresar nombres y edades, agregar estos datos a una tabla y luego exportarlos a Excel.

#  Configuración Inicial
# Primero, crea un nuevo archivo de Python llamado app.py. Asegúrate de tener instalada la librería Flet ejecutando pip install flet en
# tu terminal. Importa Flet y crea la función principal:

import flet as ft
import openpyxl
from datetime import datetime




def Main(page: ft.Page):
    page.title = "Data Table en Flet con Excel"
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    titulo = ft.Text("Data Table en Flet", size=24, color=ft.colors.WHITE)

    data_table = ft.DataTable(
        bgcolor = ft.colors.BLUE_GREY_700,
        border = ft.border.all(2, ft.colors.BLUE_GREY_200),
        border_radius = 5,
        vertical_lines=ft.border.BorderSide(2, ft.colors.BLUE_GREY_200),
        horizontal_lines=ft.border.BorderSide(1, ft.colors.BLUE_GREY_400),
        columns=[
            ft.DataColumn(ft.Text("ID", color=ft.colors.BLUE_200)),
            ft.DataColumn(ft.Text("Nombre", color=ft.colors.BLUE_200)),
            ft.DataColumn(ft.Text("Edad", color=ft.colors.BLUE_200)),
        ],
        rows=[]
    )
    

    def agregar_fila(e):
        nueva_fila = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(len(data_table.rows) + 1), color=ft.colors.WHITE)),
                ft.DataCell(ft.Text(nombre_input.value, color=ft.colors.WHITE)),
                ft.DataCell(ft.Text(edad_input.value, color=ft.colors.WHITE)),
                ]
            )
        data_table.rows.append(nueva_fila)
        nombre_input.value = ""
        edad_input.value = ""
        page.update()


    def guardar_excel(e):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Datos"

        ws.append(["ID", "Nombre", "Edad"])
        for row in data_table.rows:
            ws.append([cell.content.value for cell in row.cells])
    
            fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
            archivo_nombre = f"{fecha_hora}datos_tabla.xlsx"
            wb.save(archivo_nombre)

        snack_bar = ft.SnackBar(content= ft.Text(f"Datos guardados en {archivo_nombre}"))
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()
    

    nombre_input = ft.TextField(label="Nombre", bgcolor=ft.colors.BLUE_GREY_700)    # no coge el color ni del nombre ni edad
    edad_input = ft.TextField(label="Edad", bgcolor=ft.colors.BLUE_GREY_700, color=ft.colors.WHITE)

    agregar_btn = ft.ElevatedButton("Agregar", on_click=agregar_fila, color=ft.colors.WHITE, bgcolor=ft.colors.BLUE)
    guardar_btn = ft.ElevatedButton("Guardar en Excel", on_click=guardar_excel, color=ft.colors.WHITE, bgcolor=ft.colors.GREEN)
    
    input_container = ft.Row([nombre_input, edad_input, agregar_btn, guardar_btn], alignment=ft.MainAxisAlignment.CENTER)


    page.add(titulo, data_table, input_container)


ft.app(target=Main)
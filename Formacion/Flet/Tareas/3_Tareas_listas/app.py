import flet as ft
from tareas.front_tareas import TareasApp
from tareas.front_lista_tareas import Lista_TareasApp





def main(page: ft.page):
  page.title = "Aplicación de tareas"
  page.bgcolor = "WHITE"      # buscar colores en color hunt (ej. #C7DB9C)

  # Añadimos las vistas de tareas y lista de tareas
  tareaApp = TareasApp()
  lista_tareas = Lista_TareasApp(page)

  # Area de detalle - Tareas, Lista de tareas
  area_detalle = ft.Container(
        content= tareaApp,
        expand=True,
        )

  # Control de la vista del menú lateral
  def cambio_vista(seleccion):
    if seleccion == 0:
      area_detalle.content = tareaApp
    elif seleccion == 1:
      area_detalle.content = lista_tareas
        
    area_detalle.update()
    

  # Menú lateral
  menu = ft.NavigationRail(
    selected_index= 0,
    label_type= ft.NavigationRailLabelType.ALL,
    min_width= 100,
    min_extended_width= 0.9,
    group_alignment= -0.8,           # Alinear cerca del top -1.0, 0.0 al centro, 1.0 al bottom
    destinations=[
      ft.NavigationRailDestination(
        icon= ft.icons.FOLDER_COPY,
        selected_icon= ft.icons.FOLDER_COPY,
        label= "Tareas",
        ),
      ft.NavigationRailDestination(
        icon= ft.icons.EDIT_OUTLINED,
        selected_icon= ft.icons.EDIT,
        label= "Lista Tareas",
        ),
      ],
      bgcolor= ft.colors.WHITE,
      on_change= lambda e: cambio_vista(e.control.selected_index),
      )


  page.add(
    ft.Row([
      menu,
      ft.VerticalDivider(width=1),
      area_detalle,
      ],
      expand=True,
      )
    )



# Ejecutar la aplicación en escritorio
# ft.app(target=main)
ft.app(target=main, view=ft.WEB_BROWSER, port=5010)

import flet as ft
from tareas.tb_lista_tareas import TB_Lista_tareas





class Lista_TareasApp(ft.UserControl):
    def __init__(self, page):
        super().__init__(expand=True)
        self.page = page

        self.data_table = ft.DataTable(
            expand= True,
            border = ft.border.all(1, "black"),
            data_row_color = { ft.MaterialState.SELECTED: "grey", ft.MaterialState.PRESSED: "white"},
            border_radius=3,
            show_checkbox_column = True,
            show_bottom_border= True,
            columns=[
                ft.DataColumn(ft.Text("Nombre", color="black", weight = "bold") ),
                ft.DataColumn(ft.Text("Descripción", color="black", weight = "bold") ),
                ft.DataColumn(ft.Text("Color", color="black", weight = "bold"), ),
                ft.DataColumn(ft.Text("Acciones", color="black", weight = "bold") ),
                ],
            )        

        self.lista = ft.Column(
            expand= True,
            spacing=25,
            height=400,    
            scroll=ft.ScrollMode.ADAPTIVE,
            # alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.ResponsiveRow([
                    self.data_table
                    ]),
                ]
            )

        self.vista = ft.Column(
            controls=[
                ft.Text(value="Mantenimiento Lista de tareas", 
                        theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                        text_align= ft.TextAlign.LEFT,
                        weight=ft.FontWeight.BOLD),
                ft.Divider(height=1, color=ft.colors.GREY),  # Línea separadora
                ft.Row(
                    # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text("Lista:  "),
                        ft.TextField(expand=True, on_submit=self.addClick),
                        ],
                    ),
                ft.TextButton(text="Filtrar",
                    icon = ft.icons.SAVE,
                    icon_color= "white",
                    style= ft.ButtonStyle(color = "white",  bgcolor ="black"),
                    on_click= self.page.window_destroy,     # salir de la aplicación
                    tooltip="Filtrar",                      # descripción del botón
                    ),
                ft.Divider(height=1, color=ft.colors.GREY),  # Línea separadora
                self.lista,
                ]
            )
        
        self.show_data()

        
    def show_data(self):
        self.data_table.rows = []
        for x in TB_Lista_tareas.obtener_listas_tareas():
            self.data_table.rows.append(
                ft.DataRow(
                    on_select_changed= self.get_index, 
                    cells=[
                        ft.DataCell(ft.Text(x[1], color="black")),  
                        ft.DataCell(ft.Text(x[2], color="black")),  
                        ft.DataCell(ft.Text(x[3], color="black")),
                        ft.DataCell(
                            ft.Row([
                                ft.IconButton("create", icon_color ="black", on_click = self.get_index,),    
                                ft.IconButton("delete", icon_color ="black", on_click = self.delete_data,),
                                ])
                            ),
                    ]
                )
            )
        self.update()


    def get_index(self, e):
        if e.control.selected:
           e.control.selected = False
        else: 
            e.control.selected = True
        name = e.control.cells[0].content.value
        for row in TB_Lista_tareas.obtener_listas_tareas():
            if row[1] == name:
                self.selected_row = row
                break
        self.update()

    def delete_data(self):
        pass

    def addClick(self):
        pass


    def build(self):
        return self.vista



class Lista_Tareas(ft.Column):
    def __init__(self):
        super().__init__()


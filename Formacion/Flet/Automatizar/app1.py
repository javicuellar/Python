import flet as ft



def main(page:ft.Page):
    # Configuración básica de la ventana
    page.title = "Automatización de Tareas"
    page.window_width = 1000
    page.window_height = 600
    page.padding = 0
    page.bgcolor = ft.colors.BACKGROUND
    page.theme_mode = ft.ThemeMode.DARK

    # Agregar tema personalizado
    page.theme = ft.Theme(color_scheme_seed=ft.colors.BLUE,
                          visual_density=ft.ThemeVisualDensity.COMFORTABLE,
                          color_scheme=ft.ColorScheme(
                                primary=ft.colors.BLUE,
                                secondary=ft.colors.ORANGE,
                                background=ft.colors.GREY_900,
                                surface=ft.colors.GREY_800,
                                )
                            )

    def change_view(e):
        selected = e.control.selected_index
        if selected == 0:
            content_area.content = ft.Text(value="Vista de Duplicados", size=24)
        elif:
            content_area.content = ft.Text(value="Próximamente...", size=24)
        content_area.update()
    

    content_area = ft.Container(
        content=ft.Text(value="Vista de Duplicados", size=24),
        expand=True,
        padding=30
    )

    # Menú lateral
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.DELETE_FOREVER,
                selected_icon=ft.icons.DELETE_FOREVER,
                label="Duplicados",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.ADD_CIRCLE_OUTLINE,
                selected_icon=ft.icons.ADD_CIRCLE,
                label="Próximamente",
            ),
        ],
        on_change=change_view,
        bgcolor=ft.colors.GREY_900,
    )

    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                        ft.Text(value="Automatización de Tareas",
                            size = 28,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.BLUE_200
                            ),
                        ft.ElevatedButton(text="Botón de ejemplo",
                            icon=ft.icons.PLAY_ARROW
                            )
                        ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            alignment=ft.alignment.center,
            expand=True
        )
    )



if __name__ == "__main__":
    ft.app(target=main)

import flet as ft



class UIPago(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page
        self.page.padding = 0

        self.color_blue = "#73b1fc"
        self.color_purple = "#bb7efd"
        self.bg_color = "#3f3965"
        self.container_color = "#362e57"
        self.color_navigation_bt = "#2a2949"
        self.color1_card = "#f46fds"
        self.color2_card = "#64e4ed"

        self.page.bgcolor = self.bg_color
        
        self.animation_style = ft.animation.Animation(500, ft.AnimationCurve.EASE_IN_TO_LINEAR)

        
        self.container_1 = ft.Container(
            expand=True,
            bgcolor=self.container_color,
            offset= ft.transform.Offset(0,0),
            animate_offset=self.animation_style,
            content= ft.Row(
                controls= [
                    ft.Container(
                        expand=True,
                        content= ft.Stack(
                            # alignment= ft.alignment.top_center,
                            controls=[
                                ft.Container(
                                    expand=True,
                                    bgcolor= self.container_color,
                                    margin= ft.margin.only(left=0, top=150, right=0, bottom=0),
                                    padding= ft.padding.only(left=0, top=100, right=0, bottom=0),
                                    border_radius= 20,
                                    content= ft.Column(
                                        horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text("Transferencias", color="white", size=20, weight=20),
                                            ]
                                        )
                                    ),
                                ft.Container(
                                    height= 180,
                                    width = 300,
                                    gradient= ft.LinearGradient(
                                        rotation= 0.5,
                                        colors=[
                                            self.color1_card,
                                            self.color2_card,
                                            self.color_purple
                                            ]
                                        ),
                                        margin= ft.margin.only(left=50, top=50, right=50, bottom=0),
                                        border_radius=20,
                                        padding=10,
                                        content= ft.Column(
                                            controls=[
                                                ft.Text("6748 3511 5208 3480", color="white", size=16),
                                                ft.Text("10.470,00 €", color="white", size=30, weight="bold"),
                                            ],
                                        ),
                                    ),
                                ]
                            )
                        )
                    ]
                )
            )
    
        self.container_2 = ft.Container(
            expand=True,
            bgcolor=self.color_blue,
            offset= ft.transform.Offset(2,0),
            animate_offset=self.animation_style,
            content= ft.Row([
                ft.Text("6748 3511 5208 3480", color="white", size=16),
                ft.Text("10.470,00 €", color="white", size=30, weight="bold"),        
                ]),
            )
        self.container_3 = ft.Container(
            expand=True,
            bgcolor=self.container_color,
            offset= ft.transform.Offset(2,0),
            animate_offset=self.animation_style
            )
        self.container_4 = ft.Container(
            expand=True,
            bgcolor=self.container_color,
            offset= ft.transform.Offset(2,0),
            animate_offset=self.animation_style
            )
        
        self.frame =ft.Container(
            expand=True,
            content=ft.Stack(
                controls=[
                    self.container_1,
                    self.container_2,
                    self.container_3,
                    self.container_4,
                    ]
                )
            )

        
        self.option_1 = ft.Container(
            padding=10,
            bgcolor= self.color_purple,
            border_radius=15,
            offset= ft.transform.Offset(0,0),
            animate_offset= self.animation_style,
            on_click= lambda e: self.change_page(e, 1),
            height=40,
            content= ft.Row(
                alignment= ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.icons.DIRECTIONS, color= "white"),
                    ft.Text("Inicio", width=120, color="white")
                    ]
                )
            )
        
        self.option_2 = ft.Container(
            padding=10,
            bgcolor= self.color_navigation_bt,
            border_radius=15,
            offset= ft.transform.Offset(0,0),
            animate_offset= self.animation_style,
            on_click= lambda e: self.change_page(e, 2),
            height=40,
            content= ft.Row(
                alignment= ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.icons.SEARCH, color= "white"),
                    ft.Text("Buscar", width=120, color="white")
                    ]
                )
            )
        
        self.option_3 = ft.Container(
            padding=10,
            bgcolor= self.color_navigation_bt,
            border_radius=15,
            offset= ft.transform.Offset(0,0),
            animate_offset= self.animation_style,
            on_click= lambda e: self.change_page(e, 3),
            height=40,
            content= ft.Row(
                alignment= ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.icons.AIRPLANEMODE_ACTIVE, color= "white"),
                    ft.Text("Localidad", width=120, color="white")
                    ]
                )
            )

        self.option_4 = ft.Container(
            padding=10,
            bgcolor= self.color_navigation_bt,
            border_radius=15,
            offset= ft.transform.Offset(0,0),
            animate_offset= self.animation_style,
            on_click= lambda e: self.change_page(e, 4),
            height=40,
            content= ft.Row(
                alignment= ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.icons.SETTINGS, color= "white"),
                    ft.Text("Configuración", width=120, color="white")
                    ]
                )
            )
        

        self.navigation = ft.Container(
            padding=20,
            bgcolor= self.container_color,
            animate_size= self.animation_style,
            content= ft.Column(
                horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                alignment= ft.MainAxisAlignment.CENTER,
                controls=[
                    self.option_1,
                    self.option_2,
                    self.option_3,
                    self.option_4,
                    ]
                )
            )

        
        self.switch_control = {
            1: self.container_1,
            2: self.container_2,
            3: self.container_3,
            4: self.container_4,
            }
        

        self.page.add(
            ft.Row(
                expand=True,
                spacing=200,
                controls=[
                    self.navigation,
                    self.frame,
                        ]
                   )
            )



    def change_page(self, e, n):
        for page in self.switch_control:
            self.switch_control[page].offset.y = 2
            self.option_1.bgcolor = self.color_navigation_bt
            self.option_2.bgcolor = self.color_navigation_bt
            self.option_3.bgcolor = self.color_navigation_bt
            self.option_4.bgcolor = self.color_navigation_bt
        if n == 1:
            self.option_1.offset.x = 0.15
            self.option_1.bgcolor = self.color_purple
            self.option_2.offset.x = 0
            self.option_3.offset.x = 0
            self.option_4.offset.x = 0
        elif n == 2:
            self.option_2.offset.x = 0.15
            self.option_2.bgcolor = self.color_purple
            self.option_1.offset.x = 0
            self.option_3.offset.x = 0
            self.option_4.offset.x = 0
        elif n == 3:
            self.option_3.offset.x = 0.15
            self.option_3.bgcolor = self.color_purple
            self.option_1.offset.x = 0
            self.option_2.offset.x = 0
            self.option_4.offset.x = 0
        elif n == 4:
            self.option_4.offset.x = 0.15
            self.option_4.bgcolor = self.color_purple
            self.option_1.offset.x = 0
            self.option_2.offset.x = 0
            self.option_3.offset.x = 0
        
        self.page.update()




ft.app(target=lambda page: UIPago(page))

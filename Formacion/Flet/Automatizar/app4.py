#  Proyecto copiado de https://www.youtube.com/watch?v=KIBIuQi45D0

import flet as ft
from borrar_duplicados import find_duplicates, delete_file
from organizar_archivos import organize_folder
from cambiar_tamaño import batch_resize
from convertir_imagenes import convertir_imagen




def main(page:ft.Page):
    # Configuración básica de la ventana
    page.title = "Automatización de Tareas"
    page.window_width = 1000
    page.window_height = 650
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


    # Variables de estado
    state = {
            "current_duplicates": [],
            "current_view": "duplicates",
            "resize_input_folder": "",
            "resize_output_folder": "",
            "selecting_resize_output": False,
            "convert_input_file": "",
            }

    selected_dir_text = ft.Text(value="No se ha seleccionado ninguna carpeta", size=14, color=ft.colors.BLUE_200)
    
    result_text = ft.Text(size=14, weight=ft.FontWeight.BOLD)

    duplicates_list = ft.ListView(
            expand=1,
            spacing=10,
            height=200,
        )

    delete_all_button = ft.ElevatedButton(
            text="Eliminar Todos los Duplicados",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.RED_900,
            icon=ft.icons.DELETE_SWEEP,
            visible=False,
            on_click=lambda e: delete_all_duplicates()
        )

    # Controles para la vista Organizar archivos
    organize_dir_text = ft.Text(
        value="No se ha seleccionado ninguna carpeta", 
        size=14, 
        color=ft.colors.BLUE_200)

    organize_result_text = ft.Text(
        size=14, 
        weight=ft.FontWeight.BOLD)


    # Controles para vista de redimiensionar imágenes
    resize_input_text = ft.Text(value="Carpeta de origen: No seleccionada", size=14, color=ft.colors.BLUE_200)
    resize_output_text = ft.Text(value="Carpeta de destino: No seleccionada", size=14, color=ft.colors.BLUE_200)
    resize_result_text = ft.Text(size=14, weight=ft.FontWeight.BOLD)

    width_field = ft.TextField(
        label="Ancho",
        value="800",
        width=100,
        text_align=ft.TextAlign.RIGHT,
        keyboard_type=ft.KeyboardType.NUMBER,
        )

    height_field = ft.TextField(
        label="Alto",
        value="600",
        width=100,
        text_align=ft.TextAlign.RIGHT,
        keyboard_type=ft.KeyboardType.NUMBER,
        )
    


    # Controles para la vista de convertir imágenes
    convert_input_text = ft.Text(value="No se ha seleccionado ninguna imagen", size=14, color=ft.colors.BLUE_200)
    convert_result_text = ft.Text(size=14, weight=ft.FontWeight.BOLD)
    format_dropdoqn = ft.Dropdown(
        label="Formato de salida",
        width=200,
        options=[
            ft.dropdown.Option("PNG"),
            ft.dropdown.Option("JPEG"),
            ft.dropdown.Option("BMP"),
            ft.dropdown.Option("GIF"),
            ft.dropdown.Option("WEBP"),
            ],
        value="PNG",
        )


    def change_view(e):
        selected = e.control.selected_index
        if selected == 0:
            content_area.content = duplicate_files_view
            state["current_view"] = "duplicates"
        elif selected == 1:
            content_area.content = organize_files_view
            state["current_view"] = "organize"
        elif selected == 2:
            content_area.content = resize_files_view
            state["current_view"] = "resize"
        elif selected == 3:
            content_area.content = convert_images_view
            state["current_view"] = "convert"
        elif selected == 4:
            content_area.content = ft.Text(value="Próximamente...", size=24)
            state["current_view"] = "proximamente"
        content_area.update()
    


    # Controla la selección de un archivo (por ahora, después podrán ser más)
    def handle_file_picker(e: ft.FilePickerResultEvent):
        if e.files and len(e.files) > 0:
            file_path = e.files[0].path
            state['convert_input_file'] = file_path
            convert_input_text.value = f"Imagen seleccionada: {file_path}"
            convert_input_text.update()
            

    # Controla si se ha seleccionado una carpeta y la muestra
    def handle_folder_picker(e: ft.FilePickerResultEvent):
        if e.path:
            if state["current_view"] == "duplicates":
                selected_dir_text.value = f"Carpeta seleccionada: {e.path}"
                selected_dir_text.update()
                scan_directoriy(e.path)
            elif state["current_view"] == "organize":
                organize_dir_text.value = f"Carpeta seleccionada: {e.path}"
                organize_dir_text.update()
                organize_directory(e.path)
            elif state["current_view"] == "resize":
                if state["selecting_resize_output"]:
                    state["resize_output_folder"] = e.path
                    resize_output_text.value = f"Carpeta de destino: {e.path}"
                    resize_output_text.update()
                else:
                    state["resize_input_folder"] = e.path
                    resize_input_text.value = f"Carpeta de origen: {e.path}"
                    resize_input_text.update()



    def select_input_folder():
        state["resize_output_folder"] = ""
        folder_picker.get_directory_path()

    def select_output_folder():
        state["selecting_resize_output"] = True
        folder_picker.get_directory_path()


    def convert_image():
        try:
            if not state["convert_input_file"]:
                convert_result_text.value = "Error: Selecciona una imagen"
                convert_result_text.color = ft.colors.RED_400
                convert_result_text.update()
                return
            if not format_dropdoqn.value:
                convert_result_text.value = "Error: Selecciona un formato de salida"
                convert_result_text.color = ft.colors.RED_400
                convert_result_text.update()
                return
            
            convertir_imagen(state["convert_input_file"], format_dropdoqn.value)
            convert_result_text.value = "Imagen convertida correctamente"
            convert_result_text.color = ft.colors.GREEN_400
            convert_result_text.update()

        except Exception as e:
            convert_result_text.value = f"Error al convertir imagen {str(e)}"
            convert_result_text.color = ft.colors.RED_400
            convert_result_text.update()


    def resize_images():
        try:
            if not state["resize_input_folder"] or not state["resize_output_folder"]:
                resize_result_text.value = "Error: Selecciona las carpetas de origen y destino"
                resize_result_text.color = ft.colors.RED_400
                resize_result_text.update()
                return
            
            width = int(width_field.value)
            height = int(height_field.value)

            if width <= 0 or height <= 0:
                resize_result_text.value = "Error: Las dimensiones deben ser mayores a 0"
                resize_result_text.color = ft.colors.RED_400
                resize_result_text.update()
                return
            
            batch_resize(state["resize_input_folder"], state["resize_output_folder"], width, height)
            resize_result_text.value = "Imágenes redimensionadas correctamente"
            resize_result_text.color = ft.colors.GREEN_400
            resize_result_text.update()
        
        except ValueError:
            resize_result_text.value = "Error: Intrduce valores válidos para ancho y alto"
            resize_result_text.color = ft.colors.RED_400
            resize_result_text.update()

        except Exception as e:
            resize_result_text.value = f"Error al redimensionar imágenes: {str(e)}"
            resize_result_text.color = ft.colors.RED_400
            resize_result_text.update()


    # Borra la información de la lista de duplicados cada vez que cambia el directorio
    def scan_directoriy(directory):
        duplicates_list.controls.clear()
        state["current_duplicates"] = find_duplicates(directory)

        if not state["current_duplicates"]:
            result_text.value = "No se encontraron archivos duplicados"
            result_text.color = ft.colors.GREEN_400
            delete_all_button.visible = False
        else:
            result_text.value = f"Se encontraron {len(state['current_duplicates'])} archivos duplicados"
            result_text.color = ft.colors.ORANGE_400
            delete_all_button.visible = True
        
            for dup_file, original in state["current_duplicates"]:
                dup_row = ft.Row([
                    ft.Text(
                        value=f"Duplicado: {dup_file}\nOriginal: {original}",
                        size=12,
                        expand=True,
                        color=ft.colors.BLUE_200,
                        ),
                    ft.ElevatedButton(
                        text="Eliminar",
                        color=ft.colors.WHITE,
                        bgcolor=ft.colors.RED_900,
                        on_click= lambda e, path=dup_file: delete_duplicate(path)
                        ),
                    ])           
                duplicates_list.controls.append(dup_row)
        
        duplicates_list.update()
        result_text.update()
        delete_all_button.update()


    # Función para organizar archivos
    def organize_directory(directory):
        try:
            organize_folder(directory)
            organize_result_text.value = "Archivos organizados correctamente"
            organize_result_text.color = ft.colors.GREEN_400
        except Exception as e:
            organize_result_text.value = f"Error al organizar archivos: {str(e)}"
            organize_result_text.color = ft.colors.RED_400
        organize_result_text.update()


    # Función para borrar todos los archivos duplicados
    def delete_duplicate(filepath):
        if delete_file(filepath):
            result_text.value = f"Archivo eliminado: {filepath}"
            result_text.color = ft.colors.GREEN_400
            for control in duplicates_list.controls[:]:
                if filepath in control.controls[0].value:
                    duplicates_list.controls.remove(control)
            state["current_duplicates"] = [(dup, orig) for dup, orig in state["current_duplicates"] if dup != filepath]
            if not state["current_duplicates"]:
                delete_all_button.visible = False
        else:
            result_text.value = f"Error al eliminar {filepath}"
            result_text.color = ft.colors.RED_400
        
        duplicates_list.update()
        result_text.update()
        delete_all_button.update()


    # Boton borrar todos
    def delete_all_duplicates():
        deleted_count = 0
        failed_count = 0

        for dup_file, _ in state["current_duplicates"]:
            if delete_file(dup_file):
                deleted_count += 1
            else:
                failed_count += 1
        
        duplicates_list.controls.clear()
        state["current_duplicates"] = []
        delete_all_button.visible = False

        if failed_count == 0:
            result_text.value = f"Se eliminaron correctamente {deleted_count} archivos duplicados"
            result_text.color = ft.colors.GREEN_400
        else:
            result_text.value = f"Se eliminaron {deleted_count} archivos. Fallaron {failed_count} archivos"
            result_text.color = ft.colors.RED_400
        
        duplicates_list.update()
        result_text.update()
        delete_all_button.update()


    # Configurar los selectores de archivos
    file_picker = ft.FilePicker(on_result=handle_file_picker)
    file_picker.file_type = ft.FilePickerFileType.IMAGE
    file_picker.allowed_extensions = ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp']


    # Configurar el selector de carpetas
    folder_picker = ft.FilePicker(on_result=handle_folder_picker)
    page.overlay.extend([folder_picker, file_picker])


    # Vista de archivos duplicados
    duplicate_files_view = ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Text("Eliminar Archivos Duplicados", size=28, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200),
                        margin=ft.margin.only(bottom=20)
                    ),
                ft.Row([
                    ft.ElevatedButton(text="Seleccionar Carpeta", 
                                      icon=ft.icons.FOLDER_OPEN, 
                                      color=ft.colors.WHITE, 
                                      bgcolor=ft.colors.BLUE_900,
                                      on_click=lambda _: folder_picker.get_directory_path()
                                  ),
                    delete_all_button,
                    ]),
                ft.Container(
                    content=selected_dir_text,
                    margin=ft.margin.only(top=10, bottom=10)
                    ),
                result_text,
                ft.Container(
                        content= duplicates_list,
                        border= ft.border.all(width=2, color=ft.colors.BLUE_400),
                        border_radius=10,
                        padding=20,
                        margin= ft.margin.only(top=10),
                        bgcolor= ft.colors.BACKGROUND,
                        expand=True
                    )
            ]),
        padding=30,
        expand=True
    )


    # Vista de Organizar archivos
    organize_files_view = ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Text("Organizar Archivos por Tipo", size=28, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200),
                margin=ft.margin.only(bottom=20),
                ),
            ft.ElevatedButton(
                text="Seleccionar Carpeta",
                icon=ft.icons.FOLDER_OPEN,
                color=ft.colors.WHITE,
                bgcolor=ft.colors.BLUE_900,
                on_click=lambda _: folder_picker.get_directory_path()
                ),
            ft.Container(
                content=organize_dir_text,
                margin=ft.margin.only(top=10, bottom=10)
                ),
            organize_result_text,
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        value="Los archivos serán organizados en las siguientes carpetas:",
                        size=14,
                        color=ft.colors.BLUE_200,
                        ),
                    ft.Text(value="* Imagenes (.jpg, .jpeg, .png, .gif, .bmp, .svg, .webp)", size=14),
                    ft.Text(value="* Videos  ('.mp4, .avi, .mov, .flv, .wmv, .webm)", size=14),
                    ft.Text(value="* Audios  (.mp3, .wav, .flac, .ogg, .wma)", size=14),
                    ft.Text(value="* Documentos  (.pdf, .doc, .docx, .xls, .xlsx, .ppt, .pptx, .txt)", size=14),
                    ft.Text(value="* Comprimidos  ((.zip, .rar, .tar, .gz, .7z))", size=14),
                    ft.Text(value="* Ejecutables  (.exe, .msi)", size=14),
                ]),
                border=ft.border.all(width=2, color=ft.colors.BLUE_400),
                border_radius=10,
                padding=20,
                margin=ft.margin.only(top=10),
                bgcolor=ft.colors.BACKGROUND,
                )
            ]),
        padding=30,
        expand=True
    )


    
    # Vista de redimensionar imágenes
    resize_files_view = ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Text("Redimensionar Imágenes", size=28, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200),
                margin=ft.margin.only(bottom=20),
                ),
            ft.Row([
                ft.ElevatedButton(
                    text="Seleccionar Carpeta de Origen",
                    icon=ft.icons.FOLDER_OPEN,
                    color=ft.colors.WHITE,
                    bgcolor=ft.colors.BLUE_900,
                    on_click=lambda _: select_input_folder()
                    ),
                ft.ElevatedButton(
                    text="Seleccionar Carpeta de Destino",
                    icon=ft.icons.FOLDER_OPEN,
                    color=ft.colors.WHITE,
                    bgcolor=ft.colors.BLUE_900,
                    on_click=lambda _: select_output_folder()
                    ),
                ]),
            ft.Container(
                content=ft.Column([
                    resize_input_text,
                    resize_output_text,
                        ]),
                    margin=ft.margin.only(top=10, bottom=10)
                ),
            ft.Container(
                content=ft.Column([
                    ft.Text(value="Introduce las dimensiones en píxeles", size=14, color=ft.colors.BLUE_200),
                    ft.Row([
                        width_field,
                        ft.Text(value="x", size=20),
                        height_field,
                        ft.Text(value="píxeles", size=14),
                        ]),
                    ]),
                margin=ft.margin.only(top=10, bottom=10),
                ),
            ft.ElevatedButton(
                text="Redimensionar Imágenes",
                icon=ft.icons.PHOTO_SIZE_SELECT_LARGE,
                color=ft.colors.WHITE,
                bgcolor=ft.colors.BLUE_900,
                on_click=lambda _: resize_images()
                ),
            resize_result_text,
            ft.Container(
                content=ft.Column([
                    ft.Text(value="Información:", size=14, color=ft.colors.BLUE_200),
                    ft.Text(value="* Se procesarán archivos .jpg', .jpeg y .png", size=14),
                    ft.Text(value="* Las imágenes originales no serán modificadas", size=14),
                    ft.Text(value="* Las imaágenes redimensionadas se guardarán con el prefijo 'resized_'", size=14),
                    ]),
                border=ft.border.all(width=2, color=ft.colors.BLUE_400),
                border_radius=10,
                padding=20,
                margin=ft.margin.only(top=10),
                bgcolor=ft.colors.BACKGROUND,
                )
            ]),
        padding=30,
        expand=True
    )



    # Vista de convertir imágenes
    convert_images_view = ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Text("Convertir Formato de Imagen", size=28, weight=ft.FontWeight.BOLD),
                margin=ft.margin.only(bottom=20),
                ),
        ft.ElevatedButton(
            text="Seleccionar Imagen",
            icon=ft.icons.IMAGE,
            color=ft.colors.WHITE,
            bgcolor=ft.colors.BLUE_900,
            on_click=lambda _: file_picker.pick_files()
            ),
        ft.Container(
            content=convert_input_text,
            margin=ft.margin.only(top=10, bottom=10)
            ),
            format_dropdoqn,
            ft.Container(
                margin=ft.margin.only(top=10),
                content=ft.ElevatedButton(
                    text="Convertir Imagen",
                    icon=ft.icons.TRANSFORM,
                    color=ft.colors.WHITE,
                    bgcolor=ft.colors.BLUE_900,
                    on_click=lambda _: convert_image()
                ),
            ),
        convert_result_text,
        ft.Container(
                content=ft.Column([
                    ft.Text(value="Información", size=14, color=ft.colors.BLUE_200),
                    ft.Text(value="* Formatos soportados. PNG, JPEG, WEBP, BMP y GIF",size=14),
                    ft.Text(value="* La imagen original no será modificada",size=14),
                    ft.Text(value="* La imagen convertida se guardará en la misma carpeta",size=14),
                    ft.Text(value="* Al convertir a JPEG, las imágenes con transparencia se convertirán a fondo blanco",size=14),
                        ]),
                border=ft.border.all(width=2, color=ft.colors.BLUE_400),
                border_radius=10,
                padding=20,
                margin=ft.margin.only(top=10),
                bgcolor=ft.colors.BACKGROUND,
            ),
        ]),
        padding=30,
        expand=True
    )


    content_area = ft.Container(
        content= duplicate_files_view,
        expand=True,
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
                icon=ft.icons.FOLDER_COPY,
                selected_icon=ft.icons.FOLDER_COPY,
                label="Organizar",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.PHOTO_SIZE_SELECT_LARGE,
                selected_icon=ft.icons.PHOTO_SIZE_SELECT_LARGE,
                label="Redimensionar",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.TRANSFORM,
                selected_icon=ft.icons.TRANSFORM,
                label="Convertir",
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
        ft.Row([
            rail,
            ft.VerticalDivider(width=1),
            content_area,
            ],
            expand=True,
        )
    )



if __name__ == "__main__":
    ft.app(target=main)

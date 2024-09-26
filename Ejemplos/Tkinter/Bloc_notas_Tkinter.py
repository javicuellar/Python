#   Copiado de Recursos Python
#  https://recursospython.com/codigos-de-fuente/bloc-de-notas-simple-con-tkinter/

from typing import Optional
from tkinter import filedialog, messagebox
from pathlib import Path
import tkinter as tk


class Notepad(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Bloc de notas")
        self.geometry("800x500")
        # Barra de menú.
        self.menubar = tk.Menu()
        self.file_menu = tk.Menu(tearoff=False)
        self.file_menu.add_command(label="Nuevo", command=self.new)
        self.file_menu.add_command(label="Abrir", command=self.open)
        self.file_menu.add_command(label="Guardar", command=self.save)
        self.file_menu.add_command(
            label="Guardar como...",
            command=self.save_as
        )
        self.menubar.add_cascade(menu=self.file_menu, label="Archivo")
        self.config(menu=self.menubar)
        # Control principal para editar el texto de un archivo.
        self.text = tk.Text()
        self.text.pack(expand=True, fill=tk.BOTH)
        # El atributo `current_file` contiene la ruta del archivo
        # que se está editando actualmente o `None` si aún no se
        # ha guardado el archivo.
        self.current_file: Optional[Path] = None
        # Tipos de archivos que aparecerán en los cuadros para
        # abrir o guardar un archivo.
        self.filetypes: tuple[tuple[str, str], ...] = (
            ("Archivo de texto", "*.txt"),
            ("Todos los archivos", "*.*")
        )
        # Reemplazar el mecanismo de cierre por defecto de Tk
        # para poder guardar el archivo antes de terminar
        # el programa.
        self.protocol("WM_DELETE_WINDOW", self.close)
    
    def close(self) -> None:
        if not self.can_continue():
            return
        # Destruir la ventana.
        self.destroy()
    
    def set_current_file(self, current_file: Path) -> None:
        self.current_file = current_file
        # Cuando cambia el archivo actual se actualiza
        # el título con el nombre del nuevo archivo.
        self.title(self.current_file.name + " - Bloc de notas")
    
    def can_continue(self) -> bool:
        # Si se hicieron modificaciones al texto, pedir la
        # confirmación al usuario.
        if self.text.edit_modified():
            result = messagebox.askyesnocancel(
                title="Cambios sin guardar",
                message="¿Desea guardar el archivo actual antes de continuar?"
            )
            cancel = result is None
            save_before = result is True
            # Si el usuario canceló el diálogo, no continuar.
            if cancel:
                return False
            # Si eligió guardar el archivo, guardar y continuar.
            elif save_before:
                self.save()
            return True
        # Si no hubo modificaciones, continuar sin guardar.
        return True
    
    def new(self) -> None:
        if not self.can_continue():
            return
        # Eliminar el texto anterior.
        self.text.delete("1.0", tk.END)
        self.current_file = None
        self.title("Bloc de notas")
    
    def open(self) -> None:
        filename = filedialog.askopenfilename(filetypes=self.filetypes)
        if not filename or not self.can_continue():
            return
        # Eliminar el texto anterior e insertar el contenido
        # del arhcivo seleccionado por el usuario.
        self.text.delete("1.0", tk.END)
        file = Path(filename)
        self.text.insert("1.0", file.read_text("utf8"))
        # Reiniciar el estado del texto cuando se abre un nuevo
        # archivo.
        self.text.edit_modified(False)
        self.set_current_file(file)
    
    def save_current_file(self) -> None:
        if self.current_file is None:
            return
        self.current_file.write_text(self.text.get("1.0", tk.END), "utf8")
    
    def save(self) -> None:
        if self.current_file is None:
            self.save_as()
            return
        self.save_current_file()
    def save_as(self) -> None:
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=self.filetypes
        )
        # No hacer nada si el usuario canceló o cerró el
        # diálogo.
        if not filename:
            return
        self.set_current_file(Path(filename))
        self.save_current_file()


notepad = Notepad()
notepad.mainloop()
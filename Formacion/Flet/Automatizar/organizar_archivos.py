import os
import shutil



def organize_folder(folder):
    file_types = {
        'Imagenes':     ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
        'Videos':       ['.mp4', '.avi', '.mov', '.flv', '.wmv', '.webm'],
        'Audios':       ['.mp3', '.wav', '.flac', '.ogg', '.wma'],
        'PDFs':         ['.pdf'],
        'Documentos':   ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'],
        'Comprimidos':  ['.zip', '.rar', '.tar', '.gz', '.7z'],
        'Ejecutables':  ['.exe', '.msi'],
        }

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            for folder_name, extensions in file_types.items():
                if ext in extensions:
                    target_folder = os.path.join(folder, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, file))
                    print(f"Archivo {file} movido a {target_folder}")


if __name__ == "__main__":
    organize_folder("C:\\Users\javic\Downloads")

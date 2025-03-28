from PIL import Image
import os


def batch_resize(folder_in, folder_out, width, height):
    for filename in os.listdir(folder_in):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            img = Image.open(os.path.join(folder_in, filename))
            img = img.resize((width, height))
            img.save(os.path.join(folder_out, f"resized_{filename}"))
            print(f"Redimensionado {filename} to {width}x{height}")



if __name__ == "__main__":
    origen = "C:\\Users\javic\Downloads\Archivos\Imagenes"
    destino = "C:\\Users\javic\Downloads\Archivos\Imagenes_resized"
    batch_resize(origen, destino, 600, 800)
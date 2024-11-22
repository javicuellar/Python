import cv2
import numpy as np
import pyautogui
import keyboard



medida_pantalla = pyautogui.size()
fps = 20
fourcc = cv2.VideoWriter_fourcc(*"XVID")
fichero_salida = "grabar_pantalla.mp4"
out = cv2.VideoWriter(fichero_salida, fourcc, fps, (medida_pantalla.width, medida_pantalla.height))

print("Grabando pantalla... pulsa 'q' para parar.")
while True:
    pantalla = pyautogui.screenshot()
    frame = np.array(pantalla)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    out.write(frame)

    if keyboard.is_pressed('q'):
        print('Grabación parada.')
        break

out.release()
print(f'Video grabado: {fichero_salida}')
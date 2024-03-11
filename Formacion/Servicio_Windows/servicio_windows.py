import psutil       # Información de procesos (y memoria, disco, redes,...)
import sys          # Recuperar argumentos de terminal (y ...)


# El programa recibirá los argumentos del terminal
def checquer_argumentos():
    if len(sys.argv) == 1:
        print("Este programa no funciona sin argumentos")
        sys.exit(0)         # sale del programa


def obtener_target():                       
    targets = sys.argv[1:]                  # recuperamos desde el segundo argumento
    for i in range(len(targets)):
        if not targets[i].endswith('.exe'):     # sino tiene la extensión
            targets[i] = targets[i] + '.exe'    # se la ponemos
    return targets


def detener_proceso(target):
    for proceso in psutil.process_iter():       # recorremos los procesos activos
        if proceso.name().lower() == target.lower():
            print("Notepad ejecutándose.")
            proceso.kill()
            print("Proceso detenido")



# se ejecuta directamente, cuando no es usado como modulo
if __name__ == "__main__":      
    checquer_argumentos()
    targets = obtener_target()

    while True:
        for target in targets:
            detener_proceso(target)     # detenemos el proceso cada vez que se abre

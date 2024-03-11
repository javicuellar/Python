import sys


# Devuelve la lista de argumentos introducida al ejecutar
for i in sys.argv:
    print("Argumentos introducidos: ", i)

# Devuelve el contenido de la variable path (rutas del sistema)
for i in sys.path:
    print("Path -> ", i)


# la función sys.displayhook podría servir para decodificar caracteres raros


# salir del programa
sys.exit(0)

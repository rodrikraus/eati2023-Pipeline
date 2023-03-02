"""EATI2023 Rodrigo Kraus"""

import os.path


def main():
    """Ejecuto el método main."""

    if os.path.exists('build'):
        print('Ya existe el archivo')
    else:
        os.mkdir('build')
        with open(r'build\index.html', 'x',  encoding="utf8"):
            print('Archivo abierto exitosamente.')


main()

"""GitHub Actions EATI 2023 - Creación de pipeline"""
import os.path


def main():
    """
    Si no existe, crea la carpeta build y el archivo index.html
    """

    if os.path.exists('build/'):
        print('\nLa carpeta build ya existe.')
    else:
        os.mkdir('build/')
        print('\nSe creó la carpeta build.')

    if os.path.isfile('build/index.html'):
        print('El archivo index ya existe en la carpeta build\n')
    else:
        with open('build/index.html', 'w', encoding="utf-8"):
            print("Archivo creado exitosamente")


if __name__ == '__main__':
    main()

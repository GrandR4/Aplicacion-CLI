# Aplicacion-CLI

import os

DIRECTORIO_ACTUAL = os.getcwd()

def impresion(mensaje):
    print("="*70)
    print(mensaje)
    print("="*70)

def lista_de_archivos(directorio):
    try:
        impresion(f"Contenido de La Carpeta: {directorio}" )
        archivos = os.listdir(directorio)
        for archivo in archivos:
            print(archivo)
    except FileNotFoundError:
        print("El directorio no existe.")
    except PermissionError:
        print("No tienes permiso para acceder a este directorio.")

lista_de_archivos(DIRECTORIO_ACTUAL)

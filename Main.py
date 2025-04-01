import os

DIRECTORIO_ACTUAL = os.getcwd() #Se usa las mayuscalas para indicar que es una constante
                                #Tambien usamos getcwd() para que obtener el directeorio de trabajo actual

def impresion(mensaje): #La funcion impresion la usamos para monstrar la direccion del directorio 
    print("="*70)
    print(mensaje)
    print("="*70)

def lista_de_archivos(directorio):  #La funcion lista_de_archivos es usada para 
                                    #Revisar los archivos en el directorio y posteriormente mostrarlo
    try:
        impresion(f"Contenido de La Carpeta: {directorio}" )
        archivos = os.listdir(directorio)
        for archivo in archivos:
            print(archivo)
    except FileNotFoundError:
        print("El directorio no existe.")
    except PermissionError:
        print("No tienes permiso para acceder a este directorio.")

lista_de_archivos(DIRECTORIO_ACTUAL) #Llamamos a la funcion 

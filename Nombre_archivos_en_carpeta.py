import os

def listar_archivos(carpeta):
    # Verifica si la carpeta existe
    if not os.path.exists(carpeta):
        print(f"La carpeta '{carpeta}' no existe.")
        return []

    # Lista todos los archivos en la carpeta
    archivos = [archivo for archivo in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, archivo))]
    
    return archivos

# Ruta de la carpeta que se desea listar (predefinida)
carpeta = "C:/Users/cesar/Desktop/Imagenes" #C:\Users\cesar\Documents\Audacity

# Llamamos a la función y mostramos la lista de archivos
archivos_encontrados = listar_archivos(carpeta)

if archivos_encontrados:
    print("Archivos en la carpeta:")
    for archivo in archivos_encontrados:
        print(archivo)
else:
    print("No se encontraron archivos en la carpeta.")

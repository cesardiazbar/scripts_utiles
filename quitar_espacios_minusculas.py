import os

def renombrar_archivos(carpeta):
    # Verifica si la carpeta existe
    if not os.path.exists(carpeta):
        print(f"La carpeta '{carpeta}' no existe.")
        return

    # Lista todos los archivos en la carpeta
    for archivo in os.listdir(carpeta):
        # Verifica si es un archivo
        if os.path.isfile(os.path.join(carpeta, archivo)):
            # Separa el nombre del archivo y su extensión
            nombre, extension = os.path.splitext(archivo)
            # Cambia el nombre a minúsculas y reemplaza los espacios con guiones bajos
            nuevo_nombre = nombre.lower().replace("__", "_") + extension
            # Define la ruta completa para el renombrado
            ruta_antigua = os.path.join(carpeta, archivo)
            ruta_nueva = os.path.join(carpeta, nuevo_nombre)
            # Renombra el archivo
            os.rename(ruta_antigua, ruta_nueva)
            print(f'Renombrado: "{archivo}" a "{nuevo_nombre}"')

# Ruta de la carpeta que deseas procesar (predefinida)
carpeta = "C:/Users/cesar/Documents/Audacity"

# Llamamos a la función para renombrar los archivos
renombrar_archivos(carpeta)

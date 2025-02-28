import os

# Cambia esta ruta a la carpeta que contiene tus archivos
carpeta = 'C:/Users/cesar/Documents/RESONANCIA IMAGENES/159115/Imagenes/9_COR_T2_LCA_DER'
sufijo = '.png'  # Cambia esto por cualquier cosa que quieras agregar al final del nombre del archivo

# Recorre todos los archivos en la carpeta
for nombre_archivo in os.listdir(carpeta):
    # Verifica que sea un archivo (no una carpeta)
    if os.path.isfile(os.path.join(carpeta, nombre_archivo)):
        # Divide el nombre del archivo y su extensión
        nombre, extension = os.path.splitext(nombre_archivo)
        # Crea el nuevo nombre con el sufijo
        nuevo_nombre = f"{nombre}{sufijo}{extension}"
        # Genera la ruta completa para renombrar
        ruta_original = os.path.join(carpeta, nombre_archivo)
        nueva_ruta = os.path.join(carpeta, nuevo_nombre)
        # Renombra el archivo
        os.rename(ruta_original, nueva_ruta)
        print(f"Renombrado: {nombre_archivo} -> {nuevo_nombre}")
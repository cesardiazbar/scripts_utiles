import os

# Ruta base
ruta_base = r'C:\Users\cesar\OneDrive\Documentos\MASTER GIS\AUTOCAD\BÁSICO' #Reemplazar ruta por la ruta de los archivos

# Crear carpetas de modulo1 a modulo11
for i in range(1, 11):  #Modificar le rango a conveniencia, se ignora el último número.
    nombre_carpeta = f'AutoCAD BÁSICO - Módulo {i}'
    ruta_carpeta = os.path.join(ruta_base, nombre_carpeta)

    # Verificar si la carpeta ya existe antes de crearla
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
        print(f'Carpeta {nombre_carpeta} creada en {ruta_carpeta}')
    else:
        print(f'Carpeta {nombre_carpeta} ya existe en {ruta_carpeta}')
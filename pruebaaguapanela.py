import matplotlib.pyplot as plt
import networkx as nx
# Vamos a crear algunos ejemplos de gráficos diferentes relacionados con los conceptos de agroecología
import numpy as np

# Datos de ejemplo
concepts = ["Biodiversidad", "Soberanía Alimentaria", "Sistemas Sostenibles", "Diversificación de Cultivos", 
            "Resiliencia", "Conocimiento Local", "Autosuficiencia", "Participación Comunitaria", "Seguridad Alimentaria", "Conservación del Agua"]
values = [8, 9, 7, 6, 8, 9, 7, 8, 8, 7]

# 1. Gráfico de Barras
plt.figure(figsize=(10, 6))
plt.bar(concepts, values, color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.title("Importancia de Conceptos Clave en Agroecología", size=14)
plt.ylabel("Nivel de importancia (Escala 1-10)", size=12)
plt.tight_layout()
plt.show()

# 2. Gráfico de Radar
from math import pi

# Preparar datos para gráfico de radar
labels = np.array(concepts)
stats = np.array(values)

# Número de variables
num_vars = len(labels)

# Crear ángulo para el gráfico
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
stats = np.concatenate((stats, [stats[0]]))
angles += angles[:1]

# Crear el gráfico de radar
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, stats, color='skyblue', alpha=0.25)
ax.plot(angles, stats, color='blue', linewidth=2)
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=10)
ax.set_title("Gráfico de Radar: Agroecología", size=14, y=1.1)

plt.show()


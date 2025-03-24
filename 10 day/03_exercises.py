# Importamos la lista de países desde el archivo countries.py
from countries import countries  

# Filtramos los países que contienen la palabra "land"
paises_con_land = [pais for pais in countries if "land" in pais]
print("Países que contienen 'land':", paises_con_land)

# Lista de frutas
frutas = ['banana', 'naranja', 'mango', 'limón']

# Invertimos la lista de frutas usando un bucle
frutas_invertidas = []
for i in range(len(frutas) - 1, -1, -1):
    frutas_invertidas.append(frutas[i])
print("Lista de frutas invertida:", frutas_invertidas)

# Importamos json para manejar el archivo de datos de países
import json

# Abrimos y cargamos los datos del archivo countries-data.py
with open("countries-data.py", "r", encoding="utf-8") as archivo:
    datos_paises = json.load(archivo)

# Creamos un conjunto para almacenar todos los idiomas sin repetir
todos_los_idiomas = set()
for pais in datos_paises:
    todos_los_idiomas.update(pais["languages"])  # Agregamos los idiomas de cada país
print(f"Número total de idiomas: {len(todos_los_idiomas)}")

# Importamos Counter para contar la frecuencia de los idiomas
from collections import Counter

# Contamos cuántas veces aparece cada idioma en los datos
conteo_idiomas = Counter()
for pais in datos_paises:
    conteo_idiomas.update(pais["languages"])

# Obtenemos los 10 idiomas más hablados
top_10_idiomas = conteo_idiomas.most_common(10)
print("Los 10 idiomas más hablados son:")
for idioma, cantidad in top_10_idiomas:
    print(f"{idioma}: {cantidad}")

# Ordenamos los países por población en orden descendente y tomamos los 10 primeros
top_10_paises = sorted(datos_paises, key=lambda x: x["population"], reverse=True)[:10]
print("Los 10 países más poblados son:")
for pais in top_10_paises:
    print(f"{pais['name']}: {pais['population']}")
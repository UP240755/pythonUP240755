# Función que verifica si un número es primo
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  # True
print(is_prime(10))  # False


# Función que verifica si todos los elementos de una lista son únicos
def elementos_unicos(lista):
    return len(lista) == len(set(lista))

print(elementos_unicos([1, 2, 3, 4, 5]))  # True
print(elementos_unicos([1, 2, 2, 4, 5]))  # False


# Función que verifica si todos los elementos de la lista son del mismo tipo de datos
def mismos_tipos(lista):
    return all(isinstance(i, type(lista[0])) for i in lista)

print(mismos_tipos([1, 2, 3, 4]))  # True
print(mismos_tipos([1, "hola", 3]))  # False


# Función que verifica si una variable es un identificador válido en Python
def es_identificador_valido(variable):
    return variable.isidentifier()

print(es_identificador_valido("nombre_usuario"))  # True
print(es_identificador_valido("2variable"))  # False
print(es_identificador_valido("def"))  # False (Palabra reservada)


# Importar JSON para manejar el archivo de datos
import json

# Cargar los datos del archivo Countries-data.py
with open("countries-data.py", "r", encoding="utf-8") as archivo:
    datos_paises = json.load(archivo)


# Función que devuelve los idiomas más hablados en el mundo
from collections import Counter

def idiomas_mas_hablados(n=10):
    conteo_idiomas = Counter()
    for pais in datos_paises:
        conteo_idiomas.update(pais["languages"])
    return conteo_idiomas.most_common(n)

print("Idiomas más hablados del mundo:")
for idioma, cantidad in idiomas_mas_hablados(20):
    print(f"{idioma}: {cantidad}")


# Función que devuelve los países más poblados del mundo
def paises_mas_poblados(n=10):
    return sorted(datos_paises, key=lambda x: x["population"], reverse=True)[:n]

print("Países más poblados del mundo:")
for pais in paises_mas_poblados(20):
    print(f"{pais['name']}: {pais['population']}")

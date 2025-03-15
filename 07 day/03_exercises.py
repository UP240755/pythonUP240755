# Lista de edades
edades = [25, 30, 25, 40, 35, 30, 40, 50, 35, 25]

# Convertir la lista en un conjunto
edades_set = set(edades)

# Comparar la longitud de la lista y el conjunto
print("Longitud de la lista de edades:", len(edades))
print("Longitud del conjunto de edades:", len(edades_set))

# Determinar cuál es más grande
if len(edades) > len(edades_set):
    print("La lista es más grande que el conjunto.")
elif len(edades) < len(edades_set):
    print("El conjunto es más grande que la lista.")
else:
    print("La lista y el conjunto tienen la misma longitud.")

# Explicación de los tipos de datos
print("\n**Diferencias entre cadena, lista, tupla y conjunto:**")
print("- Cadena (str): Es una secuencia inmutable de caracteres. Se usa para almacenar texto.")
print("- Lista (list): Es una colección ordenada y mutable de elementos. Puede contener duplicados.")
print("- Tupla (tuple): Es similar a una lista, pero inmutable (no se puede modificar después de su creación).")
print("- Conjunto (set): Es una colección desordenada de elementos únicos (no permite duplicados).")

# Contar palabras únicas en una oración
oracion = "Soy profesor y me encanta inspirar y enseñar a la gente."
palabras = oracion.lower().replace(".", "").split()  # Convertir a minúsculas y dividir en palabras
palabras_unicas = set(palabras)

print("\nNúmero de palabras únicas en la oración:", len(palabras_unicas))
print("Palabras únicas:", palabras_unicas)
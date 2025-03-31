# Filtrar solo los números negativos y ceros
def filtrar_negativos_y_ceros(numeros):
    return [num for num in numeros if num <= 0]

numeros = [-4, -3, -2, -1, 0, 2, 4, 6]
print(filtrar_negativos_y_ceros(numeros))

# Aplanar una lista de listas de listas
def aplanar_lista(lista_de_listas):
    return [num for sublista1 in lista_de_listas for sublista2 in sublista1 for num in sublista2]

lista_de_listas = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print(aplanar_lista(lista_de_listas))

# Crear una lista de tuplas
def generar_tuplas():
    return [(i, *[i**j for j in range(7)]) for i in range(11)]

print(generar_tuplas())

# Aplanar una lista de países y capitales
def transformar_paises(paises):
    return [[pais.upper(), pais[:3].upper(), ciudad.upper()] for sublista in paises for pais, ciudad in sublista]

paises = [[('Finlandia', 'Helsinki')], [('Suecia', 'Estocolmo')], [('Noruega', 'Oslo')]]
print(transformar_paises(paises))

# Convertir una lista en una lista de diccionarios
def lista_a_diccionarios(paises):
    return [{'pais': pais.upper(), 'ciudad': ciudad.upper()} for sublista in paises for pais, ciudad in sublista]

print(lista_a_diccionarios(paises))

# Convertir una lista de nombres en cadenas concatenadas
def concatenar_nombres(nombres):
    return [' '.join(nombre) for sublista in nombres for nombre in sublista]

nombres = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
print(concatenar_nombres(nombres))

# Funciones lambda para calcular la pendiente e intersección con el eje Y
pendiente = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
interseccion_y = lambda x, y, m: y - m*x

# Ejemplo de uso:
m = pendiente(1, 2, 3, 6)
b = interseccion_y(1, 2, m)
print(m, b)

# Lista de edades de los estudiantes
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Ordenar la lista y encontrar la edad mínima y máxima
ages.sort()
min_age = ages[0]
max_age = ages[-1]

print("Lista ordenada:", ages)
print("Edad mínima:", min_age)
print("Edad máxima:", max_age)

# Agregar la edad mínima y máxima nuevamente a la lista
ages.append(min_age)
ages.append(max_age)
print("Lista después de agregar min y max nuevamente:", ages)

# Encontrar la edad media (mediana)
ages.sort()
mid_index = len(ages) // 2
if len(ages) % 2 == 0:
    median_age = (ages[mid_index - 1] + ages[mid_index]) / 2
else:
    median_age = ages[mid_index]

print("Mediana de las edades:", median_age)

# Encontrar la edad promedio
average_age = sum(ages) / len(ages)
print("Edad promedio:", average_age)

# Encontrar el rango de edades
age_range = max_age - min_age
print("Rango de edades:", age_range)

# Comparar (mín - promedio) y (máx - promedio) usando abs()
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)

print("Diferencia entre min y promedio:", min_diff)
print("Diferencia entre max y promedio:", max_diff)

# Lista de países
countries = ['China', 'Rusia', 'EE. UU.', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']

# Encontrar el país o países intermedios
middle_index = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = [countries[middle_index - 1], countries[middle_index]]
else:
    middle_countries = [countries[middle_index]]

print("País o países intermedios:", middle_countries)

# Dividir la lista de países en dos partes iguales
half = len(countries) // 2
if len(countries) % 2 == 0:
    first_half = countries[:half]
    second_half = countries[half:]
else:
    first_half = countries[:half + 1]
    second_half = countries[half + 1:]

print("Primera mitad de países:", first_half)
print("Segunda mitad de países:", second_half)

# Desglose de los países: primeros tres y los demás como escandinavos
first_three = countries[:3]
scandinavian_countries = countries[3:]

print("Primeros tres países:", first_three)
print("Países escandinavos:", scandinavian_countries)
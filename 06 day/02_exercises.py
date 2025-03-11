# Desempaquetar hermanos y padres de family_members
family_members = ("Padre", "Madre", "Hermano1", "Hermano2" , "Hermano3")
padre, madre, hermano1, hermano2 , hermano3 = family_members
print(family_members)

# Crear tuplas de frutas, verduras y productos animales
frutas = ("Manzana", "Banana", "Naranja")
verduras = ("Zanahoria", "Espinaca", "Brócoli")
productos_animales = ("Leche", "Huevo", "Carne")

# Unir las tres tuplas en food_stuff_tp
food_stuff_tp = frutas + verduras + productos_animales
print("Tupla de alimentos:", food_stuff_tp)

# Convertir food_stuff_tp en una lista
food_stuff_lt = list(food_stuff_tp)
print("Lista de alimentos:", food_stuff_lt)

# Extraer el elemento o elementos del medio
medio = len(food_stuff_lt) // 2
elemento_medio = food_stuff_lt[medio] if len(food_stuff_lt) % 2 != 0 else food_stuff_lt[medio-1:medio+1]
print("Elemento(s) del medio:", elemento_medio)

# Separar los primeros tres y los últimos tres elementos
primeros_tres = food_stuff_lt[:3]
ultimos_tres = food_stuff_lt[-3:]
print("Primeros tres elementos:", primeros_tres)
print("Últimos tres elementos:", ultimos_tres)

# Eliminar la tupla food_stuff_tp
del food_stuff_tp

# Comprobar si un elemento existe en una tupla
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print("¿Estonia es un país nórdico?", 'Estonia' in nordic_countries)
print("¿Islandia es un país nórdico?", 'Iceland' in nordic_countries)

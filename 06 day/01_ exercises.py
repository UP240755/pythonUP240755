# Crear una tupla vacía
empty_tuple = ()

# Crear una tupla con los nombres de hermanos y hermanas (pueden ser imaginarios)
brothers = ("Carlos", "Juan", "Miguel")
sisters = ("Ana", "María", "Sofía")

# Unir tuplas de hermanos y hermanas
siblings = brothers + sisters
print("Hermanos y hermanas:", siblings)

# Contar cuántos hermanos hay
num_siblings = len(siblings)
print("Número de hermanos:", num_siblings)

# Modificar la tupla para agregar a los padres
parents = ("Papá", "Mamá")
family_members = siblings + parents
print("Miembros de la familia:", family_members)
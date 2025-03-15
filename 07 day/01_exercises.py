# Definir un conjunto de empresas de TI
it_companies = {"Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}

# Encuentra la longitud del conjunto it_companies
print("Longitud del conjunto:", len(it_companies))

# Añadir 'Twitter' a it_companies
it_companies.add("Twitter")
print("Después de añadir 'Twitter':", it_companies)

# Insertar varias empresas de TI a la vez en el conjunto it_companies
it_companies.update(["Facebook", "Intel", "Netflix"])
print("Después de añadir varias empresas:", it_companies)

# Eliminar una de las empresas del conjunto it_companies
it_companies.remove("IBM")  # Lanza un error si el elemento no existe
print("Después de eliminar 'IBM':", it_companies)

# Diferencia entre remove y discard
# remove() genera un error si el elemento no está presente
# discard() simplemente no hace nada si el elemento no está en el conjunto
it_companies.discard("Sony")  # No da error si 'Sony' no está en el conjunto
print("Después de intentar descartar 'Sony':", it_companies)

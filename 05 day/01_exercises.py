# Declarar una lista vacía
empty_list = []

# Declarar una lista con más de 5 elementos
my_list = [1, 2, 3, 4, 5, 6, 7]

# Encuentra la longitud de la lista
list_length = len(my_list)
print("Longitud de la lista:", list_length)

# Obtener el primer, el medio y el último elemento
first_element = my_list[0]
middle_element = my_list[len(my_list)//2]
last_element = my_list[-1]

print("Primer elemento:", first_element)
print("Elemento del medio:", middle_element)
print("Último elemento:", last_element)

# Declarar la lista mixed_data_types
mixed_data_types = ["Steven", 19, 1.68, "Soltero", "San Antonio De Peñuelas"]
print("Lista mixed_data_types:", mixed_data_types)

# Declarar it_companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("Lista de empresas de TI:", it_companies)

# Número de empresas en la lista
print("Número de empresas en la lista:", len(it_companies))

# Imprimir la primera, segunda y última empresa
print("Primera empresa:", it_companies[0])
print("Segunda empresa:", it_companies[1])
print("Última empresa:", it_companies[-1])

# Modificar una empresa en la lista
it_companies[2] = "Tesla"
print("Lista después de modificar una empresa:" , it_companies)

# Añadir una empresa de TI a it_companies
it_companies.append("Samsung")
print("Lista después de añadir una empresa:", it_companies)

# Insertar una empresa en el medio
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, "Intel")
print("Lista después de insertar una empresa en el medio:", it_companies)

# Cambiar uno de los nombres a mayúsculas (IBM excluido)
it_companies[1] = it_companies[1].upper()
print("Lista con una empresa en mayúsculas:", it_companies)

# Unir it_companies con una cadena '#; '
joined_companies = "#; ".join(it_companies)
print("Empresas unidas:", joined_companies)

# Comprobar si una empresa existe en la lista
company_to_check = "Google"
exists = company_to_check in it_companies
print(f"¿{company_to_check} está en la lista?", exists)

# Ordenar la lista
it_companies.sort()
print("Lista ordenada:", it_companies)

# Invertir la lista
it_companies.reverse()
print("Lista en orden descendente:", it_companies)

# Separar las primeras 3 empresas
first_three = it_companies[:3]
print("Primeras tres empresas:", first_three)

# Eliminar las últimas 3 empresas
it_companies = it_companies[:-3]
print("Lista después de eliminar las últimas 3 empresas:", it_companies)

# Eliminar las empresas intermedias
middle_index = len(it_companies) // 2
del it_companies[middle_index]
print("Lista después de eliminar la empresa intermedia:", it_companies)

# Eliminar la primera empresa de TI
del it_companies[0]
print("Lista después de eliminar la primera empresa:", it_companies)

# Eliminar la empresa intermedia de la lista (otra vez)
middle_index = len(it_companies) // 2
del it_companies[middle_index]
print("Lista después de eliminar otra empresa intermedia:", it_companies)

# Eliminar la última empresa de la lista
it_companies.pop()
print("Lista después de eliminar la última empresa:", it_companies)

# Eliminar todas las empresas de la lista
it_companies.clear()
print("Lista después de eliminar todas las empresas:", it_companies)

# Destruir la lista
del it_companies

# Unir listas front_end y back_end
front_end = ('HTML', 'CSS', 'JS', 'React', 'Redux')
back_end = ('Node', 'Express', 'MongoDB')

# Convertir las tuplas en listas y unirlas
full_stack = list(front_end) + list(back_end)
print("Full stack antes de modificaciones:", full_stack)

# Insertar Python y SQL después de Redux
redux_index = full_stack.index("Redux") + 1
full_stack[redux_index:redux_index] = ["Python", "SQL"]
print("Full stack después de insertar Python y SQL:", full_stack)


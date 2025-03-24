import random

# Función que baraja una lista y devuelve una versión aleatoria de la misma
def shuffle_list(lista):
    lista_copiada = lista[:]  # Se crea una copia para no modificar la original
    random.shuffle(lista_copiada)  # Se mezcla aleatoriamente
    return lista_copiada

print(shuffle_list([1, 2, 3, 4, 5])) 


# Función que genera una lista de 7 números únicos entre 0 y 9
def unique_random_numbers():
    return random.sample(range(10), 7)  # sample selecciona 7 números sin repetición

print(unique_random_numbers()) 
import random
import string

# Función que genera un ID aleatorio de seis caracteres
def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

print(random_user_id())  


# Función que genera múltiples ID según la cantidad de caracteres y el número de ID deseados
def user_id_gen_by_user():
    caracteres = int(input("Ingrese el número de caracteres por ID: "))
    cantidad = int(input("Ingrese el número de ID a generar: "))
    
    return [''.join(random.choices(string.ascii_letters + string.digits, k=caracteres)) for _ in range(cantidad)]

print(user_id_gen_by_user())  

# Función que genera un color RGB aleatorio
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(rgb_color_gen()) 

# Función que suma dos números
def add_two_numbers(a, b):
    return a + b

print(add_two_numbers(3, 7))  # 10


# Función que calcula el área de un círculo
import math
def area_del_circulo(r):
    return math.pi * r * r

print(area_del_circulo(5)) 


# Función que suma todos los números pasados como argumento
def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):  # Verifica si todos son números
        return sum(args)
    else:
        return "Error: Todos los elementos deben ser números."

print(add_all_nums(1, 2, 3, 4))  
print(add_all_nums(1, "dos", 3))  


# Función que convierte grados Celsius a Fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(convert_celsius_to_fahrenheit(25))  


# Función que devuelve la estación del año según el mes
def check_season(mes):
    estaciones = {
        "Invierno": ["diciembre", "enero", "febrero"],
        "Primavera": ["marzo", "abril", "mayo"],
        "Verano": ["junio", "julio", "agosto"],
        "Otoño": ["septiembre", "octubre", "noviembre"]
    }
    for estacion, meses in estaciones.items():
        if mes.lower() in meses:
            return estacion
    return "Mes inválido"

print(check_season("junio"))


# Función que calcula la pendiente de una ecuación lineal (m = (y2 - y1) / (x2 - x1))
def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return "La pendiente es indefinida (división por cero)."
    return (y2 - y1) / (x2 - x1)

print(calculate_slope(2, 3, 5, 7))  # 1.333...


# Función que resuelve ecuaciones cuadráticas ax² + bx + c = 0
import cmath  # Para manejar raíces complejas
def solve_quadratic_eqn(a, b, c):
    discriminante = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b + discriminante) / (2*a)
    x2 = (-b - discriminante) / (2*a)
    return x1, x2

print(solve_quadratic_eqn(1, -3, 2))  


# Función que imprime cada elemento de una lista
def print_list(lista):
    for item in lista:
        print(item)

print_list(["Hola", "Mundo", "!"])  # Imprime cada elemento en una línea


# Función que invierte una lista usando un bucle
def reverse_list(lista):
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

print(reverse_list([1, 2, 3, 4, 5])) 
print(reverse_list(["A", "B", "C"])) 


# Función que capitaliza cada elemento de una lista
def capitalize_list_items(lista):
    return [item.upper() for item in lista]

print(capitalize_list_items(["hola", "mundo"])) 


# Función que agrega un elemento a una lista
def add_item(lista, elemento):
    lista.append(elemento)
    return lista

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))  
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))


# Función que elimina un elemento de una lista
def remove_item(lista, elemento):
    if elemento in lista:
        lista.remove(elemento)
    return lista

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3)) 


# Función que suma los números en un rango desde 1 hasta n
def sum_of_numbers(n):
    return sum(range(1, n + 1))

print(sum_of_numbers(5))  
print(sum_of_numbers(10))  
print(sum_of_numbers(100))  


# Función que suma solo los números impares en un rango
def suma_de_impares(n):
    return sum(i for i in range(1, n + 1) if i % 2 != 0)

print(suma_de_impares(10))  


# Función que suma solo los números pares en un rango
def suma_de_numeros_pares(n):
    return sum(i for i in range(1, n + 1) if i % 2 == 0)

print(suma_de_numeros_pares(10))  

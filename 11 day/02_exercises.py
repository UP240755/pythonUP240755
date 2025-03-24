# Función que cuenta la cantidad de números pares e impares hasta un número dado
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)  # Contar números pares
    odds = sum(1 for i in range(n + 1) if i % 2 != 0)  # Contar números impares
    print(f"The number of odds are {odds}.")
    print(f"The number of evens are {evens}.")

evens_and_odds(100)
# The number of odds are 50.
# The number of evens are 51.


# Función que calcula el factorial de un número entero
def factorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

print(factorial(5))  # 120


# Función que verifica si un parámetro está vacío
def is_empty(valor):
    return not bool(valor)

print(is_empty([]))  # True
print(is_empty("Hola"))  # False
print(is_empty(0))  # True
print(is_empty(None))  # True


# Importamos estadísticas para algunos cálculos avanzados
import statistics

# Función que calcula la media (promedio) de una lista
def calcular_media(lista):
    return sum(lista) / len(lista) if lista else None

# Función que calcula la mediana de una lista
def calcular_mediana(lista):
    return statistics.median(lista) if lista else None

# Función que calcula la moda de una lista
def calcular_moda(lista):
    try:
        return statistics.mode(lista)
    except statistics.StatisticsError:
        return "No hay una moda única."

# Función que calcula el rango (diferencia entre el máximo y mínimo)
def calcular_rango(lista):
    return max(lista) - min(lista) if lista else None

# Función que calcula la varianza de una lista
def calcular_varianza(lista):
    return statistics.variance(lista) if len(lista) > 1 else None

# Función que calcula la desviación estándar de una lista
def calcular_desviacion_estandar(lista):
    return statistics.stdev(lista) if len(lista) > 1 else None

# Lista de prueba
numeros = [10, 20, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Media:", calcular_media(numeros))  # 50.0
print("Mediana:", calcular_mediana(numeros))  # 50
print("Moda:", calcular_moda(numeros))  # 20
print("Rango:", calcular_rango(numeros))  # 90
print("Varianza:", calcular_varianza(numeros))  # 1000
print("Desviación estándar:", calcular_desviacion_estandar(numeros))  # 31.62

import random

# Función que genera una lista de colores en formato hexadecimal
def list_of_hexa_colors(cantidad):
    return [f"#{''.join(random.choices('0123456789abcdef', k=6))}" for _ in range(cantidad)]

print(list_of_hexa_colors(3))  


# Función que genera una lista de colores en formato RGB
def list_of_rgb_colors(cantidad):
    return [f"rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})" for _ in range(cantidad)]

print(list_of_rgb_colors(3)) 


# Función que genera colores en formato hexadecimal o RGB según la solicitud
def generate_colors(tipo, cantidad):
    if tipo == "hexa":
        return list_of_hexa_colors(cantidad)
    elif tipo == "rgb":
        return list_of_rgb_colors(cantidad)
    else:
        return "Tipo no válido. Use 'hexa' o 'rgb'."

print(generate_colors('hexa', 3))  # ['#a3e12f', '#03ed55', '#eb3d2b']
print(generate_colors('hexa', 1))  # ['#b334ef']
print(generate_colors('rgb', 3))   # ['rgb(5, 55, 175)', 'rgb(50, 105, 100)', 'rgb(15, 26, 80)']
print(generate_colors('rgb', 1))   # ['rgb(33,79, 176)']

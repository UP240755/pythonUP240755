# Crear un diccionario vacío llamado perro
perro = {}

# Añadir nombre, color, raza, patas y edad al diccionario de perros
perro["nombre"] = "Firulais"
perro["color"] = "Marrón"
perro["raza"] = "Labrador"
perro["patas"] = 4
perro["edad"] = 3

print("Diccionario de perro:", perro)

# Crear un diccionario de estudiante con varias claves
estudiante = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "género": "Masculino",
    "edad": 21,
    "estado_civil": "Soltero",
    "habilidades": ["Python", "Java"],
    "país": "México",
    "ciudad": "Ciudad de México",
    "dirección": "Calle 123, Colonia Centro"
}

# Obtener la longitud del diccionario de estudiante
print("\nLongitud del diccionario de estudiante:", len(estudiante))

# Obtener el valor de las habilidades y verificar el tipo de dato
habilidades = estudiante["habilidades"]
print("\nHabilidades del estudiante:", habilidades)
print("Tipo de dato de habilidades:", type(habilidades))

# Modificar los valores de las habilidades agregando más habilidades
estudiante["habilidades"].append("JavaScript")
estudiante["habilidades"].append("SQL")
print("\nHabilidades actualizadas:", estudiante["habilidades"])

# Obtener las claves del diccionario como una lista
claves = list(estudiante.keys())
print("\nClaves del diccionario de estudiante:", claves)

# Obtener los valores del diccionario como una lista
valores = list(estudiante.values())
print("\nValores del diccionario de estudiante:", valores)

# Cambiar el diccionario a una lista de tuplas usando items()
tuplas = list(estudiante.items())
print("\nDiccionario como lista de tuplas:", tuplas)

# Eliminar uno de los elementos del diccionario
del estudiante["estado_civil"]
print("\nDiccionario después de eliminar 'estado_civil':", estudiante)

# Eliminar uno de los diccionarios
del perro
print("\nEl diccionario 'perro' ha sido eliminado.")

def calificar_estudiante(puntuacion):
    if 80 <= puntuacion <= 100:
        return 'A'
    elif 70 <= puntuacion <= 79:
        return 'B'
    elif 60 <= puntuacion <= 69:
        return 'C'
    elif 50 <= puntuacion <= 59:
        return 'D'
    else:
        return 'F'

def verificar_estacion(mes):
    estaciones = {
        'otoño': ['septiembre', 'octubre', 'noviembre'],
        'invierno': ['diciembre', 'enero', 'febrero'],
        'primavera': ['marzo', 'abril', 'mayo'],
        'verano': ['junio', 'julio', 'agosto']
    }
    for estacion, meses in estaciones.items():
        if mes.lower() in meses:
            return estacion
    return 'Mes no válido'

def agregar_fruta(fruta, lista_frutas):
    if fruta.lower() in lista_frutas:
        print('Esa fruta ya existe en la lista')
    else:
        lista_frutas.append(fruta.lower())
        print('Lista modificada:', lista_frutas)

def analizar_persona(persona):
    if 'skills' in persona:
        skills = persona['skills']
        if skills:
            print("Habilidad del medio:", skills[len(skills) // 2])
        print("Tiene Python:", 'Python' in skills)
        
        if set(skills) == {'JavaScript', 'React'}:
            print('Es un desarrollador front end')
        elif {'Node', 'Python', 'MongoDB'}.issubset(skills):
            print('Es un desarrollador backend')
        elif {'React', 'Node', 'MongoDB'}.issubset(skills):
            print('Es un desarrollador fullstack')
        else:
            print('Título desconocido')
    
    if persona.get('is_marred') and persona.get('country') == 'Finland':
        print(f"{persona['first_name']} {persona['last_name']} vive en Finlandia. Está casado.")

# Ejemplo de uso:
puntuacion = int(input("Ingrese la puntuación del estudiante: "))
print("Calificación:", calificar_estudiante(puntuacion))

mes = input("Ingrese un mes: ")
print("Estación:", verificar_estacion(mes))

frutas = ['banana', 'naranja', 'mango', 'limon']
fruta = input("Ingrese una fruta: ")
agregar_fruta(fruta, frutas)

persona = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

analizar_persona(persona)

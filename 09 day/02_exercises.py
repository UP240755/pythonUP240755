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

# Ejemplo de uso:
puntuacion = int(input("Ingrese la puntuación del estudiante: "))
print("Calificación:", calificar_estudiante(puntuacion))

mes = input("Ingrese un mes: ")
print("Estación:", verificar_estacion(mes))

frutas = ['banana', 'naranja', 'mango', 'limon']
fruta = input("Ingrese una fruta: ")
agregar_fruta(fruta, frutas)

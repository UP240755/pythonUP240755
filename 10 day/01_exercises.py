#Iterar del 0 al 10 usando for y while

# Usando for
for i in range(11):
    print(i)

# Usando while
i = 0
while i <= 10:
    print(i)
    i += 1

#Imprimir el triángulo
for i in range(1, 8):
    print("#" * i)

#Crear una cuadrícula de #
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()

#Imprimir el patrón de multiplicaciones
for i in range(11):
    print(f"{i} x {i} = {i * i}")

#Iterar sobre la lista e imprimir los elementos
techs = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tech in techs:
    print(tech)
#Imprimir solo los números pares del 0 al 100
for i in range(0, 101, 2):
    print(i)

#Imprimir solo los números impares del 0 al 100
for i in range(1, 101, 2):
    print(i)
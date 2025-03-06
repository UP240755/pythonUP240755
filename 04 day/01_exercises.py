
# Concatenar las palabras en una sola cadena
treinta = "Thirty "
dias = "Days "
de = "Of "
python = "Python"
string = treinta + dias + de + python
print(string)  # 'Thirty Days Of Python'

# Concatenar 'Coding', 'For', 'All' en una sola cadena
codificacion = "Coding "
para = "For "
todos = "All"
string2 = codificacion + para + todos
print(string2)  # 'Coding For All'

# Declarar la variable company y asignarle el valor 'Coding For All'
company = string2

# Imprimir la variable company
print(company)

# Imprimir la longitud de la cadena company
print(len(company))

# Convertir la cadena a mayúsculas
print(company.upper())

# Convertir la cadena a minúsculas
print(company.lower())

# Usar métodos para formatear la cadena
print(company.capitalize())  # Primera letra en mayúscula
print(company.title())  # Primera letra de cada palabra en mayúscula
print(company.swapcase()) 

# Cortar la primera palabra de 'Coding For All'
print(company[7:]) 

# Comprobar si la cadena contiene la palabra "Coding"
print("Coding" in company)

# Reemplazar la palabra "Coding" por "Python"
print(company.replace("Coding", "Python"))

# Cambiar "Python for Everyone" a "Python for All"
frase = "Python for Everyone"
print(frase.replace("Everyone", "All"))

# Dividir la cadena 'Coding For All' usando el espacio como separador
print(company.split())

# Dividir la cadena en una lista separada por comas
empresas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(empresas.split(", "))

# Obtener el carácter en el índice 0 de 'Coding For All'
print(company[0])  #'C'

# Obtener el último índice de la cadena
print(len(company) - 1)

# Obtener el carácter en el índice 10
print(company[10])

# Crear acrónimo para 'Python For Everyone'
pfe = ''.join([palabra[0] for palabra in "Python For Everyone".split()])
print(pfe)  

# Crear acrónimo para 'Coding For All'
cfa = ''.join([palabra[0] for palabra in company.split()])
print(cfa)  

# Encontrar la posición del primer 'C' en 'Coding For All'
print(company.index('C'))

# Encontrar la posición del primer 'F' en 'Coding For All'
print(company.index('F'))

# Encontrar la última aparición de 'l' en 'Coding For All People'
frase = "Coding For All People"
print(frase.rfind('l'))

# Encontrar la primera aparición de 'because' en la oración
oracion = "You cannot end a sentence with because because because is a conjunction"
print(oracion.find("because"))

# Encontrar la última aparición de 'because'
print(oracion.rindex("because"))

# Cortar la frase 'because because because' de la oración
inicio = oracion.find("because because because")
fin = inicio + len("because because because")
print(oracion[:inicio] + oracion[fin:])

# ¿Empieza 'Coding For All' con 'Coding'?
print(company.startswith("Coding"))

# ¿Termina 'Coding For All' con 'coding'?
print(company.endswith("coding"))

# Eliminar espacios en los extremos
cadena_con_espacios = "   Coding For All      "
print(cadena_con_espacios.strip())

# Verificar si las variables son identificadores válidos
print("30DaysOfPython".isidentifier())  
print("thirty_days_of_python".isidentifier())  

# Unir nombres de librerías de Python con '# '
librerias_python = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(librerias_python))

#Utilizar la secuencia de escape de nueva línea para separar las siguientes oraciones.
"'I am enjoying this challenge."
"I just wonder what is next.'"
print("I am enjoying this challenge.\nI just wonder what is next.")

#Utilizar una secuencia de escape de tabulación para escribir las siguientes líneas.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
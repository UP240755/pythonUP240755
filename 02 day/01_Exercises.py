first_name = 'steven'
last_name = 'montoya'
country = 'México'
city = 'aguascalientes'
age = 19
año = 2006
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Steven', 
    'lastname': 'Montoya', 
    'country': 'México',
    'city': 'Aguascalientes'
}

print('Nombre:', first_name)
print('Longitud del nombre:', len(first_name))
print('Apellido:', last_name)
print('Longitud del apellido:', len(last_name))
print('País:', country)
print('Ciudad:', city)
print('Edad:', age)
print('Casado:', is_married)
print('Habilidades:', skills)
print('Información de la persona:', person_info)


first_name, last_name, country, age, is_married = 'Steven', 'Montoya', 'México', 19, False

print(first_name, last_name, country, age, is_married)
print('Nombre:', first_name)
print('Apellido:', last_name)
print('País:', country)
print('Edad:', age)
print('Casado:', is_married)
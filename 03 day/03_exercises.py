print('Suma: ', 1 + 2)
print('Resta: ', 2 - 1)
print('Multiplicación: ', 2 * 3)
print('División: ', 4 / 2)                      
print('División: ', 6 / 2)
print('División: ', 7 / 2)
print('División sin el residuo: ', 7 // 2)
print('Módulo: ', 3 % 2)                     
print('División sin el residuo: ', 7 // 3)
print('Exponencial: ', 3 ** 2)              

print('Número flotante, PI', 3.14)
print('Número flotante, gravedad', 9.81)

print('Número complejo: ', 1 + 1j)
print('Multiplicación de números complejos: ', (1 + 1j) * (1 - 1j))


a = 3 
b = 2 

total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print(total) 
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

"Declarando valores y organizándolos juntos"
num_one = 3
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

print('total: ', total)
print('diferencia: ', diff)
print('producto: ', product)
print('división: ', div)
print('residuo: ', remainder)


import math
radius = 30                                
area_of_circle = 3.14 * radius ** 2        
print('Área de un círculo:', area_of_circle)


length = 40
width = 20
area_of_rectangle = length * width
print('Área del rectángulo:', area_of_rectangle)

"Calculando el peso de un objeto"
mass = 60
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)    
print(3 >= 2)   
print(3 < 2)    
print(2 < 3)    
print(2 <= 3)   
print(3 == 2)    
print(3 != 2)  
print(len('mango') == len('aguacate')) 
print(len('mango') != len('aguacate')) 
print(len('mango') < len('aguacate')) 
print(len('leche') != len('carne'))     
print(len('leche') == len('carne'))      
print(len('jitomate') == len('papa'))  
print(len('python') > len('dragon'))   

"Comparación"
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True y True: ', True and True)
print('True o False:', True or False)


print('1 es 1', 1 is 1)                 
print('1 no es 2', 1 is not 2)         
print('A en Steven', 'A' in 'Steven') 
print('B en Steven', 'B' in 'Steven')
print('coding en "coding for all"', 'coding' in 'coding for all') 
print('"a" en "an":', 'a' in 'an')     
print('4 es 2 ** 2:', 4 is 2 ** 2)  
print(3 > 2 and 4 > 3) 
print(3 > 2 and 4 < 3) 
print(3 < 2 and 4 < 3) 
print(3 > 2 or 4 > 3)  
print(3 > 2 or 4 < 3) 
print(3 < 2 or 4 < 3) 
print(not 3 > 2)     
print(not True)      
print(not False)     
print(not not True)  
print(not not False)
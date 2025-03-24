#Sumar todos los números del 0 al 100
total_sum = 0
for i in range(101):
    total_sum += i
print(f"The sum of all numbers is {total_sum}.")

#Sumar los números pares e impares por separado
even_sum = 0
odd_sum = 0

for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.")
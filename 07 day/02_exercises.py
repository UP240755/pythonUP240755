# Definir los conjuntos A y B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Unir A y B
union_AB = A.union(B)  # También se puede usar A | B
print("Unión de A y B:", union_AB)

# Encuentra la intersección de A y B
interseccion_AB = A.intersection(B)  # También se puede usar A & B
print("Intersección de A y B:", interseccion_AB)

# Verificar si A es un subconjunto de B
es_subconjunto = A.issubset(B)
print("¿A es un subconjunto de B?", es_subconjunto)

# Verificar si A y B son conjuntos disjuntos
son_disjuntos = A.isdisjoint(B)  # Devuelve True si no tienen elementos en común
print("¿A y B son disjuntos?", son_disjuntos)

# Unir A con B y B con A (es lo mismo)
A_union_B = A.union(B)
B_union_A = B.union(A)
print("Unión A con B:", A_union_B)
print("Unión B con A:", B_union_A)

# Diferencia simétrica entre A y B (elementos que están en A o B, pero no en ambos)
diferencia_sim_AB = A.symmetric_difference(B)  # También se puede usar A ^ B
print("Diferencia simétrica entre A y B:", diferencia_sim_AB)

# Eliminar los conjuntos por completo
del A
del B
# print(A, B)  # Esto generaría un error porque los conjuntos ya no existen
print("Los conjuntos A y B han sido eliminados.")
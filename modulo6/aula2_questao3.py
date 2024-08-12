import random

lista1 = [random.randint(0,50) for i in range(20)]
lista2 = [random.randint(0,50) for i in range(20)]

print(sorted(lista1))
print(sorted(lista2))

interseccao = []
for elemento in lista1:
    if elemento in lista2 and elemento not in interseccao:
        interseccao.append(elemento)

print(sorted(interseccao))

for i in interseccao:
    print(f'{i}: ({lista1.count(i)}, {lista2.count(i)})')
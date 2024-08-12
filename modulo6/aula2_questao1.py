import random

lista = [random.randint(-100, 100) for i in range(20)]

print('Resultado:')
print(sorted(lista))
print(lista)
print(max(lista))
print(min(lista))


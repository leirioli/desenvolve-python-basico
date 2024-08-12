import random

num_elementos = random.randint(5, 20)


elementos = [random.randint(1, 10) for i in range(num_elementos)]

soma = sum(elementos)

media = sum(elementos)/len(elementos)

print(elementos)
print(soma)
print(media)
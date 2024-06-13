import random
import math

n = int(input('Digite um valor: '))

valores = [random.randint(0, 100) for i in range(n)]

soma = sum(valores)

raiz_quad = math.sqrt(soma)

print(raiz_quad)



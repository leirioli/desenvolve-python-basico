
lista = list()
print('Digite quantos números quiser, desde que sejam inteiros e no mínimo de 4 valores. Quando terminar digite "sair":')
while True:
    entrada = input()
    if entrada == 'sair':
        break
    else:
        num = int(entrada)
        lista.append(num)


print(lista)
print(lista[0:3])
print(lista[-2:])
print(lista[::-1])
print(lista[::2])
print(lista[1::2]) 


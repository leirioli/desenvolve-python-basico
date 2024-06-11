N = int(input("Quantas pessoas irão responder?: "))
soma = 0
cont = 0
while cont < N:
    idade = int(input(f"Qual a idade do respondente?: "))
    soma += idade
    cont += 1

media = soma/N

print(f"Média: {media}")
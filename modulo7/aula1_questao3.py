frase = input('Digite uma frase: ')

espacosbrancos = 0

for espaco in frase:
    if espaco == ' ':
        espacosbrancos += 1

print(f'Número de espaços brancos: {espacosbrancos}')
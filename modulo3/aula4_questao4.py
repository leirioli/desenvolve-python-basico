distancia = int(input('distância em KM: '))
peso = float(input('peso do pacote em KG: '))

if distancia <= 100:
    frete = 1 * peso
elif distancia >= 101 and distancia <= 300:
    frete = 1.50 * peso
else:
    frete = 2 * peso

if peso > 10:
    print(f'O valor do frete é: {frete+10} reais')
else:
    print(f'O valor do frete é: {frete} reais')


frase = input('Digite uma frase: ')

vogais = ['a', 'e', 'i', 'o', 'u']

frase_modificada = frase

for vogal in vogais:
    frase_modificada = frase_modificada.replace(vogal, '*')
    frase_modificada = frase_modificada.replace(vogal.upper(), '*')

print(frase)
print(frase_modificada)
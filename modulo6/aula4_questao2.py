vogais = 'aeiou'
consoantes = 'bcdfghjklmnpqrstvwxyz'
frase = input('Digite uma frase: ')

lista_vogais = [l for l in frase if l in vogais]

lista_consoantes = [l for l in frase if l in consoantes]

print(lista_vogais)
print(lista_consoantes)
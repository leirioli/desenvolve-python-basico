qntReais = int(input("digite um valor:"))
# de 100
notade100 = qntReais // 100
qntReais %= 100
# de 50
notade50 = qntReais // 50
qntReais %= 50
# de 20
notade20 = qntReais // 20
qntReais %= 20
# de 10
notade10 = qntReais // 10
qntReais %= 10
# de 5
notade5 = qntReais // 5
qntReais %= 5
# de 2
notade2 = qntReais // 2
qntReais %= 2
# de 1
notade1 = qntReais // 1
qntReais %= 1

# resultado
print(f'{notade100} notas(s) de R$100,00')
print(f'{notade50} notas(s) de R$50,00')
print(f'{notade20} notas(s) de R$20,00')
print(f'{notade10} notas(s) de R$10,00')
print(f'{notade5} notas(s) de R$5,00')
print(f'{notade2} notas(s) de R$2,00')
print(f'{notade1} notas(s) de R$1,00')

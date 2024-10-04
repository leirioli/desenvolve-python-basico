pares = [i for i in range(20,51) if i % 2 == 0]

quadrados = [a**2 for a in range(1,10)]

divisiveis = [e for e in range(1,101) if e % 7 == 0]

par_ou_impar = ['par' if u % 2 == 0 else 'impar' for u in range(0,30,3)]

print(f'Os pares da lista: {pares}')
print(f'Quadrados da lista: {quadrados}')
print(f'Divisíveis por 7: {divisiveis}')
print(f'Escrito par ou impar: {par_ou_impar}')
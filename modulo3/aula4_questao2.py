user = int(input('Avalie o filme de 1 a 5: '))

if user == 5:
    print('Excelente!')
elif user == 4:
    print('Muito Bom!')
elif user == 3:
    print('Bom!')
elif user == 2:
    print('Regular.')
elif user == 1:
    print('Ruim.')
else:
    print('Inválido')
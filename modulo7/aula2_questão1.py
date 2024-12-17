meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

data_nascimento = input('Digite sua data de nascimento (dd/mm/aaaa): ')
dia, mes, ano = data_nascimento.split('/')

nomedomes = meses[int(mes) - 1]

print(data_nascimento)
print(f'Você nasceu em {dia} de {nomedomes} de {ano}.')
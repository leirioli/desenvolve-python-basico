#entrada de dados
user = str(input('Qual o seu gênero? (Responda com "F" para feminino ou "M" para masculino): '))
idade = int(input('Qual a sua idade?: '))
servico = int(input('Qual o seu tempo de serviço?: '))

#processamento
a = (user == 'F' and idade >= 60) or (user == 'M' and idade >= 65)
b = servico > 30
c = idade >= 60 and servico >= 25

aposentar = a or b or c

#saída 
print(aposentar)
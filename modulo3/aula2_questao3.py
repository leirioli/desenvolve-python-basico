#entrada de dados
user = int(input('Digite sua idade: '))
qntsJogos = bool(input('Já jogou 3 jogos? (Digite True pra sim e False para não): '))
qntsWin = int(input('Quantas vezes ganhou um jogo?: '))

# condições
# 1 - se tiver entre 16 e 18 anos
# 2 - já tiver jogado pelo menos 3 jogos
# 3 - já ter vencido pelo menos 1 jogo

#processamento
apto_para_entrar = (user >= 16 and user <= 18) and (qntsJogos) and (qntsWin > 1)

#saída
print(f'Apto para ingressar no clube de jogos de tabuleiro: {apto_para_entrar}')
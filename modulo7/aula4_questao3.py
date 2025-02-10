import re

f = open('estomago.txt')
linhas = f.readlines()
total = 0

linha_mais_longa = max(linhas, key=len)

texto_completo = " ".join(linhas)    
contagem_nonato = len(re.findall(r'\b[nN]onato\b', texto_completo))
contagem_iria = len(re.findall(r'\b[iÍí]ria\b', texto_completo))

print('Primeiras 25 linhas: ', linhas[:25])
print('Número de linhas: ', len(linhas))
print('Linha mais longa: ', linha_mais_longa)
print("Menções ao personagem 'Nonato':", contagem_nonato)
print("Menções ao personagem 'Íria':", contagem_iria)
# entrada de dados
comprimento = int(input("qual o comprimento?"))
largura = int(input("qual a largura?"))
preço = float(input("qual o preço?"))

# cálculo da área
area_m2 = comprimento * largura

# cálculo do preço total

preco_total = preço * area_m2

# impressão do resultado

print(f'O terreno possui {area_m2}m2 e custa R${preço:,.2f}')
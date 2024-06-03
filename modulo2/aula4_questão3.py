# produto 1
nome_produto1 = str(input("informe o nome do produto"))
preço_produto1 = float(input("informe o preço unitário do produto"))
qtd_produto1 = int(input("informe a quantidade do produto"))

# produto 2
nome_produto2 = str(input("informe o nome do produto"))
preço_produto2 = float(input("informe o preço unitário do produto"))
qtd_produto2 = int(input("informe a quantidade do produto"))

# produto 3 

nome_produto3 = str(input("informe o nome do produto"))
preço_produto3 = float(input("informe o preço unitário do produto"))
qtd_produto3 = int(input("informe a quantidade do produto"))

# resultado 

print(f'Total: R${(qtd_produto1*preço_produto1)+(qtd_produto2*preço_produto2)+(qtd_produto3*preço_produto3):,.2f}') 
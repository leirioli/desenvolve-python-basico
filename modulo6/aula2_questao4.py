def intercalar_listas(lista1, lista2):
    lista_intercalada = []
    tamanho1 = len(lista1)
    tamanho2 = len(lista2)
    
    for i in range(min(tamanho1, tamanho2)):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
    
    if tamanho1 > tamanho2:
        lista_intercalada.extend(lista1[tamanho2:])
    else:
        lista_intercalada.extend(lista2[tamanho1:])
    
    return lista_intercalada

qtd1 = int(input("Digite a quantidade de elementos da lista 1:"))
lista1 = []
print(f"Digite os {qtd1} elementos da lista 1:")
for i in range(qtd1):
    lista1.append(int(input()))

qtd2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = []
print(f"Digite os {qtd2} elementos da lista 2:")
for i in range(qtd2):
    lista2.append(int(input()))

lista_intercalada = intercalar_listas(lista1, lista2)

print(f'Lista intercalada:{lista_intercalada}')
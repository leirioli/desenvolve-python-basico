#entrada de dados
classe = str(input('Escolha uma classe: guerreiro, mago ou arqueiro: '))
pontos_forca = int(input('Digite os pontos de força (de 1 a 20): '))
pontos_magia = int(input('Digite os pontos de magia (1 a 20): '))

#processamento e saída
if classe == "guerreiro":
    if pontos_forca >= 15 and pontos_magia <= 10:
        print("Pontos de atributo consistentes com a classe escolhida: True")
    else:
        print("Pontos de atributo consistentes com a classe escolhida: False")
elif classe == "mago":
    if pontos_forca <= 10 and pontos_magia >= 15:
        print("Pontos de atributo consistentes com a classe escolhida: True")
    else:
        print("Pontos de atributo consistentes com a classe escolhida: False")
elif classe == "arqueiro":
    if 5 < pontos_forca <= 15 and 5 < pontos_magia <= 15:
        print("Pontos de atributo consistentes com a classe escolhida: True")
    else:
        print("Pontos de atributo consistentes com a classe escolhida: False")
        
        
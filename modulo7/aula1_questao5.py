def contar_vogais(frase):
    vogais = "aeiou"
    indices_vogais = []
    
    for i, letra in enumerate(frase):
        if letra.lower() in vogais:
            indices_vogais.append(i)
    
    print(f"{len(indices_vogais)} vogais")
    print(f"Índices {indices_vogais}")

frase = input("Digite uma frase: ")
contar_vogais(frase)
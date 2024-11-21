from collections import Counter

def encontrar_anagramas(frase, palavra_objetivo):
    contador_objetivo = Counter(palavra_objetivo)
    anagramas = []
    
    palavras = frase.split()
    
    for palavra in palavras:
        if Counter(palavra.lower()) == contador_objetivo:
            anagramas.append(palavra)
    
    return anagramas

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

anagramas = encontrar_anagramas(frase, palavra_objetivo)

print("Anagramas:", anagramas)
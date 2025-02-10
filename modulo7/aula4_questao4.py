import random

def carregar_palavra(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        palavras = [linha.strip().lower() for linha in arquivo if linha.strip()]
    return random.choice(palavras) if palavras else None

def carregar_enforcado(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        return arquivo.read().split("\n\n")

def imprime_enforcado(erros, estagios):
    print(estagios[min(erros, len(estagios) - 1)])

def jogar_forca():
    palavra = carregar_palavra("gabarito_forca.txt")
    estagios = carregar_enforcado("gabarito_enforcado.txt")
    
    if not palavra:
        print("Erro ao carregar palavras!")
        return

    letras_descobertas = ["_"] * len(palavra)
    letras_erradas = set()
    tentativas = 6  # Limite de tentativas
    
    print("\nJOGO DA FORCA!")
    print(" ".join(letras_descobertas))

    erros = 0
    while erros < tentativas and "_" in letras_descobertas:
        letra = input("\nDigite uma letra: ").lower().strip()

        if not letra.isalpha() or len(letra) != 1:
            print("Entrada inválida! Digite apenas uma letra.")
            continue

        if letra in letras_descobertas or letra in letras_erradas:
            print("Você já tentou essa letra. Escolha outra.")
            continue

        if letra in palavra:
            for i, char in enumerate(palavra):
                if char == letra:
                    letras_descobertas[i] = letra
        else:
            erros += 1
            letras_erradas.add(letra)

        imprime_enforcado(erros, estagios)
        print("Palavra:", " ".join(letras_descobertas))
        print(f"Letras erradas: {', '.join(letras_erradas)}")
    
    if "_" not in letras_descobertas:
        print("\nParabéns! Você acertou a palavra:", palavra.upper())
    else:
        print("\nVocê perdeu! A palavra era:", palavra.upper())

jogar_forca()
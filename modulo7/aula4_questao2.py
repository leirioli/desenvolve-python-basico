import re
import os

caminho_arquivo = os.path.join(os.getcwd(), "frase.txt")

with open(caminho_arquivo, 'r', encoding="utf-8") as f:
    ler = f.read()

conteudo_limpo = re.sub(r"[^A-Za-zÀ-ÿ ]", "", ler)
palavras = conteudo_limpo.split()

with open('palavras.txt', 'w', encoding="utf-8") as arquivo_palavras:
    for palavra in palavras:
        arquivo_palavras.write(palavra + "\n")

with open("palavras.txt", "r") as arquivo_palavras:
    conteudo = arquivo_palavras.read()

print("\n".join(palavras))
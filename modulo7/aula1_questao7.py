import random

def encrypt(nomes):
    chave_aleatoria = random.randint(1, 10)

    nomes_criptografados = []
    
    for nome in nomes:
        nome_criptografado = ''.join([chr((ord(c) + chave_aleatoria - 33) % 94 + 33) for c in nome])
        nomes_criptografados.append(nome_criptografado)

    return nomes_criptografados, chave_aleatoria

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

nomes_criptografados, chave_aleatoria = encrypt(nomes)

print(f"Chave de criptografia: {chave_aleatoria}")
print(f"Nomes criptografados: {nomes_criptografados}")
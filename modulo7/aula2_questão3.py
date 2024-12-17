import string

def verificar_palindromo(frase):
    frase = frase.lower()
    frase = frase.translate(str.maketrans("", "", string.punctuation))
    frase = frase.replace(" ", "")
    

    return frase == frase[::-1]

while True:

    frase = input("Digite uma frase (ou 'Fim' para encerrar): ")
    
    if frase.lower() == "fim":
        print("Programa encerrado.")
        break
    

    if verificar_palindromo(frase):
        print(f"{frase} é um palíndromo.")
    else:
        print(f"{frase} não é um palíndromo.")
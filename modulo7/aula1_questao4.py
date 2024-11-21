numero_input = input("Digite o número de celular: ")

numero = numero_input.replace("-", "")

if len(numero) == 8:
    numero = "9" + numero

elif len(numero) == 9:
    if numero[0] != "9":
        print("Número inválido, o primeiro dígito de um número com 9 dígitos deve ser 9.")
        exit()

else:
    print("Número inválido! O número de celular deve ter 8 ou 9 dígitos.")
    exit()

numero_formatado = numero[:5] + "-" + numero[5:]

print("Número formatado:", numero_formatado)
def validador_senha(senha):

    if len(senha) < 8:
        return "A senha deve ter pelo menos 8 caracteres."

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_caracter_especial = False
    caracteres_especiais = "!@#$%^&*(),.?\":{}|<>"

    for char in senha:
        if char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif char.isdigit():
            tem_numero = True
        elif char in caracteres_especiais:
            tem_caracter_especial = True


    if not tem_maiuscula:
        return False
    if not tem_minuscula:
        return False
    if not tem_numero:
        return False
    if not tem_caracter_especial:
        return False

    return True


senha = input("Digite a senha: ")
print(validador_senha(senha))
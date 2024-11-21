def calcular_digito_verificador(cpf_parcial):
    """Calcula o dígito verificador de um CPF parcial (com 9 ou 10 dígitos)."""

    multiplicadores_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma_1 = sum(int(cpf_parcial[i]) * multiplicadores_1[i] for i in range(9))
    resto_1 = soma_1 % 11
    digito_1 = 0 if resto_1 < 2 else 11 - resto_1

    cpf_parcial_2 = cpf_parcial + str(digito_1)  
    multiplicadores_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma_2 = sum(int(cpf_parcial_2[i]) * multiplicadores_2[i] for i in range(10))
    resto_2 = soma_2 % 11
    digito_2 = 0 if resto_2 < 2 else 11 - resto_2
    
    return digito_1, digito_2

def validar_cpf(cpf):
    """Valida um CPF no formato XXX.XXX.XXX-XX."""

    cpf = cpf.replace(".", "").replace("-", "")

    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"
    
    cpf_parcial = cpf[:9]
    digito_1, digito_2 = calcular_digito_verificador(cpf_parcial)
    
    if cpf[9] == str(digito_1) and cpf[10] == str(digito_2):
        return "Válido"
    else:
        return "Inválido"

cpf = input("Digite o CPF (formato XXX.XXX.XXX-XX): ")

resultado = validar_cpf(cpf)
print(resultado)
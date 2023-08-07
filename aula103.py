import random

for _ in range(100):
    cpf_nove_digitos = ''
    for i in range(9):
        cpf_nove_digitos += str(random.randint(0,9))


    base_dig_1 = 10
    soma_dig_1 = 0

    resultado_dig_1 = 0
    for digito in cpf_nove_digitos:
        soma_dig_1 += int(digito) * base_dig_1
        base_dig_1-=1
    resultado_dig_1 = (soma_dig_1 * 10) % 11
    resultado_dig_1 = resultado_dig_1 if resultado_dig_1 <=9 else 0
        

    cpf_dez_digitos = cpf_nove_digitos + str(resultado_dig_1)
    base_dig_2 = 11
    soma_dig_2 = 0

    resultado_dig_2 = 0
    for digito in cpf_dez_digitos:
        soma_dig_2 += int(digito) * base_dig_2
        base_dig_2-=1
    resultado_dig_2 = (soma_dig_2 * 10) % 11
    resultado_dig_2 = resultado_dig_2 if resultado_dig_2 <=9 else 0

    cpf_completo = cpf_dez_digitos+str(resultado_dig_2)

    print(cpf_completo)
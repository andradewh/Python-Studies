"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
cpf = '10079389945' ##dig 1 = 1 dig 2 = 9

cpf_nove_digitos = cpf[:9]
base_dig_1 = 10
soma_dig_1 = 0

resultado_dig_1 = 0
for digito in cpf_nove_digitos:
    soma_dig_1 += int(digito) * base_dig_1
    base_dig_1-=1
resultado_dig_1 = (soma_dig_1 * 10) % 11
resultado_dig_1 = resultado_dig_1 if resultado_dig_1 <=9 else 0
    
print(resultado_dig_1)

cpf_dez_digitos = cpf[:10]
base_dig_2 = 11
soma_dig_2 = 0

resultado_dig_2 = 0
for digito in cpf_dez_digitos:
    soma_dig_2 += int(digito) * base_dig_2
    base_dig_2-=1
resultado_dig_2 = (soma_dig_2 * 10) % 11
resultado_dig_2 = resultado_dig_2 if resultado_dig_2 <=9 else 0
    
print(resultado_dig_2)
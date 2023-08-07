"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
"""number = input('Enter a number:')
if number.isdigit():
    number_int = int(number)
    odd_even = number_int % 2 == 0
    odd_even_txt = "Odd"

    if odd_even:
        odd_even_txt = "Even"

    print(f'The number {number_int} is {odd_even_txt}')
else:
    print("The entered value is not a int")"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
"""input = input("Digite sua hora em inteiro: ")
try:
    time = int(input)
    if time >= 0 and time <= 11:
        print("Bom dia!")
    elif time >= 12 and time <= 17:
        print("Boa tarde!")
    elif time >= 18 and time <= 23:
        print("Boa noite!")
    else:
        print("Hora inválida")
except:
    print("Entrada invalida! Digite apenas números inteiros!")"""
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva ""Seu nome é muito grande"". 
"""
"""input = input("Digite seu primeiro nome: ")
input_len = len(input)

if input_len > 1:
    if input_len <= 4:
        print("Seu nome é curto!")
    elif input_len >=5 and input_len <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
else:
    print("Digite mais de uma letra!")"""

a = '123'

print(a)

a[2]= '456'

print(a)

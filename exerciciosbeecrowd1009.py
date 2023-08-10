'''
Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). 
Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.
'''
nome = input()
salario_fixo = float(input())
total_vendas = float(input())

total_mensal = (salario_fixo + (total_vendas * 0.15))

print(f'TOTAL = R$ {total_mensal:.2f}')
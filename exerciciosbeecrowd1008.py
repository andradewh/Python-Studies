'''
Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. 
A seguir, mostre o número e o salário do funcionário, com duas casas decimais.
'''
numero = int(input())
num_horas = int(input())
val_hora = float(input())

salario = (num_horas * val_hora)

print(f'NUMBER = {numero} \nSALARY = U$ {salario:.2f}')
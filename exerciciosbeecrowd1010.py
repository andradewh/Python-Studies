'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. 
Após, calcule e mostre o valor a ser pago.
'''
codigo = 0
num_pecas = 0
valor_unit = 0.0
valor_total = 0.0
pecas = []

for i in range(2):
    pecas = input().split(sep=' ')
    codigo = int(pecas[0])
    num_pecas = int(pecas[1])
    valor_unit = float(pecas[2])

    valor_total += (num_pecas * valor_unit)

print(f'VALOR A PAGAR: R$ {valor_total:.2f}')
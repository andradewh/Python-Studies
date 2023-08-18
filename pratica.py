import random 
lista_nomes = []

'''for i in range(4):
    lista_nomes.append(input(f'Digite um nome:'))
    i += 1
print(random.choice(lista_nomes))'''

while True:
    print('Deseja inserir um nome na lista? [s] [n]')
    resposta = input()
    if resposta == 's':
        lista_nomes.append(input(f'Digite um nome:'))
    else:
        break
print(random.choice(lista_nomes))
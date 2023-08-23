'''import random 
lista_nomes = []

for i in range(4):
    lista_nomes.append(input(f'Digite um nome:'))
    i += 1
print(random.choice(lista_nomes))

while True:
    print('Deseja inserir um nome na lista? [s] [n]')
    resposta = input()
    if resposta == 's':
        lista_nomes.append(input(f'Digite um nome:'))
    else:
        break
print(random.choice(lista_nomes))'''


'''nome = input('Digite seu nome: ')
print(nome.lower())
print(nome.upper())
print(len(nome.replace(" ", "")))
numid = nome.split()
i=0
while i < len(numid):
    print(numid[i])
    i+=1
'''

list = [1,2,3,4]

print(*list, sep='\n')
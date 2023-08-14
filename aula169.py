# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
from itertools import zip_longest

def zipper(list1,list2):
    interval = min(len(list1),len(list2))

    return [(list1[i],list2[i]) for i in range(interval)]


l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

#forma que fiz
print(zipper(l1,l2))
print()
#forma com zip
print(list(zip(l1,l2)))
print()
#forma com zip_longest
print(list(zip_longest(l1,l2, fillvalue='SEM CIDADE')))
"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
from itertools import zip_longest

#forma que fiz
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

menor_range = min(lista_a,lista_b)
lista_soma = list([lista_a[i]+lista_b[i] for i in range(len(menor_range))])

print(lista_soma)

#forma genérica
lista_soma = []

for i in range(len(lista_b)):
    lista_soma.append(lista_a[i]+lista_b[i])

print(lista_soma)

#forma python 1
lista_soma = []

for i, _ in enumerate(lista_b):
    lista_soma.append(lista_a[i]+lista_b[i])

print(lista_soma)

#forma escolhida pelo professor
lista_soma = list([x + y for x , y in zip(lista_a,lista_b)])

print(lista_soma)

##se quisesse usar a maior lista como parâmetro poderia usar o zip_longest
lista_soma = list([x + y for x , y in zip_longest(lista_a,lista_b, fillvalue=0)])

print(lista_soma)
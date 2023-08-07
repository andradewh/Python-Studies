## inverter listas

l = [1,2,3,4,5,6,7,8,9]
l1 = []
"""resolucao 1 criando outra lista
for i in l:
    l1.insert(0,i)
print(l1)"""

"""resolucao 2 usando reverse()
l.reverse()"""

"""resolucao 3 usando um range de metade da lista e com lógica de inversão
fim = len(l)-1
aux = 0
for i in range(len(l)//2):
    aux = l[i]
    l[i] = l[fim]
    l[fim] = aux
    fim -= 1"""

print(l)

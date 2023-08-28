import aula206_a as aula

dados = aula.ler(aula.bd,aula.CAMINHO)

p1 = aula.Pessoa(**dados[1])
p2 = aula.Pessoa(**dados[2])
p3 = aula.Pessoa(**dados[3])

print(p1.nome)
print(p2.nome)
print(p3.nome)

'''p2 = aula.Pessoa(**dados)
''''''
print(p2.get_dados())
'''
'''p2.nome = 'Thainá'

print(p2.get_dados())

print(vars(p2))'''
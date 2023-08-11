# copy, sorted, produtos.sort

from copy import deepcopy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = deepcopy(produtos)

for i, v in enumerate(novos_produtos):
    novos_produtos[i]['preco'] = round(novos_produtos[i]['preco'] * 1.1,2)
    
##print(novos_produtos[1])

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = deepcopy(sorted(produtos, key=lambda x: x['nome'], reverse=True))

print(*produtos_ordenados_por_nome,sep='\n')
print()

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = deepcopy(sorted(produtos, key=lambda x: x['preco']))

print(*produtos_ordenados_por_preco,sep='\n')
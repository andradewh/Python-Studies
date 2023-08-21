produtos = {
    '1': {'preco': 4.0},
    '2': {'preco': 4.5},
    '3': {'preco': 5.0},
    '4': {'preco': 2.0},
    '5': {'preco': 1.5},
}

pedido,quantidade = input().split(sep=' ')
resultado = produtos[pedido]['preco'] * int(quantidade)

print(f'Total: R$ {resultado:.2f}')
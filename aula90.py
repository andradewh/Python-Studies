import os

lista = list()

while True:
    opcao = input('Selecione uma opção: \n[i]nserir, [a]pagar, [l]istar, [e]svaziar lista: ')
    opcao = opcao.lower()

    if len(opcao) > 1:
        continue
    if opcao == 'l' and len(lista) == 0:
        print('Nada para listar')
    if opcao in ('a','e') and len(lista) == 0:
        print('Nada para apagar')

    ##tratativas listagem
    if opcao == 'l':
        os.system('cls')
        for i,nome in enumerate(lista):
            print(i,nome)
    ##tratativas insercao
    elif opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')

        if len(valor) == 0:
            continue
        else:
            lista.append(valor)
    ##tratativas delecao
    elif opcao == 'a':
        try:
            indice = input('Escola o índice para apagar: ')
            lista.pop(int(indice))
        except ValueError:
            print('Por favor, digite um número inteiro.')
        except IndexError:
            print('Indíce não existente!')
            continue
    ##tratativas delecao da lista toda
    elif opcao == 'e':
        os.system('cls')
        lista.clear()
    else:
        os.system('cls')
        print('Por favor, escolha "i", "a", "e" ou "l"')
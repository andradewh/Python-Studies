# Exercício - sistema de perguntas e respostas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

resposta = ''
acertos = 0
## laço principal
for pergunta in perguntas:
    print('Pergunta:',pergunta['Pergunta'],'\nOpções:')

    ##laço para apresentar as opções e colher a resposta
    for index,opcao in enumerate(pergunta['Opções']):
        print(f'{index}) {opcao}')
    resposta = input('Escolha uma opção: ')

    ##validação da etrada da resposta
    try: 
        if pergunta['Opções'][int(resposta)] == pergunta['Resposta']:
            acertos += 1
            print('Acertou!\n')
        else:
            print('Errou!\n')
    except IndexError:
        print('Errou!\n')
    except ValueError: 
        print('Errou!\n')
    
print(f'Voce Acertou {acertos} de {len(perguntas)} Perguntas.')
"""Calculadora com while"""

while True:
    try:
        num_1 = float(input('Digite O primeiro valor: '))
        num_2 = float(input('Digite o segundo valor: '))
        operacao = input('Digite a operação: +(Adição) -(Subtração) /(Divisão) *(Multiplicação)')
        
        if operacao not in '+-/*':
            print('Digite uma operação válida!')
            continue
        if len(operacao) >1:
            print('Digite apenas uma operação!')
            continue

        if operacao == '+':
            resultado = num_1+num_2
        if operacao == '-':
            resultado = num_1-num_2
        if operacao == '/':
            resultado = num_1/num_2
        if operacao == '*':
            resultado = num_1*num_2

        print(f'O resultado da operação é: {resultado}')
    except:
        print("Valores digitados não são números!")
    

    sair = input("Deseja Sair? [s]im: ").lower().startswith('s')

    if sair is True:
        break
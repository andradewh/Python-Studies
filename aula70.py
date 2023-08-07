import numpy as np

frase = 'willian henrique de andrade s2 thainá Nogueira godoy'

i = 0
letra_atual = ''
letra_passada = ''
qtd_letra_atual = 0
qtd_letra_passada = 0
letra_que_mais_aparece = ''
qtd_letra_que_mais_aparece = 0
letras_analisadas = []
letras_que_mais_aparecem_list = []

while i < len(frase):
    letra_atual = frase[i]
    qtd_letra_atual = frase.count(letra_atual)
    i+=1
    ##validação para retirada de espaços (não contagem de espaços)
    if letra_atual == ' ':
        continue
    ##validação para não termos de contar letras repetidas
    if letra_atual in letras_analisadas:
        continue

    if (letra_que_mais_aparece == '' and qtd_letra_que_mais_aparece == 0
    or qtd_letra_atual >= qtd_letra_que_mais_aparece):
        letras_que_mais_aparecem_list.append(letra_atual)

    ##usado para adicionar  valores as variáveis de rank na primeira rodada
    if letra_que_mais_aparece == '' and qtd_letra_que_mais_aparece == 0:
        letra_que_mais_aparece = letra_atual
        qtd_letra_que_mais_aparece = qtd_letra_atual
        
    if qtd_letra_atual > qtd_letra_que_mais_aparece:
        letra_que_mais_aparece = letra_atual
        qtd_letra_que_mais_aparece = qtd_letra_atual
        
    if (frase.count(frase[0]) < qtd_letra_que_mais_aparece
    and frase[0] in letras_que_mais_aparecem_list):
        letras_que_mais_aparecem_list.remove(frase[0])

    letra_passada = letra_atual
    qtd_letra_passada = qtd_letra_atual
    
    letras_analisadas.append(letra_atual)

    

print (f'A letra que mais aparece é: {np.unique(letras_que_mais_aparecem_list)}, aparecendo {qtd_letra_que_mais_aparece} vezes')


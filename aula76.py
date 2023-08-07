import os
##módulo para gerar palavras em ingles
from random_word import RandomWords

r = RandomWords()
palavra_secreta = r.get_random_word()

tentativas = 0
letras_corretas = ''

while True:
    letra = input('Digite uma letra para verificar se existe na palavra secreta: '+
                  "\nCaso queira verificar a palavra secreta, digite '#'")
    ##adicionado verificação para caso o usuário deseje ler a palavra secreta
    if letra == '#':
        print(f"A plavra secreta é: {palavra_secreta}") 
        continue  

    if len(letra) > 1:
        print("Digite apenas uma letra!")
        continue

    tentativas += 1

    if letra in palavra_secreta:
        letras_corretas += letra

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_corretas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(f"Parabens, voce encontrou a palavra secreta em {tentativas} tentativas"+
              f"\nA Palavra era {palavra_secreta}")
        
        continuar = input("Deseja jogar novamente? Digite 's' para continuar e qualquer outra coisa para sair: ")
        if continuar == 's':
            os.system('cls')
            palavra_secreta = r.get_random_word()
            tentativas = 0
            letras_corretas = ''
            palavra_formada = ''                 
            continue
        else:
            break
    else:
        continue
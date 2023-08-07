nome = 'willian'
nome_len = len(nome)
novo_nome = ''
i = 0

while i < nome_len:
    novo_nome += f'*{nome[i]}'
    i+=1

novo_nome += '*'
print(novo_nome)
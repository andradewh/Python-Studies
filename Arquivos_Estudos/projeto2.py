'''
Organizador de arquivos.
'''

import os
from tkinter.filedialog import askdirectory

##seleciona o diretório
caminho = askdirectory(title="Selecione uma pasta")

##adiciona os arquivos a uma lista
lista_arquivos = os.listdir(caminho)

##dict usado para criar as pastas 
locais = {
    "imagens":[".jpg"],
    "pdf":[".pdf", ".PDF"],
    "planilhas":[".xlsx"],
    "docs":[".pptx", ".txt", ".docx (1)"],
    "outros":[".23", ".20", ".mp4", ".zip", ".rar", ".1+Script1", ".00", ".52", ".torrent", ".exe"]
}

##primeiro for passa arquivo por arquivo
for arquivo in lista_arquivos:
    ##separa o nome da extensao
    nome, extensao = os.path.splitext(f'{caminho}/{arquivo}')
    ##roda cada pasta(chave) do dict 
    for pasta in locais:
        ##verifica se a extensão do arquivo existe no dict
        if extensao in locais[pasta]:
            ##verifica se a pasta não existe, se for true, cria
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.mkdir(f'{caminho}/{pasta}')
            ##move os arquivos para a pasta correta
            os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}')
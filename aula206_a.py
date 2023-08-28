import os
import json

CAMINHO = 'dados.json'

class Pessoa:

    def __init__ (self,nome,idade,sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
    def get_dados(self):
        return f'{self.nome}, {self.idade}, {self.sexo}'
    
def salvar(lista,caminho):
    dados = lista
    with open(caminho, 'w', encoding='utf8') as arquivo:
        dados = json.dump(lista, arquivo, indent=2, ensure_ascii=False)
    return dados

def ler(class_obj_dict,caminho):
    dados = {}
    try:
        with open(caminho,'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe.')
        salvar(p1,CAMINHO)
    return dados


p1 = Pessoa('Willian',27,'M')
p2 = Pessoa('Thainá',27,'F')
p3 = Pessoa('Pant',1,'F')
p4 = Pessoa('Mel',10,'F')
bd = [vars(p1),vars(p2),vars(p3),vars(p4)]

salvar(bd,CAMINHO)


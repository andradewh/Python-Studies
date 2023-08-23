import os

# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

def initial_message():
    message = ('Comandos: listar, desfazer, refazer\n'+
          'Digite uma tarefa ou comando: ')
    return message

todo_list = []
garbage_list = []
aux = ''

while True:
    aux = input(initial_message())
    if aux not in ('listar','desfazer','refazer','limpar'):
        todo_list.append(aux)
        print()
        continue

    elif aux.lower() == 'listar' and len(todo_list) == 0:
        print('NADA A LISTAR')
        print()
        continue

    elif aux.lower() == 'listar' and len(todo_list) > 0:
        print(*todo_list, sep='\n')
        print()
        continue

    elif aux.lower() == 'desfazer' and len(todo_list) == 0:
        print('NADA A DESFAZER')
        print()
        continue

    elif aux.lower() == 'desfazer' and len(todo_list) > 0:
        garbage_list.append(todo_list[-1])
        del todo_list[-1]
        print(*todo_list, sep='\n')
        print()
        continue

    elif aux.lower() == 'refazer' and len(garbage_list) == 0:
        print('NADA A REFAZER')
        print()
        continue

    elif aux.lower() == 'refazer' and len(garbage_list) > 0:
        todo_list.append(garbage_list[-1])
        del garbage_list[-1]
        print(*todo_list, sep='\n')
        print()
        continue

    else:
        os.system('cls')
        continue



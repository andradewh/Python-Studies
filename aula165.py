# funções decoradoras

#3 - então usamos uma função decoradora
# para trabalharmos sobre nossa primeira função
#trabalho dessa função é receber ela e ter uma função interna para termos uma
# closure
def create_func(func):
    def internal(*args, **kwargs):
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print(f'seu resultado é {result}')
        return result
    return internal

#4 - ao adicionar o Syntax sugar abaixo (decorator), 
# não precisamos reescrever a usabiidade da função no item 6
@create_func
#1 - essa função inverte string, não deve fazer mais com isso
def reverse_string(string):
    return string[::-1]

#2 - devemos poder checar se é uma string que foi passada, 
# então para ter atomicidade de funçõesdevemos fazer outra função,
# e não adicionar a função de inverter
def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Param mus be string')

#6 - chamada da função
reversed = reverse_string('123')
print(reversed)
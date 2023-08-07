def multi(*args):
    multi = 0
    for item in args:
        if multi == 0:
            multi = 1
        multi = multi*item
        total = multi
    return total

def is_par(numero):
    mod = numero % 2
    if mod != 0:
        resultado = 'Ímpar'
    else:
        resultado = 'Par'
    return resultado

eh_par = is_par(13)
print(eh_par)
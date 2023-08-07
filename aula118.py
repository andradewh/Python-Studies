def cria_multiplicacao(multiplicador):
        def multiplicacao(numero):
                return numero*multiplicador
        return multiplicacao

duplicar = cria_multiplicacao(2)
triplicar = cria_multiplicacao(3)
quaduplicar = cria_multiplicacao(4)

print(duplicar(5))
print(triplicar(5))
print(quaduplicar(5))

'''
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
'''
a, b, c = input().split(sep=' ')
a, b, c = float(a), float(b), float(c)

pi = pi = 3.14159

triangulo = ((a * c) / 2)
circulo = (pi * (c ** 2))
trapezio = ((0.5 * (a + b)) * c)
quadrado = (b * b)
retangulo = (a * b)

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')
'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”
'''

a, b, c = input().split(sep=' ')
a, b, c = int(a), int(b), int(c)
maior = 0

MaiorAB = ((a + b + abs(a - b)) / 2)
MaiorABC = int((MaiorAB + c + abs(MaiorAB - c)) / 2)

print(f'{MaiorABC} eh o maior')
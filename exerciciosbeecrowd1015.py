'''
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula
'''
from math import sqrt


x1, y1 = input().split(sep=' ')
x2, y2 = input().split(sep=' ')
x1, x2, y1, y2 = float(x1), float(x2), float(y1), float(y2)
p1 = ((x2 - x1)**2)
p2 = ((y2 - y1)**2)
distancia = sqrt(p1 + p2)

print(f'{distancia:.4f}')
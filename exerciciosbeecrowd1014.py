'''
Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).

'''

dist_tot = int(input())
comb_gasto = float(input())

consumo = (dist_tot / comb_gasto)

print(f'{consumo:.3f} km/l')
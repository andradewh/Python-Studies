entrada = list(input().split())
#using list comprehension to alter list itens type
entrada = [int(i) for i in entrada]

for i,_ in enumerate(entrada):
    entrada_sorted = sorted(entrada)
    print(entrada_sorted[i])

print()

for i,_ in enumerate(entrada):
    entrada
    print(entrada[i])
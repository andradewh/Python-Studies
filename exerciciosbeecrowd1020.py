idade = int(input())

ano = idade // 365
idade = idade % 365
mes = idade // 30
idade = idade % 30
dia = idade

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')
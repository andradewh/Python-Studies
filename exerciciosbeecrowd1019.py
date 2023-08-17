tempo = int(input())

hora = tempo // 3600
tempo = tempo % 3600

minuto = tempo // 60
tempo = tempo % 60

segundo = tempo

print(f'{hora}:{minuto}:{segundo}')
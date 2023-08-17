entrada = float(input())

#notas 100
notas100 = entrada//100
entrada = entrada%100

#notas 50
notas050 = entrada//50
entrada = entrada%50

#notas 20
notas020 = entrada//20
entrada = entrada%20

#notas 10
notas010 = entrada//10
entrada = entrada%10

#notas 5
notas005 = entrada//5
entrada = entrada%5

#notas 2
notas002 = entrada//2
entrada = entrada%2

#moedas 1
notas001 = entrada//1
entrada = entrada%1

#moedas ,50
notas0005 = entrada//0.5
entrada = entrada%0.5

#moedas ,25
notas00025 = entrada//0.25
entrada = entrada%0.25

#moedas ,10
notas00010 = entrada//0.10
entrada = entrada%0.10

#moedas ,05
notas00005 = entrada//0.05
entrada = entrada%0.05

#moedas 0,01
notas00001 = entrada

print('NOTAS:')
print(f"{int(notas100)} nota(s) de R$ 100.00")
print(f"{int(notas050)} nota(s) de R$ 50.00")
print(f"{int(notas020)} nota(s) de R$ 20.00")
print(f"{int(notas010)} nota(s) de R$ 10.00")
print(f"{int(notas005)} nota(s) de R$ 5.00")
print(f"{int(notas002)} nota(s) de R$ 2.00")

print('MOEDAS:')
print(f"{int(notas001)} moeda(s) de R$ 1.00")
print(f"{int(notas0005)} moeda(s) de R$ 0.50")
print(f"{int(notas00025)} moeda(s) de R$ 0.25")
print(f"{int(notas00010)} moeda(s) de R$ 0.10")
print(f"{int(notas00005)} moeda(s) de R$ 0.05")
print(f"{int(notas00001)} moeda(s) de R$ 0.01")
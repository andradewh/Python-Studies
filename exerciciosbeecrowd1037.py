entrada = float(input())
intervalos = ([0,25], [25,50], [50,75], [75,100])

if (entrada >= intervalos[0][0] 
and entrada <= intervalos[0][1]):
    print('Intervalo [0,25]')
elif (entrada >= intervalos[1][0] 
 and entrada <= intervalos[1][1]):
    print('Intervalo (25,50]')
elif (entrada >= intervalos[2][0] 
 and entrada <= intervalos[2][1]):
    print('Intervalo (50,75]')
elif (entrada >= intervalos[3][0] 
 and entrada <= intervalos[3][1]):
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')


a,b,c,d = input().split(sep=' ')
a,b,c,d = int(a),int(b),int(c),int(d)

if ((b > c) 
and (d > a) 
and ((c + d) > (a + b)) 
and ((c > 0) and (d > 0)) 
and ((a % 2) == 0)):
    print('Valores Aceitos')
else:
    print('Valores Não Aceitos')
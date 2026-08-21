from math import hypot
print('===== DESAFIO 17 =====')
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
print('Cateto oposto é {} e Cateto adjacente é {},\n logo sua hipotenusa é {:.2f}'.format(co, ca, hypot(co, ca)))

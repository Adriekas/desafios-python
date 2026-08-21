print('===== DESAFIO 08 =====')
valor = float(input('Digite um valor em metros: '))
#cm = valor * 100
#mm = valor * 1000
#print('A conversão de {} metros para Centímetros e Milímetros é {} e {}'.format(valor, (valor*100), (valor*1000)))
print('A medida de {}m corresponde a \n{:.3f}km.\n{:.2f}hm.\n{:.1f}dam.\n{:.0f}dm.\n{:.0f}cm.\n{:.0f}mm.'.format(valor, (valor/1000), (valor/100), (valor/10), (valor*10), (valor*100), (valor*1000)))

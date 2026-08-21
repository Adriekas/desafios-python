print('===== DESAFIO 31 =====')
distancia = int(input('Digite uma distância em KM: '))
'''if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45'''
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O valor da viagem de {} Km será de R$ {:.2f} Reais'.format(distancia, preco))
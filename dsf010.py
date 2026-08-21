print('===== DESAFIO 10 =====')
carteira = float(input('Digite quantos reais você têm na carteira: R$'))
us = carteira / 3.27
print('Com R${:.2f} reais, você pode converter para ${:.2f} Dólares'.format(carteira, us))

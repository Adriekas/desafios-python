print('===== DESAFIO 12 =====')
vlr = float(input('Digite o valor de um produto: R$'))
desconto = vlr - (vlr * (5/100))
print('O novo preço do produto, que custava R${:.2f}, agora com 5% de desconto é R${:.2f} reais.'.format(vlr, desconto))
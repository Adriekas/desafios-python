print('===== DESAFIO 44 =====')
preco = float(input('Informe o preço do produto: R$'))
print('''Informe o condição de pagamento
1 - dinheiro
2 - cartão a vista 
3 - 2x no cartão
4 - 3x ou + no cartão: ''')
condicao = int(input('Qual sua forma de pagamento?: '))
if condicao == 1:
    npreco = preco - (preco * 0.10)
    print('O valor da compra R${:.2f} terá 10% de desconto! Vai custar R${:.2f} reais.'.format(preco, npreco))
elif condicao == 2:
    npreco = preco - (preco * 0.5)
    print('O valor da compra R${:.2f} terá 5% de desconto! Vai custar R${:.2f} reais.'.format(preco, npreco))
elif condicao == 3:
    print('O valor terá o preço normal de R${} reais!'.format(preco))
else:
    parcela = int(input('Quantas parcelas? '))
    juros = preco * 0.20
    npreco = preco + juros
    valorparcela = npreco / parcela
    print('A compra de R${:.2f} será parcelado em {}x de R${:.2f} reais. O valor terá 20% de juros! Fazendo a compra no final custear R${:.2f} reais! '.format(preco, parcela,valorparcela, npreco))
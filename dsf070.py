print('===== DESAFIO 70 =====')
print('-' * 28)
print(f'{'MERCADINHO BÃO':^28}')
print('-' * 28)
total = qtdeprodmil = precobarato = i = 0
prodbarato = ' '
while True:
    nomeprod = str(input('Nome do Produto: ')).strip().title()
    precoprod = float(input('Preço: R$'))
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    total += precoprod
    i += 1
    if i == 1:
        precobarato = precoprod
    else:
        if precoprod < precobarato:
            precobarato = precoprod
            prodbarato = nomeprod
    if escolha in 'N':
        break
print(f'{'-' * 11} FIM DO PROGRAMA {"-" * 11}')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {qtdeprodmil} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {prodbarato} que custa R${precobarato:.2f}')

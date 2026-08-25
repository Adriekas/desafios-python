print('====== DESAFIO 55 ======')
maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {:.1f}Kg \n'
      'O menor peso lido foi de {:.1f}Kg \n'.format(maior, menor))

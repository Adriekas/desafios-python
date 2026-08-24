print('===== DESAFIO 48 =====')
soma = 0
contador = 0
for cont in range(1,501, 2):
    if cont % 3 == 0:
        contador += 1
        soma += cont
print('A soma de todos os {} valores solicitados é {}.'.format(contador,soma))

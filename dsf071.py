print('===== DESAFIO 71 =====')
print(f'{'=' * 30}')
print(f'{'BANCO':^30}')
print(f'{'=' * 30}')
valor = int(input('Que valor você quer sacar? R$'))
total = valor
cedula = 50
totced = 0
while True:
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        print(f'Total de {totced} cédula(s) de R${cedula} real(is).')
        if cedula == 50:
            cedula = 20
            totced = 0
        elif cedula == 20:
            cedula = 10
            totced = 0
        elif cedula == 10:
            cedula = 1
            totced = 0
        if total == 0:
            break
'''cinquenta = valor // 50
vinte = (cinquenta % 50) // 20
dez = (vinte % 20) // 10
um = vinte % 10'''

print('===== DESAFIO 62 =====')
print('='*30)
print('    10 TERMOS DE UMA P.A     ')
print('='*30)
prtermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
contador = 1
somador = prtermo
total = 0
acrescimo = 10
print('{}'.format(prtermo), end=' -> ')
somador += razao
while acrescimo != 0:
    total += acrescimo
    while contador < total:
        print('{}'.format(somador), end=' -> ')
        somador += razao
        contador += 1
    print('PAUSA')
    acrescimo = int(input('Quantos termos quer mostrar a mais? '))
print('Progressão finalizada com {} termos'.format(total))
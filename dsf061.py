print('===== DESAFIO 61 =====')
print('='*30)
print('    10 TERMOS DE UMA P.A     ')
print('='*30)
prtermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
contador = 1
somador = prtermo
'''for c in range(prtermo, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')'''
print('{}'.format(prtermo), end=' -> ')
somador += razao
while contador < 10:
        print('{}'.format(somador), end=' -> ')
        somador += razao
        contador += 1
print('FIM')

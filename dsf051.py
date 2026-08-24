print('===== DESAFIO 51 =====')
print('='*30)
print('    10 TERMOS DE UMA P.A     ')
print('='*30)
prtermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = prtermo + (10-1) * razao
for c in range(prtermo, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('FIM')

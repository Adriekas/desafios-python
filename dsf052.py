print('====== DESAFIO 52 ======')
numero = int(input('Digite um número: '))
total = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(i), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(numero, total))
if total == 2:
    print('Logo, ele é Primo!')
else:
    print('Logo, ele NÃO é Primo!')
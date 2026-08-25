print('===== DESAFIO 60 =====')
n = int(input('Digite um valor para ser calcular o seu fatorial: '))
fatorial = 1
print('Calculando {}! = '.format(n), end=' ')
while n > 1:
    print('{} x'.format(n), end=' ')
    fatorial *= n
    n -= 1
    if n == 1:
        print('{} ='.format(n), end=' ')
        print(fatorial)
print('Fim do programa!')

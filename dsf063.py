print('===== DESAFIO 63 =====')
print('-' * 10)
print('Fibonacchi')
print('-' * 10)
n = int(input('Quantos termos quer mostrar? '))
t1 = 0
t2 = 1
contador = 3
print('{} -> {}'.format(t1, t2), end=' -> ')
while contador <= n:
    contador += 1
    t3 = t1 + t2
    print('{}'.format(t3), end=' -> ')
    t1 = t2
    t2 = t3
print('FIM')

print('===== DESAFIO 67 =====')
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    cont = 1
    if n < 0:
        break
    while cont <= 10:
        print(f'{n} x {cont:2} = {n * cont:2}')
        cont += 1
    print('-' * 30)
print('PROGRAMA DE TABUADA ENCERRADO!')

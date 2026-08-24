soma = 0
cont = 0
print('===== DESAFIO 50 =====')
for i in range(1, 7):
    n = int(input('Digite o {}º número inteiro:'.format(i)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Foram informados 6 números, desses {} numeros foram pares e a soma deles foi {}'.format(cont, soma))

print('===== DESAFIO 64 =====')
n = int(input('Digite um número [999 para parar]: '))
soma = 0
contagem = 0
while n != 999:
    soma += n
    if n != 999:
        n = int(input('Digite um número [999 para parar]: '))
        contagem += 1
print('Você digitou {} números e a soma entre eles foi {}'.format(contagem, soma))

print('===== DESAFIO 65 =====')

decisao = 'S'
soma = contagem = media = 0
while decisao not in 'Nn':
    contagem += 1
    numero = int(input('Digite um número: '))
    soma += numero
    if contagem == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        else:
            menor = numero
    decisao = str(input('Deseja Continuar? [S/N]: ')).upper().strip()
media = soma / contagem
print('Você digitou {} números e a média foi {:.2f}'.format(contagem, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))

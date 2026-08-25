print('===== DESAFIO 56 =====')
contador = 0
mulhermenor = 0
maioridadehomem = 0
nomevelho = ''
for i in range(1, 5):
    print('----- {}ª PESSOA -----'.format(i))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').upper())
    contador += idade
    media = contador / 4
    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulhermenor += 1
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulher(es) com menos de 20 anos.'.format(mulhermenor))

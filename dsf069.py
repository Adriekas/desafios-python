print('===== DESAFIO 69 =====')
total = cadhomem = mulheridad = 0
sexo = ' '
while True:
    print('-' * 28)
    print('    CADASTRE UMA PESSOA')
    print('-' * 28)
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
        if sexo in 'MF':
            break
    if idade >= 18:
        total += 1
    if sexo == 'M':
        cadhomem += 1
    if sexo == 'F' and idade < 20:
        mulheridad += 1
    print('-' * 28)
    escolha = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if escolha in 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {total}')
print(f'Ao todo temos {cadhomem} homem(ns) cadastrados.\n'
      f'E temos {mulheridad} mulher(es) com menos de 20 anos.')

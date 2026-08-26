from random import randint
print('===== DESAFIO 68 =====')
print('=-' * 14)
print(' BRINCANDO DE PAR OU ÍMPAR')
print('=-' * 14)
computador = randint(1, 10)
rodadas = total = vitorias = 0
escolhacomp = ' '
print('-' * 28)
while True:
    rodadas += 1
    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    if escolha == 'P':
        escolhacomp = 'I'
    else:
        escolhacomp = 'P'
    total = jogador + computador
    if total % 2 == 0 and escolha == 'P':
        print('Você VENCEU!!\n'
            f'Você jogou {jogador} e o computador {computador}. Total deu {total}\n'
              'Logo deu PAR')
        print('-' * 28)
        print('Vamos jogar novamente...')
        print('=-' * 14)
        vitorias += 1
    else:
        print('Você PERDEU!')
        print('=-' * 14)
        break
print(f'GAME OVER! Você venceu {vitorias} vez(es).')

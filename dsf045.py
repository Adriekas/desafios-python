from random import choice
from time import sleep
print('===== DESAFIO 45 =====')
pc = choice(['Pedra', 'Papel', 'Tesoura'])
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po!!!')
jogador = str(input('Escolha -> Pedra, Papel ou Tesoura: '))
if jogador == 'Pedra' and pc == 'Papel' or jogador == 'Papel ' and pc == 'Tesoura' or jogador == 'Tesoura' and pc == 'Pedra':
    print('-=-' * 12)
    print('Você perdeu! eu escolhi {}'.format(pc))
    print('-=-' * 12)
elif jogador == 'Pedra' and pc == 'Tesoura' or jogador == 'Tesoura' and pc == 'Papel' or jogador == 'Papel' and pc == 'Pedra':
    print('-=-' * 12)
    print('Você venceu! eu escolhi {}'.format(pc))
    print('-=-' * 12)
else:
    print('-=-' * 12)
    print('Empate! eu escolhi {}'.format(pc))
    print('-=-' * 12)

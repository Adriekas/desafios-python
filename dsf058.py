from random import randint
from time import sleep
print('===== DESAFIO 58 =====')
nrandom = randint(1, 10)
tentativas = 0
palpite = int(input('Qual é o seu palpite de 1 a 10? '))
tentativas += 1
print('Estou analisando....')
sleep(2)
if palpite == nrandom:
    print('Você acertou!!!')
else:
    while palpite != nrandom:
            print('Você errou!!')
            print('=' * 10)
            if(palpite > nrandom):
                print('O número é menor do que {}'.format(palpite))
                palpite = int(input('Tente novamente: '))
                print('=' * 10)
                sleep(1)
                tentativas += 1
            else:
                print('O número é maior do que {}'.format(palpite))
                palpite = int(input('Tente novamente: '))
                print('=' * 10)
                sleep(1)
                tentativas += 1
print('Você acertou!!! com {} tentativa(s)'.format(tentativas))
print('====== FIM ======')

from random import randint
from time import sleep
print('===== DESAFIO 28 =====')
nrandom = randint(0, 5)
palpite = int(input('Qual é o seu palpite?'))
print('Estou analisando....')
sleep(2)
if palpite == nrandom:
    print('Você acertou!!!')
else:
    print('Você errou!!')
    if(palpite > nrandom):
        print('O número é menor.... eu pensei no número {}'.format(nrandom))
    else:
        print('O número é maior.... eu pensei no número {}'.format(nrandom))
print('====== FIM ======')

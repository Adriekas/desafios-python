print('===== DESAFIO 39 =====')
idade = int(input('Digite sua idade: '))
if idade == 18:
    print('Já pode se alistar para o exército!')
elif idade < 18:
    print('Ainda não pode se alistar')
    idade = 18 - idade
    print('Ainda faltam {} ano(s) para se alistar'.format(idade))
else:
    print('Você passou do tempo para se alistar em {} ano(s)!,'.format(idade - 18))

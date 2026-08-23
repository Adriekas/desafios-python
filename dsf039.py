from datetime import datetime
print('===== DESAFIO 39 =====')
nasc = int(input('Digite o ano de nascimento: '))
hoje = datetime.now().year
idade = hoje - nasc
if idade == 18:
    print('Quem nasceu em {}, terá {} anos hoje. Já pode se alistar para o exército!'.format(nasc, idade))
elif idade < 18:
    print('Quem nasceu em {}, terá {} anos hoje. Ainda não pode se alistar por faltar {} anos'.format(nasc, idade, 18 - idade))
else:
    print('Você passou do tempo para se alistar em {} ano(s)! Pois você têm {} anos,'.format(idade - 18, idade))

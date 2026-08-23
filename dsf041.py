from datetime import datetime
print('===== DESAFIO 41 =====')
nasc = int(input('Digite seu ano de nascimento: '))
ano = datetime.now().year
idade = ano - nasc
if idade <= 9:
    print('MIRIM, pois você têm {} anos.'.format(idade))
elif idade <= 14:
    print('INFANTIL, pois você têm {} anos.'.format(idade))
elif idade <= 19:
    print('JUNIOR, pois você têm {} anos.'.format(idade))
elif idade <= 20:
    print('SENIOR, pois você têm {} anos.'.format(idade))
else:
    print('MASTER, pois você têm {} anos.'.format(idade))

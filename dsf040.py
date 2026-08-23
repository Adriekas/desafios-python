print('===== DESAFIO 40 =====')
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('REPROVADO, pois a média do aluno é {}'.format(media))
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO, pois a média do aluno é {}'.format(media))
else:
    print('APROVADO, pois a média do aluno é {}'.format(media))

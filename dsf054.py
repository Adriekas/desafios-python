from datetime import datetime
print('===== DESAFIO 54 =====')
ano = datetime.now().year
contadordemaior = 0
contadordemenor = 0
for i in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i)))
    idade = ano - nascimento
    if idade >= 18:
        contadordemaior += 1
    else:
        contadordemenor += 1
print('Ao todo, temos {} pessoas na maioridade \n'
      'E também tivemos {} pessoas de menor!'.format(contadordemaior, contadordemenor))

print('===== DESAFIO 43 =====')
peso = float(input('Informe o seu peso: (KG)'))
altura = float(input('Informe a sua altura: (M)'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Com {}m de altura e pesando {}kg, você tem imc de {:.1f}, logo está Abaixo do peso'.format(altura, peso, imc))
elif imc >= 18.5 and imc <= 25:
    print('Com {}m de altura e pesando {}kg, você tem imc de {:.1f}, logo está com Peso ideal'.format(altura, peso, imc))
elif imc >= 25 and imc <= 30:
    print('Com {}m de altura e pesando {}kg, você tem imc de {:.1f}, logo está Sobrepeso'.format(altura, peso, imc))
elif imc >= 30 and imc <= 40:
    print('ATENÇÃO: Com {}m de altura e pesando {}kg, você tem imc de {:.1f}, logo está com Obesidade'.format(altura, peso, imc))
else:
    print('PERIGO: Com {}m de altura e pesando {}kg, você tem imc de {:.1f}, logo está em Obesidade Mórbida!'.format(altura, peso, imc))

print('====== DESAFIO 29 ======')
velocidade = int(input('Quantos km/h o carro está fazendo? '))
limite = 80
multa = (velocidade - limite) * 7.0
if velocidade > limite:
    print('ATENÇÃO! Você foi multado!')
    print('A multa ficou R$ {:.2f} reais'.format(multa))
print('Você está está dentro da velocidade limite da rodovia, boa viagem! ')
print('====== FIM ======')
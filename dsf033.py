print('===== DESAFIO 33 =====')
salario = int(input('Digite o seu salário: '))
if salario > 1250:
    aumento = salario * 0.10
    salario += aumento
else:
    aumento = salario * 0.15
    salario += aumento
print('Esse salário vai receber no próximo ano, um aumento, e vai ficar em R${:.2f} Reais!'.format(salario))

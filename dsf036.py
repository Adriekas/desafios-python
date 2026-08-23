print('===== DESAFIO 36 =====')
casa = float(input('Digite o valor da casa: '))
salario = float(input('Quanto é o seu salário? '))
anos = int(input('E em quantos anos você quer financiar? '))
parcela = casa / anos
print('O valor da prestação é de R${} em {} anos'.format(parcela, anos))

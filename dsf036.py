print('===== DESAFIO 36 =====')
casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Quanto é o seu salário? R$'))
anos = int(input('E em quantos anos você quer financiar? '))
parcela = casa / (anos * 12)
print('=-' * 12)
print('Para pagar uma casa no valor de R${:.2f} em {} anos, o valor da prestação é de R${:.2f} reais'.format(casa, anos, parcela))
print('=-' * 12)
if parcela <= salario * 0.3:
    print('Felizmente, seu empréstimo será aprovado!')
else:
    print('Infelizmente, seu empréstimo será negado!')

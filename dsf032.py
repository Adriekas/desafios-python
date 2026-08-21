print('===== DESAFIO 32 =====')
ano = int(input('Digite um ano qualquer: '))
bissexto = ano % 4 == 0 and (ano % 100 == 0 or ano % 400 == 0)
if(bissexto):
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto!')
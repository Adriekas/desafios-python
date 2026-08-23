print('===== DESAFIO 37 =====')
numero = int(input('Digite um número inteiro: '))
print('''Escolha a base de conversão:
1 - binário
2 - octal
3 - hexadecimal
Sua escolha: ''')
escolha = int(input('Digite sua escolha: '))
if escolha == 1:
    print('{} convertido para Binário é igual a {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('{} convertido para Octal é igual a {}'.format(numero, oct(numero)[2:]))
else:
    print('{} convertido para Hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
print('====== FIM DO PROGRAMA ======')

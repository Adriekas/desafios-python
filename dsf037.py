print('===== DESAFIO 37 =====')
numero = int(input('Digite um número: '))
escolha = int(input('Escolha a base de conversão, 1 - binário, 2 - octal, 3 - hexadecimal: '))
if escolha == 1:
    print(bin(numero))
elif escolha == 2:
    print(oct(numero))
else:
    print(hex(numero))
print('====== FIM DO PROGRAMA ======')

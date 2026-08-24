print('===== DESAFIO 53 =====')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
##Versão com fatiamento
inverso = junto[::-1]
##Versão com FOR
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Essa frase é um palíndromo!')
else:
    print('Não é um caso de palíndromo!')

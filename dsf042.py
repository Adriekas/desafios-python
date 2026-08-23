print('===== DESAFIO 42 =====')
print('-=-' * 10)
ladoa = int(input('Qual a lado A: '))
ladob = int(input('Qual a lado B: '))
ladoc = int(input('Qual a lado C: '))
print('-=-' * 10)
if ladoa + ladob > ladoc and ladoa + ladoc > ladob and ladob + ladoc > ladoa:
    print('Essas medidas conseguem formar um triângulo! ')
    if ladoa == ladob and ladoa == ladoc:
        print('Esses lados formaram um triângulo Equilátero!')
    elif ladoa != ladob and ladoa != ladoc:
        print('Esses lados formaram um triângulo Escaleno!')
    else:
        print('Esses lados formaram um triângulo Isósceles!')
else:
    print('Essas medidas NÃO conseguem formar o triângulo! ')
print('===== FIM DO PROGRAMA =====')

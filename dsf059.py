print('====== DESAFIO 59 =====')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
escolha = 0
while escolha != 5:
    print('O que deseja fazer?\n'
                  '[1] Somar\n'
                  '[2] Multiplicar\n'
                  '[3] Maior\n'
                  '[4] Menor\n'
                  '[5] Sair do programa')
    escolha = int(input('Qual é a sua escolha? '))

    if escolha == 1:
        soma = n1 + n2
        print('A soma dos números {} e {} é {}'.format(n1, n2, soma))
        print('-==-' * 15)
    elif escolha == 2:
        mult = n1 * n2
        print('A multiplicação de {} por {} é {}'.format(n1, n2, mult))
        print('-==-' * 15)
    elif escolha == 3:
        if n1 > n2:
            maior = n1
            print('O maior número entre os dois é {}'.format(maior))
            print('-==-' * 15)
        else:
            maior = n2
            print('O maior número entre os dois é {}'.format(maior))
            print('-==-' * 15)
    elif escolha == 4:
        if n1 < n2:
            menor = n1
            print('O menor número entre os dois é {}'.format(menor))
            print('-==-' * 15)
        else:
            menor = n2
            print('O menor número entre os dois é {}'.format(menor))
            print('-==-' * 15)
    elif escolha == 5:
        print('Finalizando...')
        print('-==-' * 15)
    else:
        print('Opção inválida!Tente novamente')
print('Fim do programa!')

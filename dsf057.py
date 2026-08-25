print('===== DESAFIO 57 =====')
r = str(input('Digite o seu sexo: [M/F]')).strip().upper()
while r not in 'MmFf':
    r = str(input('Valor inválido, digite novamente o seu sexo: ')).strip().upper()

print('Sexo {} registrado com sucesso!'.format(r))
print('FIM DO PROGRAMA')
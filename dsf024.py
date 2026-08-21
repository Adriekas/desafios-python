print('===== DESAFIO 24 =====')
cidade = str(input('Em que cidade você nasceu? ')).strip()
#print('Essa cidade começa com "Santo" no nome? {}'.format(bool(cidade.find('Santo')+1)))
print ('Essa cidade começa com "Santo" no nome? {}'.format(cidade[:5].upper() == 'SANTO'))
'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome ""SANTO""
O retorno será True ou False.
'''
cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')

'''
A COnfederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre seua categoria, de acordo com a idade:

Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 25 anos: SENIOR
Acima: MASTER
'''

from datetime import date

atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc

print('O atleta te {} anos'.format(idade))

if idade <= 9:
    print('Categoria: Mirim')
elif idade <= 14:
    print('Categoria: Infantil')
elif idade <= 19:
    print('Categoria: Junior')
elif idade <= 25:
    print('Categoria: Senior')
else:
    print('Categoria: Master')

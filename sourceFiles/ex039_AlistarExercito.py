'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

Se ele ainda vai se alistar no serviço militar.
Se é a hora de se alistar.
Se já passou do tempo de alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date

atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print('Você deve se alistar imediatamente.')
elif idade < 18:
    tempo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(tempo))
else:
    tempo = idade - 18
    print('Você deveria ter se alistado há {} anos.'.format(tempo))

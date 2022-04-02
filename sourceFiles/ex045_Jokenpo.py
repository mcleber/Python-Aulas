'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

from random import randint
from time import sleep

item = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)

print('''OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Escolha sua jogada: '))

print('JO', end='')
sleep(0.5)
print('KEN', end='')
sleep(0.5)
print('PO!')
sleep(0.5)

print('-' * 26)
#teste de escolha jogador e computador
print('Computador jogou: {}'.format(item[comp]))
print('Jogador jogou: {}'.format(item[jogador]))
print('-' * 26)

if comp == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador venceu')
    elif jogador == 2:
        print('Computador venceu')
    else:
        print('Opção inválida!')
elif comp == 1:
    if jogador == 0:
        print('Computador venceu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador venceu')
    else:
        print('Opção inválida!')
elif comp == 2:
    if jogador == 0:
        print('Jogador venceu')
    elif jogador == 1:
        print('Computador venceu')
    elif jogador == 2:
        print('Empate')
    else:
        print('Opção inválida!')
print('-' * 26)

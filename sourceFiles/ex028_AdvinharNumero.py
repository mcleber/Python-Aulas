'''
Escreve um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
o usuário tentar descobrir qual foi o número escolhido pelo computador, O programa deverá escrever
na tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep

computador = randint(0, 5) # faz o computador sortear um número
print('-=-' * 20)
print('Vou sortear um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
#print('Pensei no número {}'.format(computador))
jogador = int(input('Em que número eu pensei? ')) # jogador tenta advinhar
print('PROCESSANDO...')
sleep(1)

if jogador == computador:
    print('Parabéns, você acertou!')
else:
    print('Ganhei! Pensei no número {} e não no número {}'.format(computador, jogador))

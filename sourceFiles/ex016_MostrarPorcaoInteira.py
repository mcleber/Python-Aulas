#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela
#sua porção inteira. Ex.: 6127, o resultado deverá ser 6

'''import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))'''

from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

'''num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))'''

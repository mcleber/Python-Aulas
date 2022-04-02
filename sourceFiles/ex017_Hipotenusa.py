'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
retângulo, calcule e mostre o comprimento da hipotenusa
'''

import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

''' SOLUÇÃO SEM IMPORTAR MÓDULOS
hi = (co ** 2 + ca ** 2) ** (1/2)
print("A hipotenusa vai medir {:.2f}".format(hi))
'''

hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

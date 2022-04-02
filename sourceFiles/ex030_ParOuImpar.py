'''
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
'''

n = int(input('Me diga um número qualquer: '))
resultado = n % 2 # % pega o resto da divisão

if resultado == 0:
    print('O número {} é par.'.format(n))
else:
    print('O número {} é ímpar.'.format(n))

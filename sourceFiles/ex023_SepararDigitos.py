'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
Ex.:
Digite um número: 1834
unidade: 4
dezenas: 3
centena: 8
milhar: 1
'''
num = int(input('Informe um número: '))
u = num // 1 % 10 #pega o número e divide por 1 e pega o moludo de 10 (pega o numero, divide por 10 e pega o resto que é a unidade).
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

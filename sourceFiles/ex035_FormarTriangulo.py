'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
formar um triângulo.

A regra diz que a reta 1 tem que ser menor que a soma das retas 2 e 3. Idem para as demais retas..
3, 3, 3 formam triângulo.
2, 4, 6 não formam triângulo
'''

print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima FORMAM UM TRIÂNGULO.')
else:
    print('Os segmentos acima NÃO FORMAM UM TRIÂNGULO.')

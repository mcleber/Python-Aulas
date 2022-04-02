'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:

1 para binário
2 para octal
3 para hexadecimal
'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma converão:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')

conv = int(input('Sua opção: '))

if conv == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)[2:])) # [2:] Fatiamento. Exclui a posição 0 e 1
elif conv == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif conv == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida.')

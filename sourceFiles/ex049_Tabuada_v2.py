'''
Mostra e tabuada de um número indicado pelo usuário.
(melhoramento do ex009)
'''

num = int(input('Digite um número para ver a tabuada: '))
print('-' * 12)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))
print('-' * 12)

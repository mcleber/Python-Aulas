'''
Faça um programa que leia o primeiro termo e a razão de uma PA (prograssão aritmética).
No final, mostre os 10 primeiros termos dessa progressão.
'''

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: ')) # é o quanto se quer pular

decimo = primeiro + (10 - 1) * razao # 10 porque queremos o decimo termo

for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' → ')
print('FIM')

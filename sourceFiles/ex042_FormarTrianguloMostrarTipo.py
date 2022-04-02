'''
Refaça o exercício ex035 dos triângulos, acrescentando o recurso de mostrar que tipo
de triângulo será formado:

Equilátero: todos os lados iguais
Isósceles: dois lados iguais
Escaleno: todos os lados diferentes
'''

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        tipo = 'equilátero'
    elif r1 != r2 != r3 != r1:
        tipo = 'escaleno'
    else:
        tipo = 'isóceles'

    print('Os segmentos {}, {} e {} formam um triângulo {}'.format(r1, r2, r3, tipo))
else:
    print('Os segmentos {}, {} e {} não formam um triângulo'.format(r1, r2, r3))

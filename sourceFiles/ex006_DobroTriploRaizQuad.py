#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))

#raiz quadrada: pow(n, (1/2))

print('O número digitado é {}. \nO dobro é {}. '
      '\nO triplo é {}. '
      '\nA raiz quadrada é {:.2f}.'
      .format(n, (n*2), (n*3), pow(n, (1/2))))

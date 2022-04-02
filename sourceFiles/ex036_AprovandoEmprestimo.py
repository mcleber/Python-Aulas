'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
'''

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

prestacao = casa / (anos * 12)
min = salario * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos,'
      ' a prestação será de R${:.2f}'.format(casa, anos, prestacao))

if prestacao <= min:
    print('Empréstimo concedido!')
else:
    print('Empréstimo negado!')

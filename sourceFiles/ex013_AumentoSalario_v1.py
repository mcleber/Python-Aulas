#desafio 013
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário, R$'))
aumento = salario + (salario * 15/100)

print('O salário do funcionário de R${:.2f}, com 15% de aumento é R${:.2f}.'.format(salario, aumento))

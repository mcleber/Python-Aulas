#desafio 012
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual o valor do produto? R$'))
desc = preco - (preco * 5/100)

print('O preço do produto é R${:.2f}, com desconto de 5% custará R${:.2f}.'.format(preco, desc))

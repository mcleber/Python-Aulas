#desafio 010
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere US$1.00 = R$5,33

real = float(input('Digite quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.33
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))

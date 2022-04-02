'''
Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:

À vista dinheiro/cheque? 10% de desconto
À vista no cartão: 5% de desconto
Em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros
'''

print('{:^30}'.format(' LOJÃO PREÇO BÃO ')) # {:^30} indica centralizado em 30 espaços
print('-' * 33)

compra = float(input('Preço das compras: R$'))
print('''Formas de pagamento:
[ 1 ] à vista no dinheiro / cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Qual a forma de pagamento? '))

if opcao == 1:
    total = compra - (compra * 10 / 100)
    print('Sua compra de R${:.2f} à vista terá desconto de 10% e custará R${:.2f}'.format(compra, total))
elif opcao == 2:
    total = compra - (compra * 5 / 100)
    print('Sua compra de R${:.2f} à vista terá desconto de 5% e custará R${:.2f}'.format(compra, total))
elif opcao == 3:
    total = compra
    parcela = total / 2
    print('Compra parcelada em 2x sem juros de R${:.2f}.'.format(parcela))
elif opcao == 4:
    total = compra + (compra * 20 / 100)
    qtdaparcelas = int(input('Digite a quantidade de parcelas: '))
    parcela = compra / qtdaparcelas
    print('Compra parcelada em {}x de R${:.2f}. '
    'Acrescido de 20% de juros custará no final R${:.2f}'.format(qtdaparcelas, parcela, total))
else:
    total = 0
    print('Opção inválida!')

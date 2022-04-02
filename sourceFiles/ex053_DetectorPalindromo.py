'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando espaços.

Ex.:
    APOS A SOPA
    A SACADA DA CASA
    A TORRE DA DERROTA
    O LOBO AMA O BOLO
    ANOTARAM A DARA DA MARATONA
'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1): # ex. 20 letras: -1 (pq é do 0 ao 19),
                                        # -1  (antes da primeira letra que é zero),
                                        # -1 (volta 1 letra)
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('Não é palíndromo')

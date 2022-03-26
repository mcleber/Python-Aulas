'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC (Índice de Massa Corporal)
e mostre seu status, de acordo com a tabela abaixo:

Abaixo de 18.5: abaixo do peso
Entre 18.5 e 25: peso ideal
25 até 30: sobrepeso
30 até 40: obesidade
Acima de 40: obesidade mórbida
'''

peso = float(input('Digite o seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))

imc = peso / (altura **2)

if imc < 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso ideal.'.format(imc))
#elif imc >= 18.5 and imc < 25:
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.2f} e você está no peso ideal.'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é de {:.2f} e você está com sobrepeso.'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é de {:.2f} e você está em obesidade.'.format(imc))
elif imc >= 40:
    print('Seu IMC é de {:.2f} e você está em obesidade mórbida.'.format(imc))

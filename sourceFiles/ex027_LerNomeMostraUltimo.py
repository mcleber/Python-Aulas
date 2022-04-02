'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
nome separadamente.
Ex.: Ana Maria de Souza
primeiro = Ana
último = Souza
'''
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split() # split particiona e cria uma lista começando no indice 0
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu segundo nome é {}'.format(nome[1])) # indice 1 pega o segundo nome
print('Seu último nome é {}'.format(nome[len(nome)-1]))

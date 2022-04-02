#desafio 008
#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input("Digite um valor em metros: "))

print('O valor em metros é {:.2f}m, '
      '\no valor em centímetros é {:.2f}cm e \n'
      'o valor em milímetros é {:.2f}mm'
      .format(medida, (medida*100), (medida*1000)))

# mm = medida * 1000 milimetro
# cm = medida * 100 centimetro
# dm = medida * 10  decimetro
# dam = medida / 10 decametro
# hm = medida / 100 hectometro
# km = medida / 1000 kilometro
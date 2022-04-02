#Faça um programa que converta uma temperatura em °C para °F (fahrenheit)

# °F = (°C * 1.8) + 32
# °C = (°F − 32) / 1.8

c = float(input('Informe a temperatura em °C: '))
f = ((c * 9) / 5) + 32

print('A temperatura de {:.2f}°C corresponde a {:.2f}°F!'.format(c, f))

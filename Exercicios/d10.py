#Programa que leia quanto dinheiro ela tem na carteira e mostre quantos dolares ela pode comprar (considere dolar 1=3,27)

real = float(input('Quantos reais você tem na carteira? '))

print ('Com {} reais, você pode comprar {} dolares'.format (real, (real//3.27)))

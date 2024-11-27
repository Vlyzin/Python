#Programa que leia quanto dinheiro ela tem na carteira e mostre quantos dolares ela pode comprar (considere dolar 1=3,27)

real = float(input('Quantos reais você tem na carteira? '))
cor = {'vermelho':'\033[1;31m','limpar':'\033[m','azul':'\033[1;36m','azul escuro':'\033[1;34m','branco':'\033[1;97m','amarelo':'\033[1;33m','verde':'\033[1;32m'}

print ('Com \033[0;33m{}\033[m reais, você pode comprar \033[4;32m{}\033[m dolares'.format (real, (real//3.27)))

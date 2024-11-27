#Escreva um programa que receba um valor em metros e leia ele em centimetros e milimetros.

v = float(input('Digite um valor em metros? '))
cor = {'vermelho':'\033[1;31m','limpar':'\033[m','azul':'\033[1;36m','azul escuro':'\033[1;34m','branco':'\033[1;97m','amarelo':'\033[1;33m','verde':'\033[1;32m'}
print ('A conversão desse valor de \033[1m{}\033[m metros é de \033[4m{:.5}\033[m centimetros e \033[4m{:.10}\033[m milimetros'.format(v,(v*100),(v*1000)))

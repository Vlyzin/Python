# Faça um programa que leia um número inteiro qualquer e mostre sua tabuada
from time import sleep
n = int(input('Digite um número: '))
cor = {'vermelho':'\033[1;31m','limpar':'\033[m','azul':'\033[1;36m','azul escuro':'\033[1;34m','branco':'\033[1;97m','amarelo':'\033[1;33m','verde':'\033[1;32m'}

for i in range(1, 11):
    resultado = n * i
    print('{} x {} vale \033[0;32m{}\033[m'.format (n, i, resultado))
    sleep(0.5)
print ('Eu saibo muito 😎')

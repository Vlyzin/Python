#Crie um algoritimo que leia um número e mostre seu dobro, triplo e raiz quadrada
import math

num = int(input('Digite um valor? '))
cor = {'vermelho':'\033[1;31m','limpar':'\033[m','azul':'\033[1;36m','azul escuro':'\033[1;34m','branco':'\033[1;97m','amarelo':'\033[1;33m','verde':'\033[1;32m'}

print('O dobro desse valor é {}{}{}'.format(cor['azul'],(num*num),cor['limpar']))
print('o triplo desse valor é {}{}{}'.format(cor['verde'],(num*num*num),cor['limpar']))
print('a raiz quadrada desse valor é {}{}{}'.format(cor['branco'],(math.sqrt(num)),cor['limpar']))

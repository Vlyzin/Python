#Crie um progama que leia um numero real qualquer e mostre sua parte inteira. (usando math)
 
from math import trunc as inteira

n = float(input('Digite um número qualquer(com virgula)? '))
cor = {'vermelho':'\033[1;31m','limpar':'\033[m','azul':'\033[1;36m','azul escuro':'\033[1;34m','branco':'\033[1;97m','amarelo':'\033[1;33m','verde':'\033[1;32m'}

print ('A parte \033[4;36minteira\033[m desse número é \033[7m{}\033[m'.format (inteira(n)))

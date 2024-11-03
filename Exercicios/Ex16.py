#Crie um progama que leia um numero real qualquer e mostre sua parte inteira. (usando math)
 
from math import trunc as inteira

n = float(input('Digite um número qualquer(com virgula)? '))

print ('A parte inteira desse número é {}'.format (inteira(n)))

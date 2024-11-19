#O mesmo professor quer decidir a ordem de apresentação de um projeto. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

n1 = 'João'
n2 = 'Gaby'
n3 = 'Vini'
n4 = 'Pedro'
lista = [n1,n2,n3,n4]

random.shuffle(lista)

print ('A ordem de apresentação será: ')
print ('\n{}'.format (lista))

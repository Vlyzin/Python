#Crie um programa que leia um numero inteiro qualquer e mostre se ele é par ou impar

n = int(input('Digite um número inteiro qualquer? '))

if n % 2 == 0:
    print ('Seu número é \033[1;97mpar\033[m!')
else:
    print ('Seu número é \033[1;32mimpar\033[m...')

#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados, exemplo:
#1834, unidades: 4, dezenas: 3, centenas: 8, milhar: 1.

numero = int(input('Digite um número inteiro entre 0 e 9999? '))
u= numero // 1 % 10
d= numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('O número {} tem \n{} unidades,\n{} dezenas,\n{} centenas e\n{} milhar(es)'.format(numero, (u),(d),(c),(m)))

#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados, exemplo:
#1834, unidades: 4, dezenas: 3, centenas: 8, milhar: 1.

numero = input('Digite um número inteiro entre 0 e 9999? ')

print('O número {} tem \n{} unidades,\n{} dezenas,\n{} centenas e\n{} milhar(es)'.format(numero, (numero[3]),(numero[2]),(numero[1]),(numero[0])))

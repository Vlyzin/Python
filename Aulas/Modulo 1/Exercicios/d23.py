#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados, exemplo:
#1834, unidades: 4, dezenas: 3, centenas: 8, milhar: 1.

numero = int(input('Digite um número inteiro entre 0 e 9999? '))
u= numero // 1 % 10
d= numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('O número \033[4m{}\033[m tem \n\033[1;32m{}\033[m unidades,\n\033[1;97m{}\033[m dezenas,\n\033[1;36m{}\033[m centenas e\n\033[1;32{}\033[m milhar(es)'.format(numero, (u),(d),(c),(m)))

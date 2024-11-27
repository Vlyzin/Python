#Faça um algoritimo que leia o salario de um funcionario e mostre o seu novo salario so que com 15% de aumento.

sal = float(input('Informe seu salario atual? '))
cor = {'vermelho':'\033[1;31m','limpar':'\033[m','azul':'\033[1;36m','azul escuro':'\033[1;34m','branco':'\033[1;97m','amarelo':'\033[1;33m','verde':'\033[1;32m'}

print ('Seu novo salario é de \033[1;34m{}\033[m reais!'.format(sal+(sal*0.15)))

#Faça um programa que calcule se o ano é bisexto ou não
from datetime import date as data
ano = int(input('Digite o ano para verificar se é bissexto? Digite 0 para o ano atual '))
if ano == 0:
    ano = data.today().year
if (ano % 4 == 0 and ano % 100 !=0) or (ano % 400 == 0):
    print ('O ano de \033[1m{}\033[m \033[1;36mé bissexto!\033[m'.format(ano))
else:
    print ('O ano \033[1m{}\033[m \033[1;31mnão é bissexto!\033[m'.format(ano))

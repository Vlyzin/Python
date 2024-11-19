#Faça um programa que calcule se o ano é bisexto ou não
ano = int(input('Digite o ano para verificar se é bisexto? '))

if (ano % 4 == 0 and ano % 100 !=0) or (ano % 400 == 0):
    print ('O ano é bisexto!')
else:
    print ('O ano não é bisexto')

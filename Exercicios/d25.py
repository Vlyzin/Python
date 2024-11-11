#Leia um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = input('Digite seu nome completo? ')

if(nome.find('Silva')) == -1:
    print('Seu nome não tem Silva!')
else:
    print('Seu nome tem Silva!')

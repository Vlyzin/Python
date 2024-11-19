#Leia um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = input('Digite seu nome completo? ').strip()

if 'silva' in nome.lower():
    print('Seu nome tem Silva!')
else:
    print('Seu nome não tem Silva!')

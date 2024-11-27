#Leia um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = input('Digite seu nome completo? ').strip()
cor={'limpar':'\033[m','verde':'\033[1;32m','vermelho':'\033[1;31m','amarelo':'\033[1;33m'}

if 'silva' in nome.lower():
    print('{}Seu nome tem {}Silva!{}'.format(cor['verde'],cor['amarelo'],cor['limpar']))
else:
    print('{}Seu nome não tem {}Silva!{}'.format(cor['vermelho'],cor['amarelo'],cor['limpar']))

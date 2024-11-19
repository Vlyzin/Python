#Programa que escolhe um número aleatorio entre 0 e 5 e peça para o usuario tentar descobrir, ele deve digitar na tela se o usuario ganhou ou perdeu
from random import randint as randomico
import time
numero = randomico(0,5)
resultado = 0
escolhido = int
vidas = 2

print('-=-' * 20)
print ('Vou pensar em um número entre 0 e 5...')
print('-=-' * 20)
time.sleep(5)


while resultado == 0:
    escolhido = int(input('Tente advinhar um número de 0 a 5? '))
    if escolhido == numero:
        resultado = 1
        print('Processando...\n')
        time.sleep(3)
        print('Acertou!! Você ganhou, parabéns!')
        exit()
    if vidas == 0:
        print('Você perdeu!! :( Tente novamente!!)')
        exit()
    else:
        vidas = vidas - 1
        print('Processando...\n')
        time.sleep(3)
        print('Tente novamente! Você ainda tem {} vidas\n'.format(vidas+1))

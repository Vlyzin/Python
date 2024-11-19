#Desenvolva um programa que leia o comprimento de três retas e diga se elas podem formar um triângulo

a = float(input('Digite o primeiro comprimento? '))
b = float(input('Digite o segundo comprimento? '))
c = float(input('Digite o terceiro comprimento? '))

if ((a + b) > c) and ((a + c) > b) and ((b+c) > a):
    print ('Esses comprimentos podem formar um triangulo!')
else:
    print ('Esses comprimentos não podem formar um triangulo...')
    
#Faça um programa que leia 3 numeros e mostre qual o maior e qual o menor

n1=float(input('Digite um número? '))
n2=float(input('Digite outro número? '))
n3=float(input('Outro número?! '))

maior = n1
menor = n1

if n1 == n2 == n3:
    print('Show os números são todos iguais kkk')
exit()
if n2 > maior:
    maior = n2
elif n3 > maior:
    maior = n3
elif n2 < menor:
    menor = n2
elif n3 < menor:
    menor = n3

print ('O maior número é {} e o menor número é {}'.format(maior, menor))

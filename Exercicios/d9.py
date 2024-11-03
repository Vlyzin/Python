# Faça um programa que leia um número inteiro qualquer e mostre sua tabuada
n = int(input('Digite um número: '))

for i in range(1, 11):
    resultado = n * i
    print('{} x {} vale {}'.format (n, i, resultado))

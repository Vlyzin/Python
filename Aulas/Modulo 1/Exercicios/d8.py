#Escreva um programa que receba um valor em metros e leia ele em centimetros e milimetros.

v = float(input('Digite um valor em metros? '))

print ('A conversão desse valor {} metros é de {:.5} centimetros e {:.10} milimetros'.format(v,(v*100),(v*1000)))

#Faça um programa que leia o nome completo de uma pessoa e mostre seu primeiro nome e seu ultimo nome, separadamento.

nome = input('Insira seu nome completo? ')
nome = nome.split()

print('Seu primeiro nome é: {} e seu ultimo nome é: {}'.format((nome[0]),(nome[-1])))

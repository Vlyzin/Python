#Faça um programa que leia o nome completo de uma pessoa e mostre seu primeiro nome e seu ultimo nome, separadamento.

nome = input('Insira seu nome completo? ').strip()
nome = nome.split()

print('Seu primeiro nome é: \033[1;33m{}\033[m e seu ultimo nome é: \033[1;35m{}\033[m'.format((nome[0]),(nome[-1])))

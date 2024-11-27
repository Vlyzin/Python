#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor
numero = int(input('Digite um número? '))
cor = {'vermelho':'\033[1;31m','limpar':'\033[m','azul':'\033[1;36m','azul escuro':'\033[1;34m','branco':'\033[1;97m','amarelo':'\033[1;33m','verde':'\033[1;32m'}

print ('O sucessor desse número é o número {}{}{}, e o antecessor é o número {}{}{}'.format (cor['verde'],(numero+1),cor['limpar'],cor['amarelo'],(numero-1),cor['limpar']))

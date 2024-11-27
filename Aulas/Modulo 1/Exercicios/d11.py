#Faça um programa que leia a altura e largura de uma parede em metros, calcule sua area e a quantidade de tinta necessaria para pinta-lá sabendo que 1l pinta 2m²
altura = int(input('Digite a altura(em metros) da parede? '))
largura = int(input('Digite a largura(em metros) da parede? '))
cor = {'vermelho':'\033[1;31m','limpar':'\033[m','azul':'\033[1;36m','azul escuro':'\033[1;34m','branco':'\033[1;97m','amarelo':'\033[1;33m','verde':'\033[1;32m'}

print ('Você precisará de \033[44m{}\033[m litros de tinta para pintar \033[1m{}m²\033[m'.format ((altura*largura/2), (altura*largura)))

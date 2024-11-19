#Faça um programa que leia a altura e largura de uma parede em metros, calcule sua area e a quantidade de tinta necessaria para pinta-lá sabendo que 1l pinta 2m²
altura = int(input('Digite a altura(em metros) da parede? '))
largura = int(input('Digite a largura(em metros) da parede? '))

print ('Você precisará de {} litros de tinta para pintar {} m²'.format ((altura*largura/2), (altura*largura)))

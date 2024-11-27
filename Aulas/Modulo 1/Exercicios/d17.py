#Ler os comprimentos do cateto oposto e cateto adjacente e mostre a hipotenusa  
from math import hypot as hipotenusa

c1 = float(input('Digite o valor do cateto oposto? '))
c2 = float(input('Digite o valor do cateto adjacente? '))
cor = {'vermelho':'\033[1;31m','limpar':'\033[m','azul':'\033[1;36m','azul escuro':'\033[1;34m','branco':'\033[1;97m','amarelo':'\033[1;33m','verde':'\033[1;32m'}

print ('A {}hipotenusa{} dos catetos inseridos é {}{:.2f}{}'.format (cor['amarela'],cor['limpa'],cor['amarela'],hipotenusa(c1,c2),cor['limpa']))

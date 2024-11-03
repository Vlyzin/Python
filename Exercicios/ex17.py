#Ler os comprimentos do cateto oposto e cateto adjacente e mostre a hipotenusa  
from math import hypot as hipotenusa

c1 = float(input('Digite o valor do cateto oposto? '))
c2 = float(input('Digite o valor do cateto adjacente? '))

print ('A hipotenusa dos catetos inseridos é {:.2f}'.format (hipotenusa(c1,c2)))

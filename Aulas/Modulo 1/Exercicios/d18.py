#Ler um angulo qualquer e mostre seno cosseno e tangente desse angulo

from math import sin, cos, tan, radians

a = float(input('Digite um angulo qualquer? '))
cor = {'vermelha':'\033[1;31m', 'azul':'\033[1;36m', 'verde':'\033[1;32m', 'limpar':'\033[m'}
a_rad = radians(a)

print ('O seno desse angulo vale {}{}{}'.format(cor['vermelha'], sin(a_rad),cor['limpar']))
print ('O seno desse angulo vale {}{}{}'.format(cor['azul'], cos(a_rad),cor['limpar']))
print ('O seno desse angulo vale {}{}{}'.format(cor['verde'], tan(a_rad),cor['limpar']))

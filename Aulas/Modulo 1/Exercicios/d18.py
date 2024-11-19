#Ler um angulo qualquer e mostre seno cosseno e tangente desse angulo

from math import sin, cos, tan, radians

a = float(input('Digite um angulo qualquer? '))

a_rad = radians(a)

print ('O seno desse angulo vale {}, o cosseno {}, e a tangente {}'.format(sin(a_rad),cos(a_rad),tan(a_rad)))

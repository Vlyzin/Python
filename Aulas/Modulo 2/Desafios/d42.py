#Refaça o desafio 35, dos triangulos acrescentando o recurso de mostrar que tipo de triangulo foi formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

a = float(input('Digite o primeiro comprimento? '))
b = float(input('Digite o segundo comprimento? '))
c = float(input('Digite o terceiro comprimento? '))

if ((a + b) > c) and ((a + c) > b) and ((b+c) > a):
    print ('Esses comprimentos podem formar um triangulo!')
else:
    print ('Esses comprimentos não podem formar um triangulo...')
    exit()

if a == b == c:
    print ("Você acabou de formar um triangulo equilátero ")
elif a == b or b == c or c == a:
    print ("Você acabou de formar um triangulo isóceles ")
elif a != b != c:
    print ("Você acabou de formar um triangulo Escaleno ")
    
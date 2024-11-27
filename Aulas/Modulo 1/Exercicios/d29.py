#Programa que leia a velocidade de um carro, se ele ultrapassar 80km/h mostre uma mensagem que ele ultrapassou, e foi multado, calculando a logica:
#7 reais a cada km excedente, se não passar suave.

vel = float(input('Qual a velocidade do carro? '))
    
if vel >80:
    print('Você foi \033[1;31mmultado\033[m! Ta muito rapido pai! Você deve pagar \033[4;32m{:.2f}\033[m reais de multa'.format((vel-80)*7))
else:
    print('\033[1;32mBoa! Ta de boa\033[m')
    exit()

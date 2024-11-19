#Programa que leia a velocidade de um carro, se ele ultrapassar 80km/h mostre uma mensagem que ele ultrapassou, e foi multado, calculando a logica:
#7 reais a cada km excedente, se não passar suave.

vel = float(input('Qual a velocidade do carro? '))
    
if vel >80:
    print('Você foi multado! Ta muito rapido pai! Você deve pagar {:.2f} reais de multa'.format((vel-80)*7))
else:
    print('Boa! Ta de boa')

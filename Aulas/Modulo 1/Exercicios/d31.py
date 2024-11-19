#Pergunte a distancia de uma viagem em KM e calcule o preço da passagem considerando 0.50R$/KM para viagens de até 200km e 0.45R$/KM para viagens mais longas.

distancia = float(input('Digite a distancia da sua viagem? '))

if distancia <=200:
    print('O valor da sua passagem é de {:.2f} reais'.format((distancia*0.50)))
else:
    print('O valor da sua passagem é de {:.2f} reais'.format((distancia*0.45)))
    
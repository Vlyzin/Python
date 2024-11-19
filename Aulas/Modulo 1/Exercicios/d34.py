#Pergunte o salario de um funcionario e calcule seu aumento, para salarios superiores a 1250R$ calcule um aumento de 10% para inferiores ou iguais, o aumento é de 15%

sal = float(input('Qual é o seu salario atual? '))

if sal > 1250.00:
    print('Seu novo salario é de {} reais'.format((sal+(sal*0.1))))
else:
    print ('Seu novo salario é de {} reais'.format((sal+(sal*0.15))))

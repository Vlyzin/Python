#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cidade = input('Digite o nome da cidade que você mora? ')
cidade = cidade.split()

if (cidade[0].find('Santo')) == -1:
    print ('O nome da sua cidade não começa com Santo!!')
else:
    print('O nome da sua cidade começa com Santo!!')

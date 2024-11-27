#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cidade = input('Digite o nome da cidade que você mora? ').strip()
cidade = cidade.split()

if cidade[0].lower() == 'santo':
    print('O nome da sua cidade \033[1;32mcomeça\033[m com \033[1;36mSanto\033[m!!')
else:
    print('O nome da sua cidade \033[1;31mnão começa\033[m com \033[1;36mSanto\033[m!!')

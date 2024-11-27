#Professor quer escolher um dos quatro alunos pra apagar o quadro, escolha e leia o nome dele
from random import choice
n1 = str(input('\033[1;97mDigite o primeiro nome? ')).strip()
n2 = str(input('Digite o segundo nome? ')).strip()
n3 = str(input('Digite o terceiro nome? ')).strip()
n4 = str(input('Digite o quarto nome? ')).strip()

print ('\033[mO aluno selecionada para apagar o quadro é: \033[1;32m{}\033[m'.format(choice([n1,n2,n3,n4])))

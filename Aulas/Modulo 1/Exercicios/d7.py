#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media

nota1 = float(input('Digite sua primeira nota? '))
nota2 = float(input('Digite sua segunda nota? '))
media = ((nota1+nota2)/2)
cor = {'vermelho':'\033[1;31m','limpar':'\033[m','azul':'\033[1;36m','azul escuro':'\033[1;34m','branco':'\033[1;97m','amarelo':'\033[1;33m','verde':'\033[1;32m'}

if media < 6:
    print ('Sua média de notas é {}{}{} Estude mais!!'.format(cor['vermelho'],media,cor['limpar']))

else:
    print('Sua média de notas é {}{}{}, Parabéns!'.format(cor['verde'],media,cor['limpar']))
    
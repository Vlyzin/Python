#Faça um algoritimo que leia o preço de um produto e calcule seu novo preço com 5% de desconto.

prod = float(input('Qual o preço do produto? '))
cor = {'vermelho':'\033[1;31m','limpar':'\033[m','azul':'\033[1;36m','azul escuro':'\033[1;34m','branco':'\033[1;97m','amarelo':'\033[1;33m','verde':'\033[1;32m'}

print ('O preço do produto com \033[32m desconto de 5%\033[m é de \033[1;36m{}\033[m reais!'.format ((prod-(prod*0.05))))

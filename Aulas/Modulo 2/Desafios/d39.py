##Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a idade:
# - Se ele ainda vai se alistar ao serviço militar; Se é hora de se alistar; Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import *

ano = int(input("Digite o ano do seu nascimento: "))

if ((datetime.now().year)-(ano)) == 18:
    print (f"Você tem {ano}, é hora de se alistar guerreiro!")
elif datetime.now().year - ano <18:
    print(f"Você ainda deverá se alistar! Faltam {18-(datetime.now().year-ano)} ano(s) para o seu alistamento!")
else:
    print(f"Você já deveria ter se alistado! O prazo já passou em {(datetime.now().year-ano)-18} anos, procure um alistamento!")

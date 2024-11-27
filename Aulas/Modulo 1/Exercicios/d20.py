import random

n1 = 'João'
n2 = 'Gaby'
n3 = 'Vini'
n4 = 'Pedro'
lista = [n1, n2, n3, n4]

cor = {'ciano': '\033[1;96m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m', 'caqui': '\033[1;35m'}
limpar = '\033[m'

cores = list(cor.values())
random.shuffle(lista)
random.shuffle(cores)

print('A ordem de apresentação será: ')
for i in range(4):
    print(f'{cores[i]}{lista[i]}{limpar}')
    
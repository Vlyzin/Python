#Crie um programa que leia o nome completo e exiba: Nome com todas as LETRAS MAISCULAS nome com todas as letras minusculas, 
#quantas letras ao todo(sem espaço), quantas letras tem o primeiro nome

nome = input('Digite seu nome completo? ').strip()
espaço=nome.replace(' ', '')
dividido = nome.split()

print (nome.upper(), nome.lower())

print('O nome possui \033[1m{}\033[m letras ao total (sem espaço) e o primeiro nome tem \033[4m{}\033[m letras'.format((len(espaço)), (len(dividido[0]))))

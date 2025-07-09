#Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input("Digite um número inteiro: "))

base = int(input("Escolha qual será a base de conversão do número, 1 para binario, 2 para octal e 3 para hexadecimal "))

if base == 1:
    print(f"O número {numero} convertido para a base binaria resulta em: {bin(numero)}")

elif base == 2:
    print(f"O número {numero} convertido para a base binaria resulta em: {oct(numero)}")

else:
    print(f"O número {numero} convertido para a base binaria resulta em: {hex(numero)}")

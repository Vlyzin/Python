#Ler dois numeros inteiros e comparar dizendo: O primeiro é maior, o segundo é maior ou são iguais

n1 = input('Digite um número: ')
n2 = input('Digite outro número a ser comparado com o primeiro: ')

if n1 == n2:
    print(f"O números {n1} e {n2} são iguais!")
elif n1 > n2:
    print (f"O primeiro número ( {n1} ) é maior que o segundo número ( {n2} )")
else:
    print(f"O segundo número ( {n2} ) é maior que o primeiro número( {n1} )")

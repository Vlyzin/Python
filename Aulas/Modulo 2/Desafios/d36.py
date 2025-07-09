#Escreva um programa que aprove o emprestimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# O valor da prestação não pode ser superior a 30% do salário. Caso ultrapasse o valor será negado

valorcasa = float(input("Qual o valor da casa que deseja comprar: "))
salario = float(input("Qual o seu salario atual: "))
anos = float(input("Quantos anos pretende pagar: "))
prestacao = (valorcasa) / (anos*12)

if (prestacao >(salario*0.3)):
    print("Seu salario não é suficiente para a prestação da casa, emprestimo negado.")

else:
    print("Seu emprestimo foi aprovado!")

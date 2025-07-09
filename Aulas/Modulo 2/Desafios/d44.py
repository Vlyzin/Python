#Elabore um programa que calcula o valor pago por um produto, considerando o seu preço normal e condição de pagamento:
## - À vista dinheiro/cheque: 10% de desconto
## - À vista no cartão: 5% de desconto
## - Em até 2x no cartão: preço normal
## - 3x ou mais no cartão: 20% de juros

valor = float(input("Digite o valor do produto: "))
pagamento = int(input("Selecione a forma de pagamento:\n1. Pix / Dinheiro\n2. Cartão\n "))

if pagamento == 1 :
    print (f"O valor final do produto optando por essa forma de pagamento é de {(valor-(valor*0.1))} reais")

if pagamento == 2:
    modal=input("Você gostaria de pagar a vista ou parcelado?\n 1. À vista\n 2. Parcelado\n")

    if modal == 2
    
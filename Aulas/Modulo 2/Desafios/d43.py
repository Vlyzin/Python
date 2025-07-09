#Ler o peso e altura de uma pessoa e calcular o IMC (Índice de Massa Corporal) e mostrar sua classificação:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - Entre 25 e 30: Sobrepeso
# - Entre 30 e 40: Obesidade
# - Acima de 40: Obesidade mórbida

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))
imc = (peso/altura**2)

if imc < 18.5:
    print (f"O seu IMC é de {imc:.2f}. Você está abaixo do peso ideal.")
    
elif imc >= 18.5 and imc <=25:
    print (f"O seu IMC é de {imc:.2f}. Você está no peso ideal.")

elif imc > 25 and imc <=30:
    print (f"O seu imc:2.f é de {imc:.2f}. Você está com sobrepeso.")

elif imc >30 and imc <=40:
    print (f"O seu IMC é de {imc:.2f}. Você está com obesidade, se cuida por favor.")

elif imc > 40:
    print (f"O seu IMC é de {imc:.2f}. Você está com obesidade mórbida, se cuida por favor!.")
exit()
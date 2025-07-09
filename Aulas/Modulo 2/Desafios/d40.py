#Crie um programa que lei duas notas de um aluno, calcule e mostre a sua média: abaixo de 5 reprovado, entre 5 e 6.9 recuperação, 7 ou superior aprovado

nota = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))

media = (nota + nota2) / 2

if media < 5:
    print (f"Você está reprovado!! sua media foi de {media} pontos.")
elif media > 5 and media <= 6.9:
    print (f"Você está de recuperação, sua media foi de {media} pontos.")
else:
    print (f"Parabéns, você foi aprovado! sua media foi de {media} pontos")

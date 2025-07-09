#Leia o ano de nascimento de um atleta e mostre sua categoria:
# - Até 9 anos: Mirim
# - Até 14 anos: Infantil
# - Até 19 anos: Junior
# - Até 25 anos: Sênior
#Acima de 25 anos: Master

from datetime import datetime

while True:
    idade = datetime.now().year - int(input("Digite qual ano você nasceu: "))

    if idade > 80:
        print(f"Você não tem {idade} anos, fala sua idade verdadeira...")
        continue 

    break

if idade <= 9:
    print(f"Você tem {idade} anos. Sua categoria é Mirim!")
elif idade <= 14:
    print(f"Você tem {idade} anos. Sua categoria é Infantil!")
elif idade <= 19:
    print(f"Você tem {idade} anos. Sua categoria é Junior!")
elif idade <= 25:
    print(f"Você tem {idade} anos. Sua categoria é Sênior!")
else:
    print(f"Você tem {idade} anos. Sua categoria é Master!")

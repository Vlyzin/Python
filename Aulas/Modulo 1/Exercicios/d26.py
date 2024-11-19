#Leia uma frase qualquer, e diga quantas vezes aparece a letra "a", em que posição aparece a primeira e em que posição aparece na ultima vez.

frase = input('Insira uma frase qualquer? ').strip().upper()

print ('A letra "a" aparece {} vez(es) na sua frase: " {} ",\nA primeira posição que a letra "a" aparece é a {}\nA ultima posição é {}'.format((frase.count('A')), frase.capitalize(),(frase.find('A')+1), (frase.rfind('A'))))

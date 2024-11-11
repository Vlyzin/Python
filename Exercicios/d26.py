#Leia uma frase qualquer, e diga quantas vezes aparece a letra "a", em que posição aparece a primeira e em que posição aparece na ultima vez.

frase = input('Insira uma frase qualquer? ')

print ('A letra "a" aparece {} vez(es) na sua frase: " {} ",\nA primeira posição que a letra "a" aparece é a {}\nA ultima posição é {}'.format((frase.count('a')), frase,(frase.find('a')), (frase.rfind('a'))))

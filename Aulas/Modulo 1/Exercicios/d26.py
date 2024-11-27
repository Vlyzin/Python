#Leia uma frase qualquer, e diga quantas vezes aparece a letra "a", em que posição aparece a primeira e em que posição aparece na ultima vez.

frase = input('Insira uma frase qualquer? ').strip().upper()

print ('A letra "a" aparece \033[4m{}\033[m vez(es) na sua frase: " \033[0;33m{}\033[m ",\nA primeira posição que a letra "a" aparece é a \033[1m{}\033[m\nA ultima posição é \033[1;36m{}\033[m'.format((frase.count('A')), frase.capitalize(),(frase.find('A')+1), (frase.rfind('A'))))

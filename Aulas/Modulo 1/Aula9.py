frase = 'Curso em video Python'

#Analise
print(len(frase))

print(frase.count('o',0,13))

print(frase.find('deo'))

print(('Curso' in frase))

print(frase.find('Android'))

print (frase[9:21:2])

print (frase[:5])

print(frase[15:])

print(frase[9::3])

print(frase)

#Transformação
frase.replace('Python','Android')

print((frase.replace('Python','Android')))

print(frase.title())

print(frase.rstrip())

#Dividr
dividido = frase.split()
print(dividido[0][::2])

print((' '.join(frase)))

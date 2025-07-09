## Aula 12 - Condições aninhadas
nome = input('Digite seu nome: ')
if nome == 'João':
    print('Que nome bonito!')
elif nome in ['Pedro', 'Vinicius', 'Maria']:
    print('Nome muito comum!')
else:
    print('Seu nome é interessante!')
print(f"Tenha um bom dia, {nome}!")
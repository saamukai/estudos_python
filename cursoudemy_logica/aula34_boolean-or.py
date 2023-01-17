nome = input('Qual o seu nome? ')

if nome:
    print(nome)
else:
    print("voce não digitou nada =(")

# todo esse if acima pode ser reduzido ao operador or

print(nome or 'Voce não digitou nada')

a = 0
b = None
c = False
d = []
e = {}
f = 13
g = 'Samuel'

variavel = a or b or c or d or e or f or g

print(variavel)

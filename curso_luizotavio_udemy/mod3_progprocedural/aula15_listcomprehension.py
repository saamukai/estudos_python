# LIST COMPREHENSION - COMPREENSÕES DE LISTA

l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [var for var in l1]

# supondo que queria multiplicar cada elemento por 2:
# list comprehension fica 'melhor'
ex2 = [v*2 for v in l1]
print(ex2)

# exp3 - criando tuplas a partir de l1
ex3 = [(v,v2) for v in l1 for v2 in range(3)]
print(ex3)

l2 = ['Luiz', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@').upper() for v in l2]
print(ex4)

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)
ex5 = [(x,y) for x,y in tupla]
print(ex5)
ex5inv = [(y,x) for x,y in tupla] # invertendo valor da chave e valor
print(ex5inv)
ex5 = dict(ex5)
print(ex5)

# pode usar condições
l3 = list(range(100))
ex6 = [v for v in l3 if v%3 == 0 if v % 8 == 0]
print(f'\n{ex6}\n')

    # ternário
ex7 = [v if v % 3 == 0 and v % 8 == 0 else 'o' for v in l3]
print(ex7)

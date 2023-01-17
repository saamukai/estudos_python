"""
Split - dividir uma string
Join - juntar uma lista
enumerate - enumerar elemetnos de uma lista
"""

string = "O Brasil é penta."
lista1 = string.split(' ') # separa onde tiver esppaço

for indice, valor in enumerate(lista1):
    print(indice, valor, lista1[indice])


lista = [
    [0, 'Luiz'],
    [1, 'João'],
    [2, 'Maria']
]

for indice, nome in lista:
    print(indice, nome)


lista2 = ['Luiz', 'JOAO', 'maria']
n1, n2, n3 = lista

print(n2)

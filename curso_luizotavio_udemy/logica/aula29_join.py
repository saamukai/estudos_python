"""
Split - dividir uma string
Join - juntar uma lista
enumerate - enumerar elemetnos de uma lista
"""

string = "O Brasil é o o o país do futebol, o Brasil é penta."
lista1 = string.split(' ') # separa onde tiver esppaço
lista2 = string.split(',') # separa onde tiver virgula

string2 = ','.join(lista1) ##junta a lista em uma string
print(string2)

string3 = ' '.join(lista1) ## com o caractere definido entre cada elemento da lista
print(string3)

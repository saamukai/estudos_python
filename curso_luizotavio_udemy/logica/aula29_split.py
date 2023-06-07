"""
Split - dividir uma string
Join - juntar uma lista
enumerate - enumerar elemetnos de uma lista
"""

string = "O Brasil é o o o país do futebol, o Brasil é penta."
lista1 = string.split(' ') # separa onde tiver esppaço
lista2 = string.split(',') # separa onde tiver virgula

print(lista1)
print(lista2)

for valor in lista1: ##foreach, contar palavras
    print(f'A palavra apareceu {valor} apareceu {lista1.count(valor)}x na frase')

palavra = ''
contagem = 0

for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes eh {palavra} ({contagem}x)\n')

#####################################################################
print("################################################\n")

for valor in lista2:
    print(valor.strip().capitalize())

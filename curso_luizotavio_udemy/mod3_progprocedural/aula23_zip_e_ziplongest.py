from itertools import zip_longest, count

indices = count()
cidades = ['Brasília', 'Goiânia', 'Uberlândia', 'Foz']
estados = ['DF', 'GO', 'MG']

cidades_estado = zip(indices, estados, cidades)

for indice, cidade, estado in cidades_estado:
    print(indice, cidade, estado)

# print(tuple(cidades_estado))


# cidades_estado = zip_longest(cidades, estados)
# print(tuple(cidades_estado))

# consumindo:
# print(next(cidades_estado))
# print(next(cidades_estado))
# print(next(cidades_estado))

def funcao (arg, arg2):
    return arg * arg2

var = funcao(2,2)
print(var)

# a mesma funcao acima, de forma anomina, usando lambda
a = lambda x, y: x * y
print(a(2,2))

##################
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

## substituir pelo lambda
# def func(item):
#     return item[1]

lista.sort(key=lambda item: item[1],reverse=True) #altera a lista
print(lista)
print(sorted(lista, key=lambda item: item[1])) #nao altera a lista, ordena somente na impressao

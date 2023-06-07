import sys

lista1 = [x for x in range(1000)] # LISTA NORMAL (iterável)
lista2 = (x for x in range(1000)) # LISTA feita com gerador (generator)

print(f'LISTA 1: {type(lista1)}, TAM: {sys.getsizeof(lista1)}')
print(f'LISTA 2: {type(lista2)}, TAM: {sys.getsizeof(lista2)}')


# for valor in lista1:
#     print(f'LISTA1 VALOR: {valor}')

for valor in lista2:
    print(f'LISTA2 VALOR: {valor}')


# OUTRA MANEIRA: USANDO YIELD

def gera():
    for valor in range(1000):
        yield valor
        # yield é tipo um return, só que retorna um gerador
        # e a func continua rodando

for valor in gera():
    print(valor)

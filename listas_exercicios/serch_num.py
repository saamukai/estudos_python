

# Função que encotnra o primeiro duplicado:
matriz_inteiros = [
    [1,2,3,4,5,6,7,8,9,10],
    [9,1,8,9,9,7,2,1,5,8],
    [1,3,2,2,8,6,5,9,6,7],
    [8,2,8,6,2,4,5,6,1,7],
]

def search_first_duplicate(lista):
    iguais = []
    indice = len(lista)
    for indice, num in len(lista):
        # if j >= 1:
        #     if num[j] == num[j-1]:
        #         iguais = iguais.append(num[j])
        # print(iguais)

    return lista


def searchDuplicate(matriz):
    for lista in matriz:
        search_first_duplicate(lista)


searchDuplicate(matriz_inteiros)

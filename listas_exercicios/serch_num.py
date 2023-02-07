

# Função que encotnra o primeiro duplicado:
matriz_inteiros = [
    [1,2,3,4,5,2,7,8,3,10],
#    [9,1,8,9,9,7,2,1,5,8],
#    [1,3,2,2,8,6,5,9,6,7],
#    [8,2,8,6,2,4,5,6,1,7],
]

def search_first_duplicate(lista):
    iguais = []

    for compair in lista:
        i = 0
        for num in lista:
            print(f'# {compair} x {num}')
            if num == compair:
                print(f'conta {i}')
                i += 1

    print(iguais)



    return lista


def searchDuplicate(matriz):
    for lista in matriz:
        search_first_duplicate(lista)


searchDuplicate(matriz_inteiros)



# Função que encotnra o primeiro duplicado:
matriz_inteiros = [
    [1,2,3,4,5,2,7,8,3,10],
    [9,1,8,9,9,7,2,1,5,8],
    [1,3,2,2,8,6,5,9,6,7],
    [8,2,8,6,2,4,5,6,1,7],
    ]

def search_last_duplicate(lista):
    sem_repeticao = list(set(lista))
    iguais = []
    for compair in sem_repeticao:
        contador = 0
        for num in lista:
            if compair == num:
                contador += 1

        if contador > 1:
            iguais.append(compair)

    return iguais[-1]

def search_first_duplicate(lista):
    checkeds = set()
    first_duplicate = -1

    for num in lista:
        if num in checkeds:
            first_duplicate = num
            break

        checkeds.add(num)

    return first_duplicate

def searchDuplicate(matriz):
    for lista in matriz:
        last_dup = search_last_duplicate(lista)
        first_dup = search_first_duplicate(lista)
        print(f'***{lista}***\nFIRST: {first_dup}\nLAST:{last_dup}')


searchDuplicate(matriz_inteiros)

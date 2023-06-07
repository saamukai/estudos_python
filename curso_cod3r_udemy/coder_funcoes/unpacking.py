def soma_2(a, b):
    return float(a+b)


def soma_3(a, b, c):
    return float(a+b+c)


def soma_nomeada(a, b, c=0):
    return float(a+b+c)


def soma_n(*numeros):
    soma = 0
    for num in numeros:
        soma += num
    return soma


if __name__ == '__main__':

    # PACKING
    print('PACKING:')
    print(soma_2(2, 4))
    print(soma_3(2, 4, 6))
    print(soma_nomeada(1, 2))
    print(soma_nomeada(1, 2, 10))
    print(soma_n(1, 2))
    print(soma_n(1, 4, 5, 10, 15, 20))

    # UNPACKING
    print('\nUNPACKING:')
    tupla_nums = (2, 4, 5)
    print(soma_n(*tupla_nums))  # os parametros meio que são passados 1 a 1

    lista_nums = [10, 20, 30, 50]
    print(soma_n(*lista_nums))


def dobro(x):
    return x*2

def quadrado(x):
    return x**2


if __name__ == '__main__':
    d = dobro # var pode receber função
    print(d(5))

    q = quadrado
    print(q(5))

    # Retornar alternademente o dobro ou quadrado do numeros de 1 a 10
    funcs = [dobro, quadrado] * 5 # multiplica as listas e concatena
    print(funcs)
    for func, numero in zip(funcs, range(1,111)):
        print(f'O {func.__name__} de {numero} é {func(numero)}')

def fibonacci_ternario(quantidade, sequencia=(0,1)):
    return sequencia if len(sequencia) == quantidade else \
        fibonacci_ternario(quantidade, sequencia + (sum(sequencia[-2:]),))

def fibonacci(quantidade, sequencia=(0,1)):
    # condicao de parada:
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))

if __name__ == '__main__':
    print('\nFib ternario: ')
    for fib in fibonacci_ternario(10):
        print(fib, end=', ')

    #lista uma quantidade de numeros de fibonacci dada uma determinada qtd
    print('\nFib QTD: ')
    for fib in fibonacci(10):
        print(fib, end=', ')

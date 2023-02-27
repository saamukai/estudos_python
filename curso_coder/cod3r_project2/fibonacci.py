
def fibonacci_lim(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(sum(resultado[-2:]))
        if sum(resultado[-2:]) > limite:
            break
    return resultado

def fibonacci_qtd(quantidade):
    resultado = [0,1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break;
    return  resultado

if __name__ == '__main__':
    #lista um indeterminado numero da sequencia de fibonacci dado um certo limite
    print('Fib LIM: ')
    for fib in fibonacci_lim(100):
        print(fib, end=' ,')

    #lista uma quantidade de numeros de fibonacci dada uma determinada qtd
    print('\nFib QTD: ')
    for fib in fibonacci_qtd(10):
        print(fib, end=' |')

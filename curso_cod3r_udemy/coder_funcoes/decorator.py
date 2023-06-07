
def log_da_funcao(function):
    def decorator(*args, **kwargs):
        print(f'Inicio da chamada da funcao: {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator


@log_da_funcao
def soma(x, y):
    return x + y


@log_da_funcao
def sub(x, y):
    return x - y


if __name__ == '__main__':
    print(soma(5,7))
    print('----------')
    print(sub(5, y=7))

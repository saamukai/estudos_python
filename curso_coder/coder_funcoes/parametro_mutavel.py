"""
É possível que tenha probleams ao trabalhar com
parametros MUTAVEL como uma lista, por exemplo
visto que uma listra cria não é  uma "variavel descartavel"
e sim cria uma espaço na memoria, entao no momento em que
voce queira reiniciar uma lista pode ter diversos problas
Exemplo
"""

def fibonacci(sequencia=[0,1]):
    # uso de mutáveis como valor default (armadilha):
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


""" RESOLVENDO O PROBLEMA """
def fibonacci_resolvido(sequencia=None):
    sequencia = sequencia or [0,1]
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio)) # [0,1,1] {endereço}
    print(fibonacci(inicio)) # [0, 1, 1, 2] -> certo
    """"
    Abaixo, é esperado que reinicie o fibonacci visto que
    ao chamar a função novamente sem parametros
    ele deviaria chegar somente o valor default [0,1] ou [0,1,1]
    """
    restart = fibonacci() # é esperado que reinicie o fibonacci
    print(restart, id(restart)) # [0, 1, 1, 2, 3] {mesmo endereço}
    """
    Observe que isso nao acontece ja que funcao foi inciada com uma
    lista e uma lista é um vetor e reserva um lugar 'fixo' na memoria.
    """
    assert restart == [0,1,1] # retorna erro pois nao é isso

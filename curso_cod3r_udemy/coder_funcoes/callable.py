
def executar(funcao):
    return funcao() if callable(funcao) else print('mamaco')


def bom_dia():
    print('Bom dia, yeaaah!')


def boa_tarde():
    print('Boa noite rafamoreira meu mano!')


if __name__ == '__main__':
    executar(bom_dia)
    executar(boa_tarde)
    executar(1)  # n vai ser executado.
    print('rafa moreira mano')

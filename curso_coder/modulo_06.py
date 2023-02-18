#!/usr/bin/python3
from math import pi, pow
import sys
import errno


# cores
class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def help():
    print('É necessário informar o raio do circulo')
    print( f'Sintaxe { sys.argv[0] } <raio>')


def calculaArea(raio):
    return pi * pow(raio,2)


if __name__ == '__main__':
    # raio = float(input('Digite o valor do raio: '))
    # print(calculaArea(raio)

    # utilizando argumentos:
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        error_text = 'O raio deve ser um valor numerico'
        print(TerminalColor.ERRO + error_text + TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)

    # else:
    raio = float(sys.argv[1])
    area = calculaArea(raio)
    print(f'A area do circulo eh: {area}')

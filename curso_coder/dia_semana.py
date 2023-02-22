def get_tipo_dia(dia):
    dias = {
        1: 'FDS',
        2: 'Semana',
        3: 'Semana',
        4: 'Semana',
        5: 'Semana',
        6: 'Semana',
        7: 'FDS'
    }
    return dias.get(dia, '*** dia invalido **')

if __name__ == '__main__':
    for dia in range(0,9):
        print(f'{dia}: {get_tipo_dia(dia)}')

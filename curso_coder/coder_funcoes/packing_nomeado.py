def resultado_f1_kwargs(**podium):
    for posicao, nome in podium.items():
        print(f'{posicao} -> {nome}')

def resultado_f1_unpacking(primeiro, segundo, terceiro):
    print(f'1 -> {primeiro} \
          \n2 -> {segundo} \
          \n3 -> {terceiro}')


if __name__ == '__main__':
    resultado_f1_kwargs(primeiro='L. Hamilton', segundo='S. Vettel', terceiro='M. Verstappen')

    podium = {
        'primeiro': 'L. Hamilton',
        'segundo': 'S. Vettel',
        'terceiro': 'M. Verstappen',
    }

    resultado_f1_unpacking(**podium)

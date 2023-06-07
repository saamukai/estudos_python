class Humano:
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_carvernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self



if __name__ == '__main__':
    jose = Humano('José')
    grokn = Humano('Grokn').das_carvernas()

    print(f'Humano Especie: {Humano.especie}')
    print(f'jose.especie: {jose.especie}')
    print(f'grokn.especie: {grokn.especie}')

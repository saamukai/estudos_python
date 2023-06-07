
class Animal:
    @property
    def capacidades(self):
        return ('dormir', 'comer', 'beber')


class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('pagar por comida', 'pagar pra viver')


class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('andar na parede', 'fazer teia')


class HomemAranha(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + ('bater em moscão', 'jogar teia nos predio')

if __name__ == '__main__':
    abebe_bikila = Homem()
    aranha = Aranha()
    peter_parker = HomemAranha()

    print(f'ARANHA: {aranha.capacidades}')
    print(f'HUMANO: {abebe_bikila.capacidades}')
    print(f'PETER PARKER: {peter_parker.capacidades}')

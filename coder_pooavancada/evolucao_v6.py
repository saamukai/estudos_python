from abc import ABCMeta, abstractproperty


class Humano(metaclass=ABCMeta):
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None  # _ : Atributo privado

    @abstractproperty
    def inteligente(self):
        pass

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um numero positivo')
        self._idade = idade

    def das_carvernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopitecos',) + tuple(f'Home {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]

    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True


if __name__ == '__main__':

    # try:
    #     anonimo = Humano('Jhon Doe')
    #     print(anonimo.inteligente)
    # except TypeError:
    #     print('Propriedade Abstrata')

    jose = HomoSapiens('José')
    grogn = Neanderthal('Grogn')
    print(f'{jose.nome} da classe {jose.__class__.__name__}, {jose.inteligente}')
    print(f'{grogn.nome} da classe {grogn.__class__.__name__}, {grogn.inteligente}')

class ClasseSimples:
    contador = 0

    # @classmethod
    # def __init__(cls):
    #     cls.contador += 1

    def __init__(self):
        # self.__class__.contador += 1
        self.contar()

    @classmethod
    def contar(cls):
        cls.contador += 1


if __name__ == '__main__':
    classes = [ClasseSimples(), ClasseSimples()]
    print(ClasseSimples.contador)

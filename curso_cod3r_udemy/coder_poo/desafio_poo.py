from datetime import datetime, timedelta


class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = int(idade)

    def __str__(self):
        return f'{self.nome}, {self.idade} anos.'


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = float(salario)


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registrar_compra(self, compra):
        self.compras.append(compra)

    def get_data_ultima_compra(self):
        return self.compras[-1].data

    def total_compras(self):
        quantidade = len(self.compras)
        total = 0
        for compra in self.compras:
            total += compra.valor
        return f'{quantidade} COMPRAS, VALOR TOTAL {total}'


class Compra():
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = datetime.now()
        self.valor = valor

    def __str__(self):
        return f'{self.vendedor} | {self.data} | {self.valor} R$ |'


if __name__ == '__main__':
    vendedor = Vendedor('Samuel', 20, 2562152)
    cliente = Cliente('Jonathan', 20)

    compra = Compra(vendedor, cliente, 2520.52)
    compra2 = Compra(vendedor, cliente, 3000.52)

    print(f'VENDEDOR: {vendedor}')
    print(f'CLIENTE: {cliente}')
    print(f'COMPRA: {compra}')
    print(f'COMPRA2: {compra2}')

    cliente.registrar_compra(compra)
    cliente.registrar_compra(compra2)
    print(cliente.total_compras())
    print(cliente.get_data_ultima_compra())

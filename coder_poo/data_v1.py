class Data:
    def __init__(self, dia='01', mes='01', ano='0000'):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 12, 2019)
print(d1)


d2 = Data(4, '06', 20223)
print(d2)

d3 = Data()
print(d3)

d4 = Data(mes='05')
print(d4)

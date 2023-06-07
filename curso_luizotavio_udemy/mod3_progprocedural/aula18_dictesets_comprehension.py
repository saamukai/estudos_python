lista = [
    ('chave', 'valor2'),
    ('chave2', 'valor2'),
]

##### DICT COMPREHENSIONS
# d1 = dict(lista)
d1 = {c: v for c, v in lista}
print(d1, type(d1))

d2 = {(c+1): v*2 for c,v in enumerate(range(5))}
print(d2, type(d2))

d3 = {f'chave_{x}': x**2 for x in range(5)}
print(d3, type(d3))

##### SET COMPREHENSION
set1 = {tupla for tupla in lista}
print(set1, type(set1))


set2 = {valor for valor in range(5)}
print(set2, type(set2))

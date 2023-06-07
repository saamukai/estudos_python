carrinho = []

carrinho.append(('Produto1', 30))
carrinho.append(('Produto2', 50))
carrinho.append(('Produto3', 20))
carrinho.append(('Produto4', 50))

total1 = sum([float(valor[1]) for valor in carrinho])
print(total1)

total2 = sum([float(valor) for nome, valor in carrinho])
print(total2)
# ---- PEGA OS PRODUTOS
# for produto in carrinho:
#     print(produto,type(produto))

# prod = [produto for produto in carrinho]
# print(prod)


# ------ PEGA OS VALORES
# for produto in carrinho:
#     print(produto[1])

# valor = [valor[1] for valor in carrinho]
# print(valor)


# ----- SOMA OS VALORES
# soma = 0
# for produto in carrinho:
#     soma += produto[1]

# print(soma)

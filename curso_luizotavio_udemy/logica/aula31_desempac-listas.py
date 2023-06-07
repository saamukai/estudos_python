lista = ['Luiz', 'JOAO', 'maria']
n1, n2, n3 = lista ## tem q ter a mesma qunatidade de itens e variaves ou o ponteiro

print(n2)

n1, n2, *outra_lista = lista #o ponteiro cria uma nova lista para o restante dos valores

print(n1)

n1, n2, *_ = lista # faz a mesma coisa que a acima, todavia o
                    # underline indica que não se preocupa com o restante dos valores

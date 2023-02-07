# set
s1 = set()
s1.add('a')
s1.update([1,2,3,3,3], [1,2,2,2,4,5])

#set geralmente usado para remover elementos duplicados em uma lista.
l1 = [1,1,1,2,2,2,3,3,3,1,1,1,4, 'Samuel', 'Jonathan', 'Samuel']
l1 = set(l1)

# não tem mais elementos repetidos
l1 = list(l1) # volta pra list
s2 = set(l1)

print(f'\n\nSET 1 = {s1}\nSET 2= {s2}')

print('\n#### Union')
s3 = s1 | s2
print(s3)

print('\n#### Intersection')
s3 = s1 & s2
print(s3)

print('\n#### Difference')
s3 = s1 - s2
print(s3)

print('\n#### Symmetric Differencce ("complemento")')
s3 = s1 ^ s2
print(s3)
print ('===============================')

lista1 = ['Luiz', 'João', 'Maria']
lista2 = ['João', 'Maria', 'Maria', 'Luiz', 'Luiz']

print(lista1 != lista2) # é diferente

    # se eu  quiser ignorar os repetidos
# comparar se sao iguais sem mexer na lista
print(set(lista1) != set(lista2)) # false, agora é igual

# ou alterando e ao mesmo tmepo voltando a lista
lista1 = list(set(lista1))
lista2 = list(set(lista2))

if lista1 == lista2:
    print('Igual, possui os mesmo elemetnos')
else:
    print('Difernte, tem coisa diferente')

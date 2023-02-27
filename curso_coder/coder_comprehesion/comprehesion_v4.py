generator = (i**2 for i in range(10) if i%2 == 0)

for numero in generator:
    print(numero)


dicionario = {j: j*2 for j in range(10) if j%2!=0}


for numero, dobro in dicionario.items():
    print(f'{numero} x 2: {dobro}')

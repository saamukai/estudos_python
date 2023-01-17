l2 = list(range(1,10))
print(l2)

soma = 0;

for valor in l2:
    soma += valor;
    print(f'{soma} + {valor} = {soma}')

print(soma)
print('######################\n')

###############################################
l3 = ['String', True, 10, -20.5]

for elemento in l3:
    print(f'O tipo de {elemento} é {type(elemento)}')

print('######################\n')

###############################################
secreto = 'perfume'
digitadas = []

while True:
    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Ahhh, isso nao vale, digite apenas uma letra")
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra {letra} existe na palavra secreta')
    else:
        print(f'A letra {letra} nao existe na palavra secreta')
        digitadas.pop()


    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    print(secreto_temp)

    if secreto_temp == secreto:
        print(f'que legal, voce ganhou! A palavra era {secreto_temp}')
        break
    else:
        print(f'A palavra secreta está assim {secreto_temp}')

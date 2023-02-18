# Adivinhe o numero secreto (gerado)
from random import randint

numero_informado = -1
numero_secreto = randint(0,9)

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe um numero: '))

    if numero_informado != numero_secreto:
        print('Número informado não é o mesmo do secreto')

print('Parabens voce adivinhou o numero')

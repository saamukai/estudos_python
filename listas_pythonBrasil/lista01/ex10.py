# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    # o produto do dobro do primeiro com metade do segundo .
    # a soma do triplo do primeiro com o terceiro.
    # o terceiro elevado ao cubo. 

from numbers import Real


num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))
numReal = float(input("Digite um numero real: "))

a = (2*num1)*(num2/2);
b = (num1*3)+numReal;
c = numReal**3;

print(f"{a}\n{b}\n{c}")
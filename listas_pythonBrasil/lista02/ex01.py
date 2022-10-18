# Faça um Programa que peça dois números e imprima o maior deles.

num1 = input("Digite um numero: ")
num2 = input("Digite outro numero: ")

if num1.isnumeric() and num2.isnumeric():
    float(num1)
    float(num2)
    if num1 > num2:
        print(f"{num1} é maior que {num2}")
    elif num1 == num2:
        print("Os números são iguais")
    else:
        print(f"{num2} é maior que {num1}")
else:
    print("Um dos numeros digitados não é um numero")
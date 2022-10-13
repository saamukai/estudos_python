# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

fahr = float(input("Digite a temperatatura em Farenheit: "))

celsius = 5*((fahr-32)/9)

print(f"A temperatura digitada é igual a {round(celsius,2)}º celsius")
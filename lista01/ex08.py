# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 

valor_hora = float(input("Digite quanto voce ganhar por hora: "))
horas = float(input("Digite quantas horas voce trabalha no mes: "))

total = valor_hora*horas

print(f"Voce ganha um total de {round(total, 2)} por mes");

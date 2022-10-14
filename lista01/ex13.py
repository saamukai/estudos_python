
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#   salário bruto.
#   quanto pagou ao INSS.
#   quanto pagou ao sindicato.
#   o salário líquido.
#   calcule os descontos e o salário líquido, conforme a tabela abaixo: 

valor_hora = float(input("Digite o valor que voce ganha por hora: "))
horas = float(input("Digite quantas horas por mes voce traballha: "))


salario_bruto = valor_hora*horas
imposto_renda = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
salario_liquido = salario_bruto - imposto_renda - inss - sindicato

print(f"\n+ Salario Bruto: {round(salario_bruto,2)} R$\n- IR: {round(imposto_renda,2)} R$\n- INSS: {round(inss,2)} R$")
print(f"- Sindicato: {round(sindicato,2)} R$\n= Salário Liquido: {round(salario_liquido,2)} R$\n")
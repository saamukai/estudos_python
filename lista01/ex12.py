# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas. 

peso = float(input("Digite o peso total de todos os peixes pescados: "))

if peso > 50:
    excedente = peso - 50;
    print(f"O peso execedente foi de {excedente} kilos")
    print(f"Você terá que pagar {round((excedente*4), 2)} reais de multa")
else:
    print(f"Voce ṕescou {peso} kilos54")
    print("Voce nao precisa pagar multa")
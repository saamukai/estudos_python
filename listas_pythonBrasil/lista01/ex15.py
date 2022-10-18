# Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

tamanho = float(input("Digite o tamanho (em me metros quadrados) da parede: "))

quantidadeLitros = tamanho/3
print(f"Você irá precisar de {quantidadeLitros:.2f} litros de tinta")

quantidadeLatas = quantidadeLitros/18
quantidadeLatas = int(quantidadeLatas+1);
print(f"Você irá precisar de {quantidadeLatas} latas")

precoTotal = float(quantidadeLatas*80.00)
print(f"Você irá pagar {precoTotal:.2f} R$")





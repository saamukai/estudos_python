# Faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;

tamanho = float(input("Digite o tamanho (em me metros quadrados) da parede: "))

quantidadeLitros = tamanho/6
print(f"Você irá precisar de {quantidadeLitros:.2f} litros de tinta")

quantidadeLatas = quantidadeLitros/18
quantidadeLatas = int(quantidadeLatas+1)

quantidadeGalao = quantidadeLitros/3.6
quantidadeGalao = int(quantidadeGalao+1)

print(f"Você irá precisar de {quantidadeLatas} latas ou {quantidadeGalao} galões")

precoLatas = float(quantidadeLatas*80.00)
precoGaloes = float(quantidadeGalao*25.00)

print(f"Você irá pagar {precoLatas:.2f} R$ se comprar somente latas")
print(f"Você irá pagar {precoGaloes:.2f} R$ se comprar somente galoes")
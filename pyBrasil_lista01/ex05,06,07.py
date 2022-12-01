# Faça um Programa que converta metros para centímetros
# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. 

from cmath import pi


raioMetro = float(input("Digite o raio do circulo em metros: "))
raioCm = raioMetro*100;
areaCm = pi*(raioCm**2)


print(f"A area do circulo em centimentros: {round(areaCm, 2)} cm²")

lado = float(input("Agora digite o lado de um quadrado: "))
areaQ = lado*lado;
print(f"O dobro da area do quadrado eh de: {areaQ*2}")


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
ano_atual = 2022
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

ano_nascimento = ano_atual - idade;
imc = peso / (altura*altura);

print(f'Noome: {nome}\nIdade: {idade}\nPeso: {peso}\nAltura: {altura}\nAno de Nascimento: {ano_nascimento}\nIMC: {imc:.2f}')